from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/index")
def index():
    if request.environ.get("HTTP_ORIGIN"):
        print(request.environ["HTTP_ORIGIN"])
    else:
        print("not http_origin")
    return jsonify(status=200, msg="ok")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
