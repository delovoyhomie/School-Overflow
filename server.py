from flask import Flask, jsonify, request
from common.preferences import DEBUG_MODE, ALLOW_HOST, LOAD_PORT
from middleware.users import User


app = Flask(__name__)
users = User()


@app.route('/')
def homes():
    return 'Привет Хакатон'


@app.route('/new_user', methods=['POST'])
def new_user():
    try:
        login = request.form['login']
        passw = request.form['passw']
        print(login, passw)
        return jsonify(users.create_user(login, passw))
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'False'})
    
@app.route('/posts/create', methods=['POST'])
def posts_list():
    try:
        login = request.form['login']
        passw = request.form['passw']
        if users.check_user(login, passw):
            description = request.form['description']
            text_body = request.form['text_body']
            try:    label = request.form['label']
            except: pass
            try:    doc = request.form['document']
            except: pass
            
            return jsonify({'status': 'True'})
        return jsonify({'status': 'IncorrectValue'})
    except Exception as _ex:
        print(_ex)
        return jsonify({'status': 'Erore'})


app.run(debug=DEBUG_MODE, host=ALLOW_HOST, port=LOAD_PORT)
