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

Arrancar servidor Werkzeug

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Migraciones con DBMATE - ubicaciones:

    $ dbmate -d "ubicaciones/migrations" -e "DATABASE_UBICACIONES" new <<nombre_de_migracion>>
    $ dbmate -d "ubicaciones/migrations" -e "DATABASE_UBICACIONES" up

### Fuentes

+ https://github.com/pepeul1191/python-gestion
+ https://pypi.python.org/pypi/pysftp
+ http://flask.pocoo.org/docs/0.12/quickstart/
+ http://werkzeug.pocoo.org/docs/0.14/datastructures/#werkzeug.datastructures.FileStorage
+ http://flask.pocoo.org/docs/0.12/templating/
+ https://stackoverflow.com/questions/4239825/static-files-in-flask-robot-txt-sitemap-xml-mod-wsgi
+ https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
+ https://stackoverflow.com/questions/29386995/how-to-get-http-headers-in-flask
+ http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
