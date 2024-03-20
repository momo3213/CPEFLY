from markupsafe import escape
from flask import Flask

app = Flask(__name__)

users = ['Bob', 'Jane', 'Adam']

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    if 0 <= user_id < len(users):
        return '<h2>Hi {}</h2>'.format(escape(users[user_id]))
    else:
        abort(404)

if __name__ == '__main__':
    app.run()