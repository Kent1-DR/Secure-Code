#application who require admin privileges
from flask import Flask, render_template, request, abort
import configparser
import datetime
import win32com.shell.shell as shell
import ctypes, sys, os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index2.html')


@app.route("/setdate",methods = ['POST', 'GET'])
def setTime():
        lol = request.form.get('actiontest')
        try:
            date = datetime.datetime.fromisoformat(lol)
        except:
            return 'You have entered an invalid value, date cant be NULL or out of range(mounth = 30 for example).'
        
        year = date.year
        month = date.month
        weekday = date.weekday()
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second
        microsecond = date.microsecond
        
        #print (str(year) +" "+ str(month) +" "+ str(weekday) +" "+ str(day) +" "+ str(hour) +" "+ str(minute)+" "+ str(second)+" "+ str(microsecond))
        admin(str(year) +" "+ str(month) +" "+ str(weekday) +" "+ str(day) +" "+ str(hour) +" "+ str(minute)+" "+ str(second)+" "+ str(microsecond))
        
        return "the time of your PC has been set at :" + str(date)



def admin(params):
    directory = os.getcwd()
    commands1 = "cd "+directory+ " " + "&&" + "python timechange.py"+ " "+params
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands1)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config_file2.cfg')
    port = config['FLASK']['Port']
    host = config['FLASK']['Host']
    app.run(port=port, host=host)

