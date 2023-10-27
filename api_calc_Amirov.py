from flask import Flask, request, jsonify

app = Flask(__name__) 

@app.route('/plus', methods=['POST'])
def plus():
    req = request.get_json()
    a = req['a']
    b = req['b']
    result = a + b
    return jsonify({'result': result})

@app.route('/minus', methods=['POST'])
def minus():
    req = request.get_json()
    a = req['a']
    b = req['b']
    result = a - b
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    req = request.get_json()
    a = req['a']
    b = req['b']
    result = a*b
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    req = request.get_json()
    a = req['a']
    b = req['b']
    if b==0:
        return "Ошибка: введите корректное значение второго числа...", 400
    result = a/b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
