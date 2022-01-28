# Put your app in here.
from flask import Flask, request
from operations import add, div, mult, sub

app = Flask(__name__)

"""
@app.route("/add")
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)
    return str(sum)

@app.route("/div")
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    quotient = div(a, b)
    return str(quotient)

@app.route("/mult")
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    product = mult(a, b)
    return str(product)

@app.route("/sub")
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    difference = sub(a, b)
    return str(difference)
"""

@app.route("/math/<operator>")

def do_math(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operator == "add":
        result = add(a, b)
        return str(result)
    elif operator == "div":
        result = div(a, b)
        return str(result)
    elif operator == "mult":
        result = mult(a,b)
        return str(result)
    else:
        result = sub(a,b)
        return str(result)
