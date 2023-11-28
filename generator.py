from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return jsonify({'msg': 'Hello It worked'})

if __name__ == "__main__":
    app.run(debug=True)
