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
    # try:s
    jsn = loads(request.data)
    login = jsn['login']
    passw = jsn['passw']
    mail = jsn['mail']
    return jsonify(users.create_user(login, passw,mail))
    # except Exception as _ex:
    #     print(_ex)
    #     return jsonify({'status': 'False'})
    
# @app.route('/confirmation/<link>', methods=['POST'])
# def confirmation_new_user(link):
#     try:
#         return jsonify(users.create_user(login, passw,mail))
#     except Exception as _ex:
#         print(_ex)
#         return jsonify({'status': 'False'})


@app.route('/question/create', methods=['POST'])
def posts_create():
    try:
        jsn = loads(request.data)
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


@app.route('/question/<int:post_id>/answer', methods=['POST'])
def posts_answer(post_id):
    try:
        jsn = loads(request.data)
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            post_id = str(post_id)
            body = jsn['text_body']
            try:
                doc = jsn['document']
            except:
                doc = None
            try:
                id_answ = jsn['id_answ']
            except:
                id_answ = None
            users.create_answ(login, body, post_id, doc, id_answ)
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})

@app.route('/auth', methods=['POST'])
def auth():
    try:
        jsn = loads(request.data)
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        return jsonify({'status': 'Erore'})

@app.route('/questions', methods=['POST'])
def posts_read():
    try:
        jsn = loads(request.data)
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            try:
                filter = jsn['filter']
            except:
                filter = None
            return jsonify(users.read_posts(filter))
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


@app.route('/question/<int:post_id>', methods=['POST'])
def posts_read_question(post_id):
    try:
        jsn = loads(request.data)
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            return jsonify(users.read_current_post(str(post_id)))
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})
    
@app.route('/question/<int:post_id>/statis')
def question_statis(post_id):
    return jsonify({'status': 'True'})
    
@app.route('/profile', methods=['POST'])
def profile_info():
    try:
        jsn = loads(request.data)
        login = jsn['login']
        passw = jsn['passw']
        if users.check_user(login, passw):
            return jsonify(users.read_current_user(login))
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


app.run(debug=DEBUG_MODE, host=ALLOW_HOST, port=LOAD_PORT)
