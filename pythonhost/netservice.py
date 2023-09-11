import ftplib, os

def connect(USER, PASS, PATH):
    global ftp
    ftp = ftplib('pouya.7ho.st')
    ftp.login(USER, PASS)
    ftp.encoding = 'utf-8'

    if PATH != '':
        ftp.cwd(PATH)

def ls():
    return ftp.dir()

def pwd():
    return ftp.pwd()

def upload(filename):
    if filename == '*':
        for fname in os.listdir():
            ftp.storbinary(f'STOR {fname}', open(fname, 'rb'))
    else:
        ftp.storbinary(f'STOR {filename}', open(filename, 'rb'))
    ftp.quit()

def download(filename):
    if filename == '*':
        for fname in ftp.nlst():
            ftp.retrbinary(f'RETR {fname}', open(fname, 'wb').write)
    else:
        ftp.retrbinary(f'RETR {fname}', open(fname, 'wb').write)
    ftp.quit()
