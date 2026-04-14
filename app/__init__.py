from pathlib import Path # pour gerer les chemins de fichiers dans l'application

from flask import Flask # framework web pour créer l'application

from config import Config # importation de la configuration de l'application

from .routes.api import api_blueprint # routes de l'api
from .routes.web import web_blueprint # routes web

# configuartion des chemins 
BASE_DIR = Path(__file__).resolve().parent.parent # être à la racine du projet

# dossier pour les templates html et les fichiers statiques (css, js, images)
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

#factory pattern 
def create_app() -> Flask:
    # Crée l'instance flask avec les emplacements des templates et des fichiers statics
    app = Flask (
        __name__,
        template_folder=str(TEMPLATES_DIR),
        static_folder=str(STATIC_DIR)
    )
    
    # charger la config depuis config.py
    app.config.from_object(Config)
    
    # on enregistre les routes webs 
    app.register_blueprint(web_blueprint)
    
    # on enregistre les routes api
    app.register_blueprint(api_blueprint)
    
    # retourne l'application configurée
    return app