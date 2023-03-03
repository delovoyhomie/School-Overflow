from flask import Flask, jsonify, request
from common.preferences import DEBUG_MODE, ALLOW_HOST, LOAD_PORT
from middleware.users import User


app = Flask(__name__)
users = User()

@app.route('/')
def homes():
    return 'Привет Хакатон'

@app.route('/new_user')
def new_user():
    return "status"

app.run(debug=DEBUG_MODE, host=ALLOW_HOST, port=LOAD_PORT)
