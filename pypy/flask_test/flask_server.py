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


@app.route('/global/control/server_maps')
def test2():
    value = [
        {
            "ip": "47.110.92.112",
            "port": 62345
        }
    ]
    print("-----------")
    print(request.url)
    return jsonify(value)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=62242)
