import http.server
import socketserver
from flask import Flask

# Define the server address and port
host = 'localhost'
port = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host=host, port=port)
