import os                      #importing os library
import datetime                #module

def run_command(command):      #define kiya 
    return os.system(command)

def show_date():
    return datetime.datetime.today()

today = show_date()   #call a function
print(today)
