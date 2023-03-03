from flask import Flask, jsonify, request
from common.preferences import DEBUG_MODE, ALLOW_HOST, LOAD_PORT
from middleware.users import User
from middleware.document import save_document
from json import loads
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

users = User()


@app.route('/')
def homes():
    return 'Привет Хакатон'


@app.route('/new_user', methods=['POST'])
def new_user():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        print(login, passw)
        return jsonify(users.create_user(login, passw))
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'False'})
    
@app.route('/posts/create', methods=['POST'])
def posts_list():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            description = jsn['description']
            text_body = jsn['text_body']
            try:    label = jsn['label']
            except: pass
            try:
                doc = jsn['document']
                doc = save_document(login, doc)
            except: doc = None
            users.create_post()
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


app.run(debug=DEBUG_MODE, host=ALLOW_HOST, port=LOAD_PORT)
