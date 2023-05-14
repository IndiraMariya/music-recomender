import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import requests
import json
import os

def callurl (auth_url):
    response = requests.get(auth_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the response content
        # Process the content as needed
        # cont = response.data
        print(json.dumps(response.text))
        # return(cont["code"])
    else:
        print(f"Request failed with status code: {response.status_code}")


load_dotenv('.env')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')


scope = 'user-library-read playlist-read-private user-top-read'  # Set the required scope for your application

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

auth_url = sp_oauth.get_authorize_url()
print("Please visit this URL to authorize the application:", auth_url)

# After authorization, the user will be redirected to the redirect URI.
# Extract the authorization code from the redirected URL
# code = input("Enter the code from the returned URL: ")

code = callurl(auth_url)

# token_info = sp_oauth.get_access_token(code)
# access_token = token_info['access_token']
# refresh_token = token_info['refresh_token']

# sp = spotipy.Spotify(auth=access_token)

# # Fetch user's playlists
# playlists = sp.current_user_playlists()
# for playlist in playlists['items']:
#     print(playlist['name'])
