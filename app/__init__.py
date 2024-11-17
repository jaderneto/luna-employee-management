from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.auth.routes import bp as auth_bp
from app.employees.routes import bp as employees_bp
from app.relationship.routes import bp as relationship_bp
from app.teams.routes import bp as teams_bp
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Getting the configurations from config.py
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)

    # Import the models
    from app.employees.models import Employees
    from app.auth.models import User
    from app.organization.models import Organization
    from app.assignment.models import Assignment
    from app.relationship.models import WorkRelationship
    from app.teams.models import Teams

    # Registre os Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(employees_bp, url_prefix='/employees')
    app.register_blueprint(relationship_bp, url_prefix='/relationship')
    app.register_blueprint(teams_bp, url_prefix='/teams')

    return app
