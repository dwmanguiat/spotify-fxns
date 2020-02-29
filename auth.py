import requests
import json
import util

config = util.getConfig()
keys = config["Keys"]
print(keys)


tokenEndpoint = "https://accounts.spotify.com/api/token"
playlistEndpoint = "https://api.spotify.com/v1/me/playlists"

params= {
    "client_id": keys["ClientID"]
    ,"client_secret": keys["SecretKey"]
    ,"grant_type": "client_credentials"
}

response = requests.post(tokenEndpoint, params)
payload = json.loads(response.content.decode('utf-8'))

authHeaders = {"Authorization": "Bearer {}".format(payload["access_token"])}
print(authHeaders)

response2 = requests.get(playlistEndpoint, headers=authHeaders)

payload2 = json.loads(response2.content.decode('utf-8'))

print(payload2)