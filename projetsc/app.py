from flask import Flask, render_template, request, abort
import datetime
import configparser
import ctypes, sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', utc_dt=datetime.datetime.now().strftime("%H:%M:%S"), utc_dm=datetime.datetime.today().strftime("%d-%m-%Y"))  


#error handlings
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500



#app to set the time only with admin rights
"""
@app.route("/setdate",methods = ['POST'])
def setdate():
        lol = request.form.get('actiontest')
        try:
            date = datetime.datetime.fromisoformat(lol)
            date = setTime(date)
        except:
            return 'You have entered an invalid value.'
            

        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "".join(sys.argv), None, 1)
        return "the time of your PC has been set at :" + str(date)
"""         



#app to select format
@app.route("/getformat",methods = ['POST'])
def formatD():
        lel = request.form.get('action1')
        return "This is the result of what you have type :" + datetime.datetime.now().strftime(lel)



#error redirection
@app.route('/404')
def error404():
    abort(404)



@app.route('/500')
def error500():
    abort(500)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config_file.cfg')
    port = config['FLASK']['Port']
    host = config['FLASK']['Host']
    debu = config['FLASK']['Debug']
    app.run(port=port, host=host, debug=debu)
    