from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask import render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.38.52:3306/model_database"
#getenv('DATABASE_URI')
app.config['SECRET_KEY'] = "bncubcobcp"
#getenv("SECRET_KEY")

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
    added = db.Column(db.Boolean)

class SelectModel(FlaskForm):
    model_select = SelectField("Please choose your model:",
        choices=[
            ("UM","Ultramarines"), ("Orks", "Orks"), ("BA","Blood Angels"), 
            ("BT","Black Templars"), ("Necrons","Necrons"), ("Tau", "Tau"), 
            ("GrK","Grey Knights"), ("ImF","Imperial Fists")
        ],
        validators = [DataRequired()]
    )
    select = SubmitField("Select")

@app.route('/', methods=['POST', 'GET'])
def index():
    form = SelectModel()
    model_select = form.model_select.data
    select = form.select
    addform = SelectModel()
        
    return render_template('index.html', form=form, model_select=model_select, select=select, addform=addform)





if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')