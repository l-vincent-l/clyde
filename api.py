from flask import Flask, request, current_app
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class Pong(restful.Resource):
    def post(self):
       current_app.logger.info("data: {}".format(request.data))
       current_app.logger.info("headers: {}".format(request.headers))
       hail = request.get_json()
       hail['hail']['status'] = 'received_by_taxi'
       return hail

api.add_resource(Pong, '/hail/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
