from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
