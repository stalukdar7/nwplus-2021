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
    lon = request.form["longtitude"]
    eventId = request.form["eventId"] 
    rad = request.form["radius"]
    start = request.form["start"]
    end = request.form["end"]
    answer = func(lat, lon, eventId, rad, start, end) 
    return render_template('answer.html', answer=answer)


if __name__ == '__main__':
    app.run()
