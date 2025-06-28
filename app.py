from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_api():
    name = request.args.get('name', 'Nayan')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run()
