from flask import Flask # importing Library
import flask
from flask import request,jsonify
app = Flask(__name__)

import compiler

@app.route('/hello/') # Making Endpoint
def hello_world(): # defining function for endpoint
    return 'This is my first API call!' # Returning Data

@app.route('/test/') # Making Endpoint
def test(): # defining function for endpoint
    return 'Test Endpoint' # Returning Data

@app.route('/compile/') # Endpoint for Code Compilation
def compile_code():

    # Parsing the Headers
    code = request.args.get('code')
    input_str = request.args.get('input_str')

    # Running the code
    result = compiler.compile(code,input_str)
    # Returning the jSon object
    return jsonify(result)

if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=1212) # Starting our API
