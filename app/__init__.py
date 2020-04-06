from flask_restplus import Api
from flask import Blueprint

from .main.controller.song_controller import api as song_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='STELLA DOWNLOADER API',
          version='1.0',
          description='Flask RESTplus API for downloading and converting Youtube videos to mp3.'
          )

api.add_namespace(song_ns, path='/song')