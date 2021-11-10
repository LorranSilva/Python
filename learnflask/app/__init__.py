'''
A Logica da aplicação é salva dentro da controller
Comandos
db init - inicializa as migrações
db migrate - pega o que esta no banco de dados e compara com o que já existe
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)  # db é o nome padrao da classe, auqi esta recebendo a instancia do flask
migrate = Migrate(app, db)  #  O migrate vai cuidar das migrações, por isso recebe a aplicação e o banco de dados

manager = Manager(app)  #  Manager vai ser o controle de comandos que vão inicializar a aplicação
manager.add_command('db', MigrateCommand)

from app.controllers import default