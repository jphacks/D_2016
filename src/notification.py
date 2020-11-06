import os
import time

import activity_log

def generate_path(event) -> str:
    path = ""
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
    
    if txt == "":
        return
    
    os.system('powershell -Command' + ' ' +
              'powershell -ExecutionPolicy RemoteSigned .\\' + path + " " + str(txt) +" "+ img_path)

def need_to_notify(s_num,f_num):
    """通知を送る条件を満たす場合True、ほかはFalse
    """
    # TODO: 通知が必要な条件を記入
    previous_saved_time = activity_log.get_previous_saved_time()
    dt = time.time() - previous_saved_time
    if s_num == -1:
        return False
    elif dt < 20:
        return False
    elif int(f_num) - int(s_num) > 100:
        return True
    elif int(f_num) - int(s_num) <= 100 and int(f_num) - int(s_num) > 0:
        return False
    else:
        return False
        
if __name__ == "__main__":
    notify("こんにちは","startup_300px.gif")
