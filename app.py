from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World2!'

@app.route('/sanity')
def hello_world():
    return 'deploy done!!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
