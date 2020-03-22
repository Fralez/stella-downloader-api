from flask_restplus import Api
from flask import Blueprint

from .main.controller.download_controller import api as download_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='STELLA DOWNLOADER API',
          version='1.0',
          description='Flask RESTplus API for downloading and converting Youtube videos to mp3.'
          )

api.add_namespace(download_ns, path='/download')