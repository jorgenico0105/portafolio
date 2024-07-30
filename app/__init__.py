from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY')
    )

    # Importación y registro del Blueprint e importa la aplicaicon de portfolio 
    from . import portfolio
    app.register_blueprint(portfolio.bp)

    return app
