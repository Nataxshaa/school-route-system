from bottle import route, run

@route('/hello')
def hello(): 
    return "Hello, World!"  

if __name__ == '__main__': #impede que o arquivo seja executado sempre que for importado
    run(host='localhost', port=8080)