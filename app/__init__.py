from flask import Flask
from flask_restful import Api

from app.config import configurations
from app.api.api import NumberForms


def create_app(config_name):
  """create app factory defines app settings"""

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(configurations[config_name])

  # define API
  api = Api(app)
  api.add_resource(NumberForms, "/api/v1/number-forms")

  return app