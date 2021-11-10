from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# from validate_email import validate_email
# is_valid = validate_email('cricciardi@lymtechbr', check_mx=True)

# print(is_valid)
#
# dicio = {
#     'a': 'abelha',
#     'b': 'balde'
# }
# l = list()
# count = 0
# try:
#     x = dicio.keys()
#     for y in x:
#         l.append(y)
#         l[count].replace("'",'')
#         print(l[count])
#         count += 1
# except:
#     print('excessao')

def send_msg(message):
    config = {
        "EMAIL_SMTP": "lym_func_teste@outlook.com",
        "EMAIL_RECEIVER": "js2844419@gmail.com",
        "SMTP": "outlook.office365.com",
        "SMTP_PORT": 587,
        "PASSWORD_SMTP": "lymt9102"
    }

    msg = MIMEMultipart()
    msg['From'] = config['EMAIL_SMTP']
    msg['To'] = config['EMAIL_RECEIVER']
    msg['Subject'] = message # titulo
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP(config['SMTP'], config['SMTP_PORT'])
    server.starttls()
    server.login(msg['From'], config['PASSWORD_SMTP'])
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


mensagem = 'mensagem teste'
send_msg(mensagem)
print('Email enviado')

# def enviar_email(msg, email_para_enviar=None):
#     retemente = False
#     if email_para_enviar:
#         remetente = email_para_enviar
#     else:
#         remetente = self.env[''].search([()])