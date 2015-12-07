from bottle import run, route, template, static_file, view

@route('/')
@view('static/index.html')
def index():
    posts = [
        {
            'author': 'HuaiShao',
            'message': 'Hello, Bottle.py'
        }
    ]
    
    for i in range(10):
        posts.append({
            'author': 'User #%d' % (i + 100),
            'message': 'I Love Python.' * (i + 1)
        })
    return {'posts': posts}
    #return template('static/index.html')

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

run()