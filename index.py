from flask import Flask, make_response, request, current_app, jsonify, session, render_template
from flask_cors import CORS
from lib.env import *

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return "done to create project"

if __name__ == '__main__':
    app.run(debug=True, host=env("HOST"), port=env("PORT")) 