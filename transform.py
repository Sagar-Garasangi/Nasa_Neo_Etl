import pandas as pd
df_data=pd.read_parquet("Nasa.parquet")
df_data = df_data.rename(columns={
    "estimated_diameter.kilometers.estimated_diameter_min": "diameter_min_km",
    "estimated_diameter.kilometers.estimated_diameter_max": "diameter_max_km",
    "absolute_magnitude_h": "magnitude",
    "is_potentially_hazardous_asteroid": "is_hazardous",
    "is_sentry_object": "is_sentry",
    "links.self": "api_self_url"
})

df_data = df_data[
    [
        "id",
        "neo_reference_id",
        "name",
        "magnitude",
        "is_hazardous",
        "is_sentry",
        "diameter_min_km",
        "diameter_max_km",
        "nasa_jpl_url",
        "api_self_url",
        "close_approach_data"
    ]
]
asteroids_df = df_data.drop(
    columns=["close_approach_data"]
)
asteroids_df.to_parquet(
    "asteroids.parquet",
    index=False
)
df_closed_approach=df_data.explode("close_approach_data")
df_closed_approach_parent=df_closed_approach[["id","name"]]
df_closed_approach_normalize=pd.json_normalize(df_closed_approach["close_approach_data"])
df_close_approach_normalize=df_closed_approach_normalize[
    [
        "close_approach_date",
        "orbiting_body",
        "relative_velocity.kilometers_per_hour",
        "miss_distance.kilometers"
    ]]
df_close_approach_normalize=df_close_approach_normalize.rename(
    columns={
        "id":"asteroid_id",
        "relative_velocity.kilometers_per_hour":"velocity_kph",
        "miss_distance.kilometers":"miss_distance_km"
    }
)

df_close_approach_main=pd.concat([df_closed_approach_parent.reset_index(drop=True),df_close_approach_normalize.reset_index(drop=True)],axis=1)
df_close_approach_main.to_parquet("close_approach.parquet")
df_close_approach_main["velocity_kph"] = pd.to_numeric(
    df_close_approach_main["velocity_kph"]
)

df_close_approach_main["miss_distance_km"] = pd.to_numeric(
    df_close_approach_main["miss_distance_km"])
df_close_approach_main = df_close_approach_main[
    [
        "id",
        "name",
        "close_approach_date",
        "velocity_kph",
        "miss_distance_km",
        "orbiting_body"
    ]
]
print(df_close_approach_main.dtypes)
print(df_close_approach_main.columns)
print("Extract successfull")