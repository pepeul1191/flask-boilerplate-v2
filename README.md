## Python3 Flask Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar servidor Torando

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Migraciones con DBMATE:

    $ dbmate -d "db/migrations" -e "DATABASE_URL" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" up

### Fuentes

+ https://github.com/pepeul1191/python-gestion
+ https://pypi.python.org/pypi/pysftp
+ http://flask.pocoo.org/docs/0.12/quickstart/
+ http://werkzeug.pocoo.org/docs/0.14/datastructures/#werkzeug.datastructures.FileStorage
+ http://flask.pocoo.org/docs/0.12/templating/

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
