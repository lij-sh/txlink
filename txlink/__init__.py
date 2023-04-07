import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'txdb.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)
    db.modif_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import cust
    app.register_blueprint(cust.bp)
    app.add_url_rule('/', endpoint='index')

    from . import prod
    app.register_blueprint(prod.bp)


    return app
