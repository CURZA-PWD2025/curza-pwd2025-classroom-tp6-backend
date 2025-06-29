from flask import Flask
from flask_cors import CORS

from app.modules.articulo.articulo_routes import articulo_bp
from app.modules.categoria.categoria_routes import categoria_bp
from app.modules.marca.marca_routes import marca_bp
from app.modules.proveedor.proveedor_routes import proveedor_bp

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    app.register_blueprint(articulo_bp, url_prefix="/articulos")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")

    @app.route("/")
    def home():
        return "<h1>Trabajo Práctico n° 7</h1>"

    return app
