from flask import Flask # importing Library
app = Flask(__name__)

@app.route('/hello/') # Making Endpoint
def hello_world(): # defining function for endpoint
    return 'This is my first API call!' # Returning Data

@app.route('/test/') # Making Endpoint
def test(): # defining function for endpoint
    return 'Test Endpoint' # Returning Data

if __name__ == '__main__': 
    app.run(port=1212) # Starting our API
