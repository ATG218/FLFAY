from website import create_app
from flask import Flask
from waitress import serve

app = create_app()

if __name__ == '__main__':
    app.run(host ='0.0.0.0')
    serve(app,host='0.0.0.0', port=5000, url_scheme='https')