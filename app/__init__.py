from flask import Flask
from flask_restful import Api

from app.config import configurations


def create_app(config_name):
  """create app factory defines app settings"""

  # instanciate Flask using configs from the config file
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(configurations[config_name])

  return app