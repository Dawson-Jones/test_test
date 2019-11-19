from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    dic = dict()
    data_dict = {
        "NG隐裂": ["5-11", "5-11", "5-11"],
        "NG混档": ["5-11", "5-11"],
        "NG其他": ["5-11", "5-11", "5-11", "5-11"],
        "NG失效": ["5-11"],
        "NG破片": ["5-11"],
        "NG虚焊": ["5-11"],
        "NG断栅": ["5-11"]
    }
    dic['defects'] = data_dict
    data = json.dumps(dic)
    print(data)
    # return jsonify(num=400, msg='errno')
    return data, 200


@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.get_json(force=True)
    print(data)
    return 'haha', 200


if __name__ == '__main__':
    app.run(debug=True)
