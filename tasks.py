from celery import Celery
import time

app = Celery('tasks', broker="redis://localhost:6379", backend="redis://localhost:6379/4")

@app.task()
def print_hello():
    print("Started task")
    time.sleep(7)
    return "Completed task!"
