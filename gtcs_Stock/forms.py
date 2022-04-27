from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Company Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    location = StringField('Location', validators=[DataRequired()])
    phn_number = IntegerField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class NewLogin(FlaskForm):
    comp_name = StringField('Company Name', validators=[DataRequired()])
    website = StringField('Company Website', validators=[DataRequired()])
    regd_address = StringField('Regd Address', validators=[DataRequired()])
    work_address = StringField('Work Address', validators=[DataRequired()])
    type_of_business = SelectField('Select From The List', choices=[('Garments','Garments'), ('Electronics','Electronics'), ('Grosseries','Grosseries'),('MobileShop', 'Mobile Shop'), ('jaars', 'Water Jar Supply')])
    pincode = IntegerField('Pincode', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    vat = IntegerField('Vat Number', validators=[DataRequired()])
    tin = IntegerField('Tin Number', validators=[DataRequired()])
    gstin = IntegerField('GSTIN Number', validators=[DataRequired()])
    cin = IntegerField('CIN Number', validators=[DataRequired()])
    pan = IntegerField('PAN Number', validators=[DataRequired()])
    service_tax = IntegerField('Service Tax Number', validators=[DataRequired()])
    mfg = IntegerField('Mfg.License Number', validators=[DataRequired()])
    dl = IntegerField('DL Number', validators=[DataRequired()])
    telephone = IntegerField('Telephone Number', validators=[DataRequired()])
    fax = IntegerField('Fax Number', validators=[DataRequired()])
    submit = SubmitField('Save')





