import os
from instagrapi import Client
from .settings import USERNAME, PASSWORD

def get_insta_client():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cl = Client()
    cl.load_settings(BASE_DIR+"/session.json")
    cl.login(USERNAME, PASSWORD)
    return cl
