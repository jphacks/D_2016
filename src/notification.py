import os


def notify():
    path = "notification.ps1"

    os.system('powershell -Command' + ' ' +
              'powershell -ExecutionPolicy RemoteSigned .\\'+path)


if __name__ == "__main__":
    notify()
