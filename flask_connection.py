from flask import Flask,request, jsonify


app = Flask(__name__)

@app.route('/chat')
def chat():
    return "Hi"

if __name__ == '__main__':
    app.run(debug=True,port=5000)