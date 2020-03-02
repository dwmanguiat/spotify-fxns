from util import getConfig
from auth import getCCFToken
import requests
import json
import pandas as pd

def getTopNPlaylists(keywordParams, resultSize, tokenDict):
    #return list/dict/dataframe of the top N playlists with given search keywords
    searchEndPoint = "https://api.spotify.com/v1/search"
    resultCount = 0
    resultDict = {}
    resultIndex = 0
    callCount = 0

    headerParams= {
    "Authorization": "Bearer {}".format(tokenDict["access_token"])
    }

    while resultCount < resultSize:

        queryParams = {
            "q" : keywordParams
            ,"type": "playlist"
            ,"limit": 50
            ,"offset": resultCount
        }

        response = requests.get(searchEndPoint, params=queryParams, headers=headerParams)
        responseJSON = json.loads(response.content)

        #add response items to result dict
        for item in responseJSON["playlists"]["items"]:
            resultDict[resultIndex] = {
                "playlist_name": item["name"]
                ,"playlist_owner": item["owner"]["display_name"]
                ,"href": item["href"]
            }
            resultIndex += 1

        if len(responseJSON["playlists"]["items"]) > resultSize:
            # procedure for a result larger than requested:
            # 
            resultCount = resultCount + len(responseJSON["playlists"]["items"])
            print(resultCount)

        if len(responseJSON["playlists"]["items"]) <= resultSize & callCount == 0:
            # procedure for a result smaller than requested on the first try:
            # exit loop
            break
        else: 
            resultCount = resultCount + len(responseJSON["playlists"]["items"])

        callCount += 1
        #TODO: add exit condition for small resultsets

    return resultDict

def main():
    config = getConfig()
    keys = config["Keys"]
    authToken = getCCFToken(keys)

    playlists = getTopNPlaylists("rainbow rock mountain", 60, authToken)

    print(pd.DataFrame(playlists).transpose())


main()