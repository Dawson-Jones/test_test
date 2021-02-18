from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/xxx', methods=['POST'])
def index():
    v = request.values
    print(v)
    key = v.get("key")
    return key, 200


@app.route('/monitor_event', methods=['GET', 'POST'])
def test():
    data = request.get_json(force=True)
    print(data)
    return 'haha', 200


@app.route('/pic_catcher/alive')
def test2():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True, port=8090)
