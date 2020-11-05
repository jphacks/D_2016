import os
import time


def notify(txt):
    path = "notification.ps1"
    os.system('powershell -Command' + ' ' +
              'powershell -ExecutionPolicy RemoteSigned .\\' + path + " " + str(txt))


def need_to_notify() -> bool:
    """通知を送る条件を満たす場合True、ほかはFalse
    """
    # TODO: 通知が必要な条件を記入
    return False


if __name__ == "__main__":
    notify("こんにちは")
