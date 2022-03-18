from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/Hello', methods = ['GET', 'POST'])
def Hello(name=None,a=1,b=2):
    return jsonify(200)    
    
@app.route('/', methods = ['GET'])
def FirstGet():
    return jsonify(200)    
    
if __name__ == '__main__':
    app.run(host='localhost', port=5700)

