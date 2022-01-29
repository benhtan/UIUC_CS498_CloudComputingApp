from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def resp():
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()