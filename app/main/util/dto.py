from flask_restplus import Namespace, fields


class downloadDto:
    api = Namespace('download', description='download related operations')