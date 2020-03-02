from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World3!'

@app.route('/sanity')
def sanity():
    return 'deploy done!!!'

@app.route('/try')
def try_out():
    return 'try out'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
