# --------------Practice start--------------
from flask import Flask, jsonify, request
# --------------Practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# --------------Practice start--------------
@app.route('/json', methods=["POST"])
def process_json():
    print(vars(request))
    json_req = request.get_json()  # reviset to get_json(force=True) if Content-Type isn't application/json 
    if type(json_req) == list:
        res = json_req+["processed by flask"]
    elif type(json_req) == dict:
        json_req.update({"add by flask": "processed by flask"})
        res = json_req
    return jsonify(res)
# --------------Practice end--------------

if __name__ == '__main__':
    app.run(debug=True)