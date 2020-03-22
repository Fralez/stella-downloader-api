from flask import request
from flask_restplus import Resource

from ..util.dto import downloadDto
from ..service.download_service import download

# @api.route('/download')
# @api.response(200, 'Song downloaded successfully.')
# @api.response(500, 'Error when downloading.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user