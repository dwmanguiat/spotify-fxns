import os
import json

def getConfig():
    with open("resources\\keys.json") as cfg:
        config = json.load(cfg)

    return config
