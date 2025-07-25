from flask import Flask
from app.routes.file_routes import file_bp
import os

def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max size

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.register_blueprint(file_bp, url_prefix='/files')
    return app
