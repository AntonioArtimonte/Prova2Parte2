from flask import Flask, render_template
from flask_cors import CORS
from .routes import main as main_bp

def create_app():
    app = Flask(__name__, template_folder='../../frontend/templates')
    app.register_blueprint(main_bp)
    
    CORS(app)
    return app    