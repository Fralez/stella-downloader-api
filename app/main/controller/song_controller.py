from flask import request, send_file
from flask_restplus import Resource, Namespace

from ..service.song_service import download, extract

api = Namespace('song', description='Song related operations')

@api.route('/download')
@api.param('imgUrl', 'Cover image URL (.jpeg, .png, .gif or .bmp files).')
@api.param('album', 'Song album.')
@api.param('artist', 'Song artist.')
@api.param('songTitle', 'Song title.')
@api.param('ytUrl', 'Youtube video URL.')
@api.response(200, 'Song downloaded successfully.')
@api.response(400, 'Bad Youtube URL.')
@api.response(404, 'Youtube (Media) URL is missing.')
@api.response(415, 'Cover image URL extension is unsupported.')
class Download(Resource):
	@api.doc("Download a song in mp3 format from a Youtube link.")
	def get(self):
		"""download a song given its data (Youtube link, title, artist, album and cover art link,)"""
		data = {
			'url': request.args.get('ytUrl'),
			'title': request.args.get('songTitle'),
			'artist': request.args.get('artist'),
			'album': request.args.get('album'),
			'img': request.args.get('imgUrl')
		}
		response = download(data)
		if response[0].get('status') == 'fail':
			return response[0], response[1]
		
		return send_file(response[0].get('songpath'), as_attachment=True)


@api.route('/info')
@api.param('ytUrl', 'Youtube video URL.')
@api.response(200, 'Song info extracted successfully.')
@api.response(400, 'Bad Youtube URL.')
@api.response(404, 'Youtube (Media) URL is missing.')
class SongInfo(Resource):
	@api.doc("Extract a song's information given its Youtube link.")
	def get(self):
		"""Extract a song's information given its Youtube link"""
		url = request.args.get('ytUrl')
		response = extract(url)
		return response[0], response[1]