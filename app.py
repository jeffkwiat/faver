from flask import Flask, render_template
from flask_migrate import Migrate

from models import db

# Blueprints
from api.api import api
from auth.auth import auth

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(auth)

# load config from the config file we created earlier
app.config.from_object('config')

# initialize and create the database
db.init_app(app)
db.create_all(app=app)

migrate = Migrate(app, db, render_as_batch=True)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

if __name__ == '__main__':
    app.run()