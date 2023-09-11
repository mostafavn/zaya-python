

``pythonhost`` is a toolbox for the https://pythonhost.ir community.


Install
-------

    pip3 install pythonhost


Usage
-------------

import pythonhost

    import pythonhost as ph


connect to ftp server
    ph.connect(USER='pythonho', PASS='@UNknown13#',PATH='')



upload file

    ph.upload('manage.py')
    # or
    ph.upload('*')
    

download file

    ph.download('manage.py')
    # or
    ph.download('*')
    

View existing files

    ph.ls()
    

print working directory

    ph.pwd()


get Information from pythonhost
-------

> ph.__author__

> ph.__website__

> ph.__version__