from urllib import response
from flask import Flask, Response, render_template, url_for, request, abort
import datetime
import time
import win32api
import ctypes, os, sys
from flask_talisman import Talisman


app = Flask(__name__)

#app.config.from_file('config.py', load=True)
#app.config.from_object(__name__)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)


#error handlings
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500



#app to set the time only with admin rights
@app.route("/setdate",methods = ['POST'])
def setdate():
        lol = request.form.get('actiontest')
        #talisman = Talisman(app, content_security_policy=None)
        date = datetime.datetime.fromisoformat(lol)
        win32api.SetSystemTime(date.year,date.month,date.weekday(),date.day,date.hour,date.minute,date.second,date.microsecond)
        return "the time of your PC has been set at :" + str(date)


#default page
@app.route("/")
def index():
        #csp = {
        #'default-src': '\'self\'',
    #'img-src': '*',
    #'media-src': [
     #   '*'
    #],
    #'script-src': '*'
#}

        #talisman = Talisman(app, content_security_policy=csp)
        return render_template('index.html', utc_dt=datetime.datetime.now().strftime("%H:%M:%S"), utc_dm=datetime.datetime.today().strftime("%d-%m-%Y"))  
        
            



#app to select format
@app.route("/getformat",methods = ['POST'])
def formatD():
        lel = request.form.get('action1')
        #talisman = Talisman(app, content_security_policy=None)
        return "This is the result of what you have type :" + datetime.datetime.now().strftime(lel)



#error redirection
@app.route('/404')
def error404():
    abort(404)



@app.route('/500')
def error500():
    abort(500)
