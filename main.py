import time
from flask import Flask, request, url_for, redirect, make_response,render_template
from tasks import print_hello

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def call_celery_task():
    if request.method == "POST":
        r = print_hello.delay()
        while r.status == "PENDING":
            print("sleeping...")
            time.sleep(1)

        print("job complete!")
        print(r.get())
        resp = make_response(render_template('index.html'), 200)
        print("End of main.py")
        return resp
    else:
        return "Welcome to Celery"
