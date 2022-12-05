from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'we9pphofljnksdf;fq9ryu39[p3h5blk3nmbxf[249qht4p'

    return app