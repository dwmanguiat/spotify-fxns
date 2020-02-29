from util import getConfig
from auth import getCCFToken
import requests
import json

config = getConfig()
keys = config["Keys"]
token = getCCFToken(keys)

searchEndPoint = "https://api.spotify.com/v1/search"

headerParams= {
    "Authorization": "Bearer {}".format(token["access_token"])
    }

queryParams = {
    "q" : "Jazz Cigarettes"
    ,"type": "playlist"
}

r = requests.get(searchEndPoint, params=queryParams, headers=headerParams)
respjson = json.loads(r.content)


#with open ("file.txt", "r+") as f:
    #f.write(str(respjson))


for line in respjson["playlists"]["items"]:
    print("name: {}, owner: {}".format(line["name"], line["owner"]["display_name"]))