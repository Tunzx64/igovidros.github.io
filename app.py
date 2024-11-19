from flask import Flask
from routes.home import home
from routes.vidros_comun import edit
from routes.painel_vendas import vendas
from models import db
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home)
app.register_blueprint(edit)
app.register_blueprint(vendas)
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)