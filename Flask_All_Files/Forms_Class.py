from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField)


class InfoForm1(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    FN = StringField('Name = ')
    submit = SubmitField('Submit')


class InfoForm2(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    FN = StringField('Name = ', validators=[DataRequired()])
    VID = BooleanField("Voter ID = ")
    GEN = RadioField('Gender = ', choices=[('M', 'Male'), ('F', 'Female')])
    BC = SelectField(u'Benefits Selection = ', choices=[
                              ('pf', 'PF'), ('eps', 'EPS'), ('mc', 'Medi-Claim')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


