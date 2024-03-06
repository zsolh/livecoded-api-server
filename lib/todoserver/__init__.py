from flask import Flask, make_response, request
import json

app = Flask(__name__)

MEMORY = {}

@app.route("/tasks/", methods=["GET"])
def get_all_tasks():
    tasks = [ {"id": task_id, "summary": task["summary"]}
             for task_id, task in MEMORY.items()]

    return make_response(json.dumps(tasks), 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    payload = request.get_json(force = True)
    try:
        task_id = 1 + max(MEMORY.keys())
    except ValueError:
        task_id = 1
        
    MEMORY[task_id] = {
            "summary" : payload["summary"],
            "description":payload["description"],
            }
    data = {"id" : task_id}
    return make_response(json.dumps(data), 201)

@app.route("/tasks/<int:task_id>/")
def task_details(task_id):
    task_info = MEMORY[task_id].copy()
    task_info["id"] = task_id
    return json.dumps(task_info)



