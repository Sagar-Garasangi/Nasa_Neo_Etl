import pandas as pd
import mysql.connector
from config import host, user, password, db


def load_data(asteroid_path, close_approach_path):

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )

    cursor = conn.cursor()

    asteroids_df = pd.read_parquet(
        asteroid_path
    )

    close_approach_df = pd.read_parquet(
        close_approach_path
    )
    cursor.execute("""USE nasa_neo""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asteroids(
        id VARCHAR(50) PRIMARY KEY,
        neo_reference_id VARCHAR(50),
        name VARCHAR(255),
        magnitude FLOAT,
        is_hazardous BOOLEAN,
        is_sentry BOOLEAN NULL,
        diameter_min_km FLOAT,
        diameter_max_km FLOAT,
        nasa_jpl_url TEXT,
        api_self_url TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS close_approaches(
    asteroid_id VARCHAR(50),
    asteroid_name VARCHAR(100),
    close_approach_date DATE,
    velocity_kph FLOAT,
    miss_distance_km FLOAT,
    orbiting_body VARCHAR(50),
    FOREIGN KEY (asteroid_id)
        REFERENCES asteroids(id)
    )
    """)
    asteroid_sql = """
    INSERT IGNORE INTO asteroids
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    asteroid_data = list(
        asteroids_df.itertuples(index=False, name=None)
    )
    cursor.executemany(
    asteroid_sql,
    asteroid_data
    )
   
    approach_sql = """
    INSERT INTO close_approaches(
        asteroid_id,
        asteroid_name,
        close_approach_date,
        velocity_kph,
        miss_distance_km,
        orbiting_body
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    
    close_approach_df = close_approach_df[
    [
        "id",
        "name",
        "close_approach_date",
        "velocity_kph",
        "miss_distance_km",
        "orbiting_body"
    ]
    ]
    close_approach_df["velocity_kph"] = pd.to_numeric(
    close_approach_df["velocity_kph"]
    )

    close_approach_df["miss_distance_km"] = pd.to_numeric(
    close_approach_df["miss_distance_km"]
    )

    approach_data = list(
        close_approach_df.itertuples(index=False, name=None)
    )
    print(close_approach_df.dtypes)

    print(close_approach_df.columns.tolist())

    print(approach_data[0])

    for i, value in enumerate(approach_data[0]):
        print(i, value, type(value))


    cursor.executemany(
        approach_sql,
        approach_data
    )

    conn.commit()

    print(
        f"Loaded {len(asteroids_df)} asteroids and "
        f"{len(close_approach_df)} close approaches"
    )

    cursor.close()
    conn.close()
load_data("asteroids.parquet","close_approach.parquet")
print("load succesfull")