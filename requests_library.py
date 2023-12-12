from requests import get
import json

artist = input("Write down the name of the artist you want to check: ")
response =  get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist)

# .json will convert the response to a json file
reponse_json_format = response.json()

# using the json library to help better format the json file
response_better_json_formatted = json.dumps(reponse_json_format, indent = 2)

for result in reponse_json_format["results"]:
    print(result["trackName"])