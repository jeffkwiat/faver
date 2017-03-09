from flask import Flask, render_template
from flask_migrate import Migrate

from models import db

# Blueprints
from api.api import api
from auth.auth import auth

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(api)
app.register_blueprint(auth)

app.config.from_object('config')

# initialize and create the database
db.init_app(app)
db.create_all(app=app)

# migrate database, if necessary
migrate = Migrate(app, db, render_as_batch=True)

@app.route('/')
def home():
    '''
    Router for the index URL.
    :return:
    '''
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    '''
    Router for the favorites URL.
    :return:
    '''
    return render_template('favorites.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
