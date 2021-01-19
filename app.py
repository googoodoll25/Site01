from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    date = now.strftime('%d/%m/%Y')
    return render_template('Realtime.html', date=date)


@ app.route('/report')
def report():
    return 'Report'


if __name__ == "__main__":
    app.run(debug=True)
