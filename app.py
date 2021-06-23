from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap = Bootstrap(app)

@app.route('/')
def main():
    abort(404)
    return '<h1>Hello World!</h1>'

@app.route('/name/<test>')
def name(test):
    return '<h1>NAME!</h1> : ' + test

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', test=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

