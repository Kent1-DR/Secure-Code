from flask import Flask, Response, render_template, url_for, request
import datetime
import time

app = Flask(__name__)


@app.route("/settime")
def settime():
    return "lel"


@app.route("/")
def index():
        return render_template('index.html', utc_dt=datetime.datetime.now().strftime("%H:%M:%S"), utc_dm=datetime.datetime.today().strftime("%d-%m-%Y"))


@app.route("/format",methods = ['POST'])
def formatD():
    if request.method == 'POST':
        if request.form.get('action1') == '$JMY':
            return datetime.datetime.today().strftime("%d-%m-%Y")
        elif  request.form.get('action1') == '$MJY':
            return datetime.datetime.today().strftime("%m-%d-%Y")
        elif request.form.get('action1') == '$HMS':
            return datetime.datetime.today().strftime("%H-%M-%S")
        elif  request.form.get('action1') == '$MS':
            return datetime.datetime.today().strftime("%M-%S")
        elif  request.form.get('action1') == '$HM':
            return datetime.datetime.today().strftime("%H-%M")
        else:
            return "You don't listen to me so .... error ;("    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



