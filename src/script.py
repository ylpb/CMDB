from lib.conf.config import settings
from src.client import Agent,mySSh

def run():
    if settings.MODE == 'agent':
        obj = Agent()

    else:
        obj = mySSh()
    obj.collectAndPost()