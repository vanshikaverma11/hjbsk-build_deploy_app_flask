from flask import Flask, request, render_template
from Maths.mathematics import summation, subtraction, multiplication

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum", methods=["GET"])
def calculate_sum():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = summation(num1, num2)
    return f"The result of the summation is: {result}"

@app.route("/sub", methods=["GET"])
def calculate_subtraction():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = subtraction(num1, num2)
    return f"The result of the subtraction is: {result}"

@app.route("/mul", methods=["GET"])
def calculate_multiplication():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = multiplication(num1, num2)
    return f"The result of the multiplication is: {result}"

if __name__ == "__main__":
    app.run(debug=True)
