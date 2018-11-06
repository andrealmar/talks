__author__ = 'andrealmar'

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello #CPMG3 !!!"

@app.route("/add") # exemplo de chamada URL: http://localhost:5000/add?a=1&b=5
def add():
    try:
        num1 = int(request.args.get('a'))
        num2 = int(request.args.get('b'))
        return jsonify({'resultado': num1 + num2})
    except Exception as e:
        return jsonify({'resultado': "OCORREU O SEGUINTE ERRO: " + str(e)})

@app.route("/subtract") # exemplo de chamada URL: http://localhost:5000/subtract?a=1&b=5
def subtract():
    try:
        num1 = int(request.args.get('a'))
        num2 = int(request.args.get('b'))
        return jsonify({'resultado': num1 - num2})
    except Exception as e:
        return jsonify({'resultado': "OCORREU O SEGUINTE ERRO: " + str(e)})

@app.route("/multiply") # exemplo de chamada URL: http://localhost:5000/multiply?a=2&b=5
def multiply():
    try:
        num1 = int(request.args.get('a'))
        num2 = int(request.args.get('b'))
        return jsonify({'resultado': num1 * num2})
    except Exception as e:
        return jsonify({'resultado': "OCORREU O SEGUINTE ERRO: " + str(e)})

@app.route("/divide") # exemplo de chamada URL: http://localhost:5000/divide?a=10&b=2
def divide():
    try:
        num1 = int(request.args.get('a'))
        num2 = int(request.args.get('b'))
        return jsonify({'resultado': num1 / num2})
    except Exception as e:
        return jsonify({'resultado': "OCORREU O SEGUINTE ERRO: " + str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
