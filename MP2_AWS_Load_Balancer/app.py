from flask import Flask, request, jsonify
app = Flask(__name__)

seed = 0

@app.route('/', methods = ['POST', 'GET'])
def resp():
    global seed
    if request.method == 'POST':
        seed = int(request.json.get('num'))
        print(f'POST: {seed}')
        return jsonify(success=True)
    else:
        print(f'GET: {seed}')
        return str(seed)

if __name__ == '__main__':
    app.run()