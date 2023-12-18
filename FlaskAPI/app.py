from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello world '

if  __name__ == '__main__':
    app.run(debug=True)