from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Complete Backend API",
        "description": "Build a REST API using Flask"
    },
    {
        "id": 2,
        "title": "Test API with Postman",
        "description": "Test GET, POST and DELETE endpoints"
    },
    {
        "id": 3,
        "title": "Prepare API Documentation",
        "description": "Create README documentation for the backend API"
    }
]

next_id = 4


@app.route("/")
def home():
    return jsonify({
        "message": "Task Management REST API is running",
        "version": "1.0"
    })


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "success": True,
        "count": len(tasks),
        "tasks": tasks
    })


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    return jsonify({
        "success": True,
        "task": task
    })


@app.route("/api/tasks", methods=["POST"])
def add_task():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required"
        }), 400

    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({
            "success": False,
            "message": "Task title is required"
        }), 400

    task = {
        "id": next_id,
        "title": title,
        "description": description
    }

    tasks.append(task)
    next_id += 1

    return jsonify({
        "success": True,
        "message": "Task added successfully",
        "task": task
    }), 201


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    tasks.remove(task)

    return jsonify({
        "success": True,
        "message": "Task deleted successfully",
        "deleted_task_id": task_id
    })


if __name__ == "__main__":
    app.run(debug=True)