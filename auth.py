import requests
import json

clientID = "f2d5518c716c40548eb55e289525bb1f"
secrectKey = "9ec6fed8800540d4971c9444823e09c9"
tokenEndpoint = "https://accounts.spotify.com/api/token"
playlistEndpoint = "https://api.spotify.com/v1/me/playlists"

params= {
    "client_id": clientID
    ,"client_secret": secrectKey
    ,"grant_type": "client_credentials"
}

response = requests.post(tokenEndpoint, params)
payload = json.loads(response.content.decode('utf-8'))

authHeaders = {"Authorization": "Bearer {}".format(payload["access_token"])}
print(authHeaders)

response2 = requests.get(playlistEndpoint, headers=authHeaders)

payload2 = json.loads(response2.content.decode('utf-8'))

print(payload2)