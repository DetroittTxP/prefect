from flask import Flask, jsonify, request
from flowtask.task_1 import task_1, task_1_flow
from flowtask.task_2 import task_2_process_data, task_2_save_data
app = Flask(__name__)

# Flask routes


@app.get("/task_1")
def task_1_api():

    task_1_flow()
    return jsonify({"status": f"Task 1 is running:  "})


@app.post("/task_2")
def task_2_api():
    data = request.json

    task_2_process_data.delay(data)
    task_2_save_data.delay(data)

    return jsonify({"status": "Task 2 is running", "data": data})


if __name__ == "__main__":
    app.run(debug=True)
