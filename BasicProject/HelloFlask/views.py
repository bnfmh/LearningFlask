from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    #1
    #html_content = "<html><head><title>Hello Flask</title></head><body>"
    #html_content += "<strong>Hello Flask!</strong> on " + formatted_now
    #html_content += "</body></html>"
    #return html_content

    #2
    #return render_template("index.html",content = "<strong>Hello, Flask!</strong> on " + formatted_now)

    #3
    return render_template("index.html",
                           content = " on " + formatted_now,
                           message = "hello , flask",
                           title = "Hello Flask")

@app.route('/api/data/')
def get_data():
    return app.send_static_file('scripts/data.json')

@app.route('/about')
def about():
    return render_template("about.html", 
                           title = 'About Hello Flask',
                           content = 'Example app page for hello flask')