from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def home():
    return template('page')

run(host='localhost', port=8080, debug=True)