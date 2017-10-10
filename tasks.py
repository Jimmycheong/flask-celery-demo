from celery import Celery

app = Celery('tasks', broker="redis://localhost:6379", backend="redis://localhost:6379/4")

@app.task()
def print_hello():
    return "Completed task!"


if __name__ == '__main__':
    print("Running script")
    r = print_hello.delay()

    print(r.get())
