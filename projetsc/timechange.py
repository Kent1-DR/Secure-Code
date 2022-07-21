from datetime import date
import ctypes, sys, os
import win32api


def setTime(year,month,weekday,day,hour,minute,second,microsecond):
        #print ("exeeeeec")
        win32api.SetSystemTime(year,month,weekday,day,hour,minute,second,microsecond)



if __name__ == '__main__':
                setTime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]),int(sys.argv[8]))

