from project.server.auth.views import auth_blueprint
from project.server import app

app.register_blueprint(auth_blueprint)