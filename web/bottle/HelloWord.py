from bottle import *
from bottle import request, response

"""
#import gevent,sys
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
"""
"""
@route('/')
@route('/hello/<name>/<pw:int>')
def greet(name='Stranger', pw=123):
    return template('Hello {{name}}, how are you? {{pwd}}', name=name, pwd=str(pw))
"""
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    if username == 'ly':
        return True
    else:
        return False

@route('/restricted')
def restricted_area():
    t2 = request.get_cookie("account", secret='some-secret-key')
    username = str(t2).split(";")[0]
    right =str(t2).split(";")[1]
    if username:
        return template("Hello {{name}}. Welcome back. right: {{right}}", name=username, right=right)
    else:
        return "You are not logged in. Access denied."

run(host='localhost', port=8080)


#run(host='localhost', port=8080, server='gevent')
