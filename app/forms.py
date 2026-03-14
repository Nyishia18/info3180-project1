from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=0)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0)])
    location = StringField('Location', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    submit = SubmitField('Add Property')