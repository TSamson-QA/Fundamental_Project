from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.38.52:3306/model_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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