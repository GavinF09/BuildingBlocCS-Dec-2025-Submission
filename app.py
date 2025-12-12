from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('working.html')

@app.route("/<path:path>")
def returnStatic(path):
    return app.send_static_file(path)

@app.route('/tips')
def getTips():
    # load tips file into array, each line is an element
    with open('tips.txt', 'r') as file:
        tips = file.readlines()
    # insert the tip into template and return the page
    return render_template('tips.html', tip=tips[random.randint(0, len(tips)-1)])


if __name__ == '__main__':
   app.run()