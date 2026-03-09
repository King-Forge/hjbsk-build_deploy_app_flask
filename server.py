from flask import Flask, render_template, request
from Math.mathematics import summation, subtraction, multiplication

# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if num1 is None or num2 is None:
        return {'message': 'invalid input, both parameters must be integers'}, 400

    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if num1 is None or num2 is None:
        return {'message': 'invalid input, both parameters must be integers'}, 400

    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if num1 is None or num2 is None:
        return {'message': 'invalid input, both parameters must be integers'}, 400

    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
