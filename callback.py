from flask import Flask, request
import json
import jsonify

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    # Handle the Spotify authorization callback here
    # You can access the authorization code or access token from the request parameters
    
    # Example: Print the authorization code or access token
    code = request.args.get('code')
    access_token = request.args.get('access_token')
    # print(f"Authorization Code: {code}")
    # print(f"Access Token: {access_token}")  
    
    #Generate or retrieve your data
    data = {'jwt': code}
    print(data)
    # Set the response header
    headers = {'Content-Type': 'application/json'}

    # Return the JSON response
    return json.dumps(data), 200, headers


if __name__ == '__main__':
    app.run(port=8888)