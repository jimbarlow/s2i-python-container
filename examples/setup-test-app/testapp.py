import sys, os
from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class Greeting (Resource):
    def get(self):
        return 'Hello World from a generic Universal Base Image optimized for RHEL! try hitting this resource at /python_version'

class PythonVersion (Resource):
    def get(self):
        return (sys.version)

api.add_resource(Greeting, '/')
api.add_resource(PythonVersion, '/python_version')

if __name__ == '__main__':
    application.run('0.0.0.0','8080')
