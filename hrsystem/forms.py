from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import random


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AddForm(FlaskForm):
    subsidiary = SelectField('Subsidiary', choices=[
                             ('CZ', 'CZ'), ('SK', 'SK')])
    id = StringField()
    citizenship = StringField('Citizenship', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    country_of_residence = StringField(
        'Country of Residence', validators=[DataRequired()])
    date_of_birth = StringField('Date of Birth', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    national_id = StringField('National ID', validators=[DataRequired()])
    email = StringField('Personal e-mail', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    street_address = StringField('Address', validators=[DataRequired()])
    telephone_number = StringField(
        'Telephone Number', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    band = StringField('Band', validators=[DataRequired()])
    contract_beginning = StringField(
        'Contract Start', validators=[DataRequired()])
    contract_end = StringField('Contract End', validators=[DataRequired()])
    contract_type = SelectField('Contract Type', choices=[(
        'Permanent', 'Permanent'), ('Temporary', 'Temporary')])
    department = StringField('Department', validators=[DataRequired()])
    employment_status = SelectField(
        'Employment Status', choices=[('0', '0'), ('1', '1')])
    fte = StringField('FTE', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    is_manager = SelectField('Is manager', choices=[('1', 'Yes'), ('0', 'No')])
    job_title = StringField('Job Title', validators=[DataRequired()])
    manager = StringField('Manager Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
