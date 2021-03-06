from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class add_cust(FlaskForm):
    first_name= StringField('first_name')
    last_name= StringField('last_name')
    address= StringField('address')
    phone_no= StringField('phone_no')
    e_mail= StringField('e_mail')
    submit = SubmitField('Add Customer')

class add_order(FlaskForm):
    item= StringField('item')
    quantity= IntgerField('quantity')
    price= IntegerField('price')
    submit = SubmitField('addd order')

class update_cust(FlaskForm):
    first_name= StringField('first_name')
    last_name= StringField('last_name')
    address= StringField('address')
    phone_no= StringField('phone_no')
    e_mail= StringField('e_mail')
    submit = SubmitField('Update Customer')

class update_order(FlaskForm):
    item= StringField('item')
    quantity= IntgerField('quantity')
    price= IntegerField('price')
    submit = SubmitField('Update Order')