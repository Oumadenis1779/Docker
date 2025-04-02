from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Docker python World!'
@app.route('/health')
def hello():
    return {'Hello, Flask!': 'Hello, Docker python World!'}, 200
    

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)