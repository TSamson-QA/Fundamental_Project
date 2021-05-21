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
    added = db.Column(db.Boolean, default=False)

class SelectModel(FlaskForm):
    
    model_select = SelectField()

    def __init__(self):
        super(SelectModel, self).__init__()
        self.model_select.choices = [(x.id, x.model_name) for x in Models.query.all()]
        

    select = SubmitField("Select")

@app.route('/', methods=['POST', 'GET'])
def index():
    form = SelectModel()
    selected_models = Models.query.filter_by(added = True).all()
    added_paint = Paints.query.filter_by(needed = True).all()
    return render_template('index.html', form=form, selected_models=selected_models, added_paint=added_paint)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = SelectModel()

    
    if form.validate_on_submit():
        added_model = Models.query.filter_by(id = form.model_select.data).first()
        added_model.added = True

        added_paint_id = added_model.paint_id
        added_paint = Paints.query.filter_by(id = added_paint_id).first()
        added_paint.needed = True

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)






if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')