#!flask/bin/python
from flask import Flask, request, render_template
from os import environ
import sys


print("*************", __name__, file=sys.stderr)
app = Flask(__name__)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/')
def index():
    return "bonjour world"

@app.route('/food')
def shoe():
    return "bonjour food"


@app.route('/', methods=['POST'])
def index_post():
    return "bye world"

@app.errorhandler(404)
def page_not_found(e):
    code = '404'
    print("---------------------- COWABUNGE", file=sys.stderr)
    # print("page "+ e + "not found\n", file=sys.stderr)
    return "page-----"+ str(e) + "-----not found\n"
    #render_template('error.html', code=code), 404


@app.errorhandler(500)
def internal_server_error(e):
    code = '500'
    return "bad feet" #render_template('error.html', code=code), 500


@app.errorhandler(503)
def service_unavailable(e):
    code = '503'
    return "bad rice" #render_template('error.html', code=code), 503


if __name__ == '__main__':
    PORT = 8080
    # PORT = environ.get('PORT') or 8080
    # if sys.version_info[0] < 3 and sys.version_info[1] < 2:
        # print('Requires minimum Python 3.2')
        # quit()
    app.run(host='0.0.0.0', port=PORT)
