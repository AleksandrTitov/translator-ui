# ui-tanslator
UI service for the [go-translator](https://github.com/taleksandrv/go-translator)

## About

[ui-tanslator](https://github.com/taleksandrv/ui-tanslator) it's a UI for the [go-translator](https://github.com/taleksandrv/go-translator) application.

## Using
### Base

The ui-tranlator application based on [Flask](http://flask.pocoo.org/) framework 
To launch, necessary install all the Python dependency described in the file [requirements]( https://github.com/taleksandrv/ui-tanslator/blob/master/requirements), after lounch Flask application: 

```
pip install --no-cache-dir -r requirements
export FLASK_APP=ui.py
flask run
```

Open the url:

```
http://127.0.0.1:5000/
```
### Using go-translate

By default the [go-translator](https://github.com/taleksandrv/go-translator) application should be run on the same vm-instance and avalible to URL http://localhost:8080, else necessary export an environment variable **TRANSLATE_SRV** contain the go-translate URL, for example:

```
export TRANSLATE_SRV=http://go-translate.tr.srv.local:8080
```

## Docker way

For convenience of running application created Dockerfile, so possible to build and run docker image. 
