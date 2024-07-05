from flask import Flask, jsonify, request
from flask_cors import CORS
import requests as http

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def upload_fcm_token():
    return jsonify({'hello':'world'}), 200
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=7000)
