'''
Virtual Environment is a mini python software loaded inside a python file 
which is totally new and has no third-party modules installed.
It is used to run multiple versions of python in a single python file.
'''

import flask
import pandas as pd
import pygame

'''
To create a virtual environment type virtualenv 'filename' in console.
Next to activate the virtual environment :
For Linux Users : source project1/bin/activate
For Windows Powershell Users : .\project1\Scripts\activate.ps1
'''

'''
If Error displays while activating the virtual environment :
https://stackoverflow.com/questions/67150436/cannot-be-loaded-because-running-scripts-is-disabled-on-this-system-for-more-in 
Run "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted" on Powershell as Administrator.
If problem arises as 'running scripts is disabled on the system'.
'''

'''
We can install and activate any module of our choice in the virtual environment and 
work with it separately without interfering with base version of python.
We can get out of the virtual environment by running 'deactivate' command and return to base version.
For max efficiency please use different terminals for base version and virtual
'''

'''
We can get the modules installed in a version of python using 'pip freeze' command.
We can even make a file containing the installed modules in that version by running 'pip freeze > "filename.txt"' command.
We can install those modules into another version of python by importing the file by running 'pip install -r "filename.txt"' command.
'''