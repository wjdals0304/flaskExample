from flask import Flask
from flask_restful import Api,reqparse,Resource,marshal_with,fields

class AllCapsString(fields.Raw):
    def format(self, value):
        return value.upper()

fields = {
    'name':fields.String,
    'all_caps_name' : AllCapsString(attribute='name'),
}

app=Flask(__name__)
api = Api(app)

class todoObject():
    def __init__(self,name):
        self.name=name

def get_todo():
    return todoObject("kikm")

class Todo(Resource):
    @marshal_with(fields)
    def get(self, **kwargs):
        return get_todo()

api.add_resource(Todo,'/todo')

if __name__ == "__main__":
    app.run(debug=True)


