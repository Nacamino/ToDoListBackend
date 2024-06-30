from flask import Flask, request, send_from_directory
import uuid
import os
import json

app = Flask(__name__, static_url_path='/static/')

@app.route('/')
def index():
    return send_from_directory('', './static/web.html')

if __name__ == '__main__':
    # os.makedirs("./predictions/images", exist_ok=True)
    # os.makedirs("./predictions/text", exist_ok=True)
    # os.makedirs("./predictions/json", exist_ok=True)
    os.makedirs("./Login", exist_ok=True)

    app.run(host='0.0.0.0', debug=True)
