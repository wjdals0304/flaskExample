from flask import Flask,request
from flask_restful import Resource,Api,reqparse,fields,marshal_with

app = Flask(__name__)
api = Api(app)

resource_fields = {
    'task' : fields.String,
    'uri' : fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self,todo_id,task):
        self.todo_id = todo_id
        self.task = task

        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self,**kwargs):
        return TodoDao(todo_id='my_todo',task='remember the milk')


api.add_resource(Todo)


if __name__ == '__main__':
    app.run(debug = True)

