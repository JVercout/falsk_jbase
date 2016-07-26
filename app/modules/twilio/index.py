from simplexml import dumps
from flask import make_response
from flask_restful import Api, Resource

from app.blueprints import twilio_gateway
from app.tasks.workflow.workflow import add

# class TwilioApi(Api):
#     def error_router(self, original_handler, e):
#         print('error_router called', original_handler, e)
#         # Extension for 404 errors code
#         self.handle_error(e)
#         return super().error_router(original_handler, e)

#     def handle_error(self, e):
#         code = getattr(e, 'code')
#         print('handle_error', e, code)
#         if code == 404:
#             print('4o4 catch')
#             code = 404
#             data = {'error': 'test'}
#         else:
#             return super().handle_error(e)

#         print('make_response')
#         return self.make_response(data, code)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'twilio', 'test': 'is true'}


class Workflows(Resource):
    def get(self):
        async_add = add.delay(1, 1)
        while(not async_add.ready()):
            print('async not ready')
            print(async_add)
        return {}


class Databases(Resource):
    def get(self):

        return {}


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!" + id'}


rest_api = Api(twilio_gateway, default_mediatype='application/xml')
rest_api.add_resource(HelloWorld, '/')
rest_api.add_resource(TodoItem, '/todos/<int:id>')
rest_api.add_resource(Workflows, '/w')
rest_api.add_resource(Databases, '/d')


@rest_api.representation('application/xml')
def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response': data}), code)
    resp.headers.extend(headers or {})
    return resp
