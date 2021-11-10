import zipfile
from imap_tools import MailBox
import io


class InMemoryZip(object):
    def __init__(self):
        # Create the in-memory file-like object for working w/imz
        self.in_memory_zip = io.StringIO()

    # Just zip it, zip it
    def append(self, filename_in_zip, file_contents):
        # Appends a file with name filename_in_zip and contents of
        # file_contents to the in-memory zip.
        # Get a handle to the in-memory zip in append mode
        zf = zipfile.ZipFile(self.in_memory_zip, "a", zipfile.ZIP_DEFLATED, False)

        # Write the file to the in-memory zip
        zf.writestr(filename_in_zip, file_contents)

        # Mark the files as having been created on Windows so that
        # Unix permissions are not inferred as 0000
        for zfile in zf.filelist:
            zfile.create_system = 0

        return self

    def read(self):
        # Returns a string with the contents of the in-memory zip.
        self.in_memory_zip.seek(0)
        return self.in_memory_zip.read()

    # Zip it, zip it, zip it
    def writetofile(self, filename):
        # Writes the in-memory zip to a file.
        f = self.file(filename, "wb")
        f.write(self.read())
        f.close()


if __name__ == "__main__":
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
                # print(att.filename)
                #  verificando se é um arquivo zip
                if att.filename[-3::] == 'zip':
                    imz = InMemoryZip()
                    imz.append()
                    imz.writetofile(att.filename)
                    print(imz)
                    # imz.append("testfile.txt", "Make a test").append("testfile2.txt", "And another one")
                    # imz.writetofile("testfile.zip")
                    #  passando o caminho
                    # filepath = extract_zip(att.filename)
                    # extract_zip(att.filename)
                    # filepath =
                    # download_extract_zip(att.filename)
                    continue
                    if (os.path.exists(filepath)):
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
                                        # extra.extract(extract_zip)
                                        ZipFile.read(extract_zip)

    # Run a test
    # imz = InMemoryZip()
    # imz.append("testfile.txt", "Make a test").append("testfile2.txt", "And another one")
    # imz.writetofile("testfile.zip")