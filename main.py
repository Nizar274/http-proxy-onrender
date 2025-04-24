from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path):
    target_url = f"http://example.com/{path}"  # بس placeholder
    if request.method == "POST":
        resp = requests.post(target_url, data=request.data)
    else:
        resp = requests.get(target_url, params=request.args)

    return Response(resp.content, status=resp.status_code)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
