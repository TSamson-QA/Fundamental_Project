from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

db = SQLAlchemy(app)

class Paints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paint_name = db.Column(db.String(50), nullable=False)
    needed = db.Column(db.Boolean, nullable=False)
    paint = db.relationship('Models', backref='Paints')
    

class Models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50), nullable=False)
    paint_id = db.Column(db.Integer, db.ForeignKey('paints.id'), nullable=False)
    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')