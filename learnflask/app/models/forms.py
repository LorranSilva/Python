from flask_wtf import FlaskForm
from flask import StringField

class LoginForm(FlaskForm):
	#  cada campo deve receber um nome que é primeiro argumento
	username = ""
	password = ""
	remember_me = ""