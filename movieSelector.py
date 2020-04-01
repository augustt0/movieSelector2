import requests
import config

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"page":"1","r":"json","s":"Avengers Endgame"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': config.api_key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)