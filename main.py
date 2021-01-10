from flask import Flask, request, render_template
from service import func

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    lat = request.form["lattitude"]
    long = request.form["longtitude"]
    event = request.form["event"]
    rad = request.form["radius"]
    time = request.form["time"]
    answer = func(lat, long, event, rad, time) 
    return render_template('answer.html', answer=answer)


if __name__ == '__main__':
    app.run()
