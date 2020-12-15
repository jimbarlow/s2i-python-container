import sys
import os
from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class Greeting (Resource):
    def get(self):
        return 'Hello Another World from a generic Universal Base Image optimized for RHEL! try hitting this resource at /python_version'

class PythonVersion (Resource):
    def get(self):
        return (sys.version)

class ListFiles (Resource):
    def get(self):
        file_list = os.listdir( '/datafiles' )
        listToStr = ' '.join(map(str, file_list))
        return listToStr

api.add_resource(Greeting, '/')
api.add_resource(PythonVersion, '/python_version')
api.add_resource(ListFiles, '/data_files')

if __name__ == '__main__':
    application.run('0.0.0.0','8080')
