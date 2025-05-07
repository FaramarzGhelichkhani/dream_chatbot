import os
from instagrapi import Client
from .settings import USERNAME, PASSWORD

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings(BASE_DIR+"/session.json")
