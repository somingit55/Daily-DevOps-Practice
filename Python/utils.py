import os  #importing a new library into code

#print(os.system('systeminfo')) #Linux or Mac exit status 0 with successfull 

os.system('systeminfo')  # Windows System info
os.system('wmic') #Windows Management Instrumentation Command-line
os.system('tasklist')  # for task
os.system('wmic cpu get loadpercentage') #CPU Check
os.system('powershell -Command "Get-PSDrive C"') #for Drive