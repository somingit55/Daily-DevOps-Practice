import subprocess

def run_com(command):
    return subprocess.run(command)

run_com("ls")
run_com("ps")
run_com("rmdir som")

#def hello():             #define 
 #   print("Hello Som")   #inside
#print("Program start")   #outside
#hello()                  #outside
#print("Program end")     #outside