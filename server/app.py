from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__) 
app.config['MONGO_URI'] = 'mongodb://admin:admin123@db:27017/workshopdb'
mongo = PyMongo(app)

@app.route('/') 
def hello(): 
    return "Welcome"

@app.route('/api/todos', methods=['GET']) 
def getTodos(): 
    todos = mongo.db.todos
    # if request.method == 'POST':
    #     print("again")
    #     todoName = request.json.get('todo')
    #     todo_id = todos.insert({'title': todoName})
    #     # res = "added" + todoName
    #     res = {'status': 'created', 'id': str(todo_id)}
    #     return jsonify(res)
    # else:
        # todos = [
        #     {
        #         'title': 'eat properly',
        #         'completed': False
        #     },
        #     {
        #         'title': 'wake up early',
        #         'completed': False
        #     }
        # ]        
    output = []
    for item in todos.find():
        output.append({'title': item['title']})
    return jsonify(output)

@app.route('/api/todos', methods=['POST'])
def addTodo():
    todos = mongo.db.todos
    todoName = request.json.get('todo')
    todo_id = todos.insert({'title': todoName})
    # res = "added" + todoName
    res = {'status': 'created', 'id': str(todo_id)}
    return jsonify(res)
  
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)  
