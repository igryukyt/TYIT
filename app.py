from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/attendance.db'
db = SQLAlchemy(app)

# Import models and routes (You’ll get them)
from models import *
from routes import *

if __name__ == "__main__":
    app.run(debug=True)
