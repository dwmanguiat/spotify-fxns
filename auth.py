import requests
import json
import util

def getCCFToken(keys):
    CCFTokenEndpoint = "https://accounts.spotify.com/api/token"
    params= {
    "client_id": keys["ClientID"]
    ,"client_secret": keys["SecretKey"]
    ,"grant_type": "client_credentials"
    }

    response = requests.post(CCFTokenEndpoint, params)
    payload = json.loads(response.content.decode('utf-8'))

    return payload

