from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ HTTP Proxy Server is up and running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
