
import os

os.system("ls")

# USING SUBPROCESS
'''
subprocess.run(
    args,
    *, 
    stdin=None, 
    input=None, 
    stdout=None, 
    stderr=None, 
    capture_output=False, 
    shell=False, 
    cwd=None, 
    timeout=None, 
    check=False, 
    encoding=None, 
    errors=None, 
    text=None, 
    env=None, 
    universal_newlines=None
)'''

import subprocess
subprocess.run(['ls'])

subprocess.run(["ls","-l"])


# retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# retrieving information about disk
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])