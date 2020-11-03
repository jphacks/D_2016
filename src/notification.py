import os

path = "notification.ps1"

os.system('powershell -Command' + ' ' +\
          'powershell -ExecutionPolicy RemoteSigned .\\'+path)