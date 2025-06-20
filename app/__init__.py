
from flask import Flask
from app.modules.categoria.categoria_routes import categoria_bp
from app.modules.marca.marca_routes import marca_bp
from app.modules.proveedor.proveedor_routes import proveedor_bp
from app.modules.articulo.articulo_routes import articulo_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")
    app.register_blueprint(articulo_bp, url_prefix="/articulos")

    @app.route("/")
    def home():
        return "<h1>TP 6 funcionando correctamente.</h1>"
    return app