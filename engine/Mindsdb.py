from dotenv import load_dotenv
import requests
import os

load_dotenv()

def login_to_cloud():
    session = requests.Session()
    response = session.post("https://cloud.mindsdb.com/cloud/login", json={
        "email": os.getenv("USER_ID"),
        "password": os.getenv("PASSWORD")
    })
    if response.status_code == 200:
        return session.cookies
    raise Exception(f"Failed to login: {response.text}")
