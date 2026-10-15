import subprocess

# Windows System info
subprocess.run(["systeminfo"])

# Windows Management Instrumentation Command-line
subprocess.run(["wmic"])

# Task list
subprocess.run(["tasklist"])

# CPU load percentage
subprocess.run(["wmic", "cpu", "get", "loadpercentage"])

# C Drive information
subprocess.run(["powershell", "-Command", "Get-PSDrive C"])