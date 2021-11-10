import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

"""
Este script e responsavel por ler o nome de pastas e arquivos de um path, e salvar um arquivo .txt
com o nome dos itens, depois manda a lista para seu email. Assim caso os perca, sabera o nome dos
itens caso nao lembre o que deseja recuperar.

This script is responsable by read the name of directorys and files of a path and save a .txt file
with the name of itens, after send an email to You. ...lost, You know the name of itens case You
wish to backup them.
"""


def send_email(target_email=None):
    config = {
        "EMAIL_SMTP": '',
        "EMAIL_RECEIVER": '',
        "SMTP": 'outlook.office365.com',
        "SMTP_PORT": 587,
        "PASSWORD_SMTP": ''
    }

    filename = "files-list.txt"
    titulo = 'L para A'
    message = 'teste divertido'
    msg = MIMEMultipart()
    msg['From'] = config['EMAIL_SMTP']
    msg['To'] = config['EMAIL_RECEIVER']
    msg['Subject'] = titulo
    msg.attach(MIMEText(message, 'plain'))
    attachment = open(filename, "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    try:
        server = smtplib.SMTP(config['SMTP'], config['SMTP_PORT'])
        server.starttls()
        server.login(msg['From'], config['PASSWORD_SMTP'])
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        print("Erro ao enviar Email. Verifique as informações cadastradas ou veja as configurações de seu email.")

# passar o nome do diretorio que deseja escanear // send the directory name that You wish to scan
# dir = input('Name of directory to scan:\n')
dir = 'C:\\'

# organizar itens em um dict
organizador = {'pastas': dict()}

# lista de pastas // directory lists
for pasta in os.walk(dir):
    # cada nome de pasta vira uma chave de pastas e recebem uma tupla com o nome de seus arquivos
    organizador["pastas"][f'{pasta[0]}'] = pasta[2:]

# trabalhando com a chave 'pastas'
files = organizador.get('pastas')

f = open("files-list.txt", "w+", encoding="utf-8")
for i in files.values():
    n = i[0]
    for name in n:
        print(name)
        f.write(f'{name}\n')
f.close()

# enviar por email TODO
a = send_email()