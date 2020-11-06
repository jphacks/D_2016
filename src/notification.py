import os
import time

def generate_path(event) -> str:
    
    if event == "start":
        path = "startup_300px.gif"
    
    if event == "terminate":
        path = "ending_ver2_300px.gif"
    
    if event == "cheer":
        path = "breaktime_ver2_300px.gif"
    
    if event == "praise":
        path = "mirai.gif"
    
    if event == None:
        path = "mirai.gif"
    
    return path


def notify(txt,img_path):
    path = "notification.ps1"
    
    os.system('powershell -Command' + ' ' +
              'powershell -ExecutionPolicy RemoteSigned .\\' + path + " " + str(txt) +" "+ img_path)


def need_to_notify() -> bool:
    """通知を送る条件を満たす場合True、ほかはFalse
    """
    # TODO: 通知が必要な条件を記入
    return False


if __name__ == "__main__":
    notify("こんにちは","startup_300px.gif")
