from flask_restful import Api, Resource
from app.blueprints import clickatell_gateway

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'clickatell'}


click_api = Api(clickatell_gateway)
click_api.add_resource(HelloWorld, '/')
