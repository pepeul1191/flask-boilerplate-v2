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

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Arrancer aplicación con servidor GreenUnicorn:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    # Sin logs ni reload
    $ gunicorn app:app -w 6 -b 0.0.0.0:3000
    # Con logs y reload
    $ gunicorn app:app -w 6 -b 0.0.0.0:3000 --reload --access-logfile -

Migraciones con DBMATE - ubicaciones:

    $ dbmate -d "ubicaciones/migrations" -e "DATABASE_UBICACIONES" new <<nombre_de_migracion>>
    $ dbmate -d "ubicaciones/migrations" -e "DATABASE_UBICACIONES" up

Migraciones con DBMATE - accesos:

    $ dbmate -d "accesos/migrations" -e "DATABASE_ACCESOS" new <<nombre_de_migracion>>
    $ dbmate -d "accesos/migrations" -e "DATABASE_ACCESOS" up

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
+ https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
