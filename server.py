from flask import Flask, jsonify, request
from common.preferences import DEBUG_MODE, ALLOW_HOST, LOAD_PORT
from middleware.users import User
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
        mail = jsn['mail']
        print(login, passw, mail)
        return jsonify(users.create_user(login, passw,mail))
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'False'})


@app.route('/posts/create', methods=['POST'])
def posts_create():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            description = jsn['description']
            text_body = jsn['text_body']
            try:
                label = jsn['label']
            except:
                label = None
            try:
                doc = jsn['document']
            except:
                doc = None
            users.create_post(login, description, text_body, label, doc)
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


@app.route('/posts/answer', methods=['POST'])
def posts_answer():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            post_id = jsn['post_id']
            body = jsn['text_body']
            try:
                doc = jsn['document']
            except:
                doc = None
            users.create_answ(login, body, post_id, doc)
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


@app.route('/posts', methods=['POST'])
def posts_read():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            try:
                filter = jsn['filter']
            except:
                label = None
            return jsonify(users.read_posts(filter))
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


@app.route('/posts/question', methods=['POST'])
def posts_read_question():
    try:
        jsn = loads(request.data.decode()[5:])
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            post_id = jsn['post_id']
            return jsonify(users.read_current_post(post_id))
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


app.run(debug=DEBUG_MODE, host=ALLOW_HOST, port=LOAD_PORT)
