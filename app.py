# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# Inisiasi object flask_restful
api = Api(app)

# Inisiasi object flask_cors
CORS(app)

# inisiasi variabel kosong bertipe dictiniary
identity = {} # variabel global

# Class Resource
class ExampleResource(Resource):
    # metode get dan post
    def get(self):
        # response = {"msg" : "Hello World"}
        return identity
    
    def post(self):
        name = request.form["name"]
        age = request.form["age"]
        identity["name"] = name
        identity["age"] = age
        response = {"msg" : "successfully save data"}
        return response

# setup resourcenya
api.add_resource(ExampleResource, "/api", methods=["GET", "POST"]) 

if __name__=="__main__":
    app.run(debug=True, port=5005) 