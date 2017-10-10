from flask import Flask, request, url_for, redirect, make_response,render_template
from tasks import print_hello

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def call_celery_task():
    if request.method == "POST":
        r = print_hello.delay()
        print(r.get())
        print("End of main.py")
        resp = make_response(render_template('index.html'), 200)
        resp.headers['X-Something'] = 'A value'
        return resp
    else: 
        return "Welcome to Celery"
