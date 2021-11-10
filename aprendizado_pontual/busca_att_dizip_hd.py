from imap_tools import MailBox
import os.path
from zipfile import ZipFile

#  parametros de login
email = 'caiolymtech@hotmail.com'
password = 'lymt9102'
imap = 'outlook.office365.com'

#  logando
with MailBox(imap).login(email, password) as mailbox:
    #  verificando mensagens
    for msg in list(mailbox.fetch()):
        #  verificando anexos
        for att in msg.attachments:
            print(f'Nome: {att.filename} Tipo: {att.content_type}')
            #  verificando se é um arquivo zip
            if att.filename[-4::] == '.zip' and att.content_type == 'application/x-zip-compressed' or att.filename[-3::] == '.gz':
                #  passando o caminho
                filepath = os.path.join('C:\\', att.filename)
                if(os.path.exists(filepath)):
                    print('Arquivo já existe!')
                else:
                    print(att.filename, att.content_type)
                    with open(filepath, 'wb') as f:
                        f.write(att.payload)
                        print('Saved attachment to:', filepath)
                        file_ext = att.filename
                        with ZipFile(filepath, "r") as extra:
                            extra.printdir()  # mostra informações do arquivo
                            list_zip = extra.namelist()
                            for file_to_ext in list_zip:
                                if file_to_ext.endswith('.xml') or file_to_ext.endswith('.pdf'):
                                    extra.extract(file_to_ext, 'C:\\')