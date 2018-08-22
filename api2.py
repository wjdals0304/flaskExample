from flask import Flask
from flask_restful import Api,reqparse,Resource,marshal_with,fields

fields = {
    'name':fields.String,
    'uri' : fields.Url('todo_resource',absolute=True),
    'https_uri': fields.Url('todo_resource',absolute=True,scheme='https')
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

api.add_resource(Todo,'/todo',endpoint='todo_resource')

if __name__ == "__main__":
    app.run(debug=True)


