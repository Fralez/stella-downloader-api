from flask import request
from flask_restplus import Resource, Namespace

from ..service.download_service import download

api = Namespace('download', description='Download related operations')

# FORMAT SAMPLE: http://127.0.0.1:5000/download?ytUrl=${data}&songTitle=${data}&artist=${data}&album=${data}&imgUrl=${data}
@api.route('/')
@api.param('?imgUrl', 'Cover image URL.')
@api.param('?album', 'Song album.')
@api.param('?artist', 'Song artist.')
@api.param('?songTitle', 'Song title.')
@api.param('?ytUrl', 'Youtube video URL.')
@api.response(200, 'Song downloaded successfully.')
@api.response(500, 'Error when downloading a song.')
class Download(Resource):
	@api.doc('Download a song in mp3 format from a Youtube link.')
	def get(self):
		"""download a song given its data (ytUrl, songTitle, artist, album and imgUrl,)"""
		data = {
			'url': request.args.get('ytUrl'),
			'title': request.args.get('songTitle'),
			'artist': request.args.get('artist'),
			'album': request.args.get('album'),
			'img': request.args.get('imgUrl')
		}
		response = download(data)
		if response['status'] is 'fail':
			api.abort(404)
		else:
			return response