from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config

from routes.auth_routes import auth_bp
from routes.train_routes import train_bp
from routes.booking_routes import booking_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(train_bp, url_prefix="/train")
app.register_blueprint(booking_bp, url_prefix="/booking")
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)
