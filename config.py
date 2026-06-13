import os
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("MYSQL_HOST")
password=os.getenv("MYSQL_PASSWORD")
api_key=os.getenv("API_KEY")
user=os.getenv("MYSQL_USER")
db=os.getenv("MYSQL_DATABASE")