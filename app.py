from flask import Flask
from os import environ

app = Flask(__name__)
app.config['TESTING'] = True

SECRET_KEY = environ.get("OPENAI_API_KEY")

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to our RAG test Api: ' + SECRET_KEY

if __name__ == '__main__':
   app.run(debug=True)