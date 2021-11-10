# a variavel app ésta sendo importada do __ini__ dentro de app
from flask import render_template
from app import app


@app.route('/index')
app.route('/')
#  defauls recebe o nome da variavel e o valor padrao
#  @app.route('/', defaults={'user': None})
def index(user):
    return render_template('index.html')
    #  pega o arquivo html e renderiza por string

app.route('/login')
def login():
	return render_template('base.html')
'''
Anotações:

É possível retornar uma string html atraves da rota.

@app.route('/empre', defaults={'name':None})
@app.route('/empre/<empre>')  #  passando pela rota com variavel
def empre(empre):  #   o None é passado caso não seja inserida variavel, pois é padrão receber algo
	if empre:
		return "%s nota 10!" % empre
	else:
		return "Nota 10!"

A mesma coisa que o codigo a cima, mas esta estrutura é menos usual

@app.route('/empre')  #  passando pela rota sem variavel
@app.route('/empre/<empre>')  #  passando pela rota com variavel
def empre(empre=None):  #   o None é passado caso não seja inserida variavel, pois é padrão receber algo
	if empre:
		return "%s nota 10!" % empre
	else:
		return "Nota 10!"


Forçando mudança de tipo no flask <int:idade>
''' 