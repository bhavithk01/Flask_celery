from flask import Flask

from .views import main
from .utils import make_celery

def create_app():
    """Configuring and creating flask app"""
    app = Flask(__name__)
    
    # configuring message broker url
    app.config["CELERY_CONFIG"] = {"broker_url": "amqp://bhavith:1234@localhost:5672"}

    celery = make_celery(app)
    celery.set_default()
    
    app.register_blueprint(main)

    return app, celery