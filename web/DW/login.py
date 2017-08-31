from bottle import *
#from gevent import monkey; monkey.patch_all()

css_path = './css'
@route('/css/<filename:re:.*\.css>')
def server_static(filename):
    return static_file(filename, root=css_path)
img_path = './image'
@route('/image/<filename:re:.*\.jpg>')
def server_static(filename):
    return static_file(filename, root=img_path)
js_path = './statics/js'
@route('/statics/js/<filename:re:.*\.js>')
def server_static(filename):
    return static_file(filename, root=js_path)


@route('/')
@route('/hello/<name>/<pw:int>')
def greet(name='Stranger', pw=123):
    return template('Hello {{name}}, how are you? {{pwd}}', name=name, pwd=str(pw))

@get('/login') # or @route('/login')
def login():
#    name = edit = request.GET.get('username','').strip()
    return template("login.html")
#    return template("login.html", name=username, password=password)

#    return '''
#        <form action="/login" method="post">
#            Username: <input name="username" type="text" />
#            Password: <input name="password" type="password" />
#            <input value="Login" type="submit" />
#        </form>
#    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
#如果登录成功把用户名了权限用secret加密后写入cookie中
    username = request.forms.get('username')
    password = request.forms.get('password')
    right = 'abc123'
    if check_login(username, password):
        response.set_cookie("account", username+';'+right, secret='some-secret-key')
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
#从cookie中读出登录用户的用户名的权限，解密密钥在secret中
    username = request.get_cookie("account", secret='some-secret-key')
    rig = str(username).split(';')
    username = rig[0]
    rig = rig[1]
    if username:
        return template("Hello {{name}}. Welcome back. right {{right}}", name=username, right=rig)
    else:
        return "You are not logged in. Access denied."

#run(host='localhost', port=8080, server='gevent')
run(host='localhost', port=8080)
