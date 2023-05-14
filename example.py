from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Generate or retrieve your data
    data = {'key': 'value'}

    # Set the response header
    headers = {'Content-Type': 'application/json'}

    # Return the JSON response
    return jsonify(data), 200, headers

if __name__ == '__main__':
    app.run()
