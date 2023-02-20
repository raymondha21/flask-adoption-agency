from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators, SelectField,IntegerField,BooleanField

class AddPetForm(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet Name",[validators.InputRequired()])
    species = StringField("Species",[validators.InputRequired(),validators.AnyOf(['Dog','Cat','Porcupine'])])
    photo_url = StringField("Photo URL",[validators.Optional(),validators.URL()])
    age = IntegerField("Age",[validators.Optional(),validators.NumberRange(min=0,max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editting pet"""

    photo_url = StringField("Photo URL",[validators.Optional(),validators.URL()])
    notes = StringField("Notes",[validators.Optional()])
    available = BooleanField("Available")