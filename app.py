from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Welcome', username='WSB')


@app.route('/index/<name>')
def hello(name):
    return render_template('index.html', title='Welcome', username=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('hello', name=user))
    else:
        user = request.args.get('name')
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
