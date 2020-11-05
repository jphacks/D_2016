import os


def add_to_startup(file_path: str):
    """file_path を、PC立ち上げ時に実行するように設定
    もしファイルパスを指定しなければ、このファイルを登録

    venv=Trueなら仮想環境を立ち上げてから実行
    """
    import getpass

    USER_NAME = getpass.getuser()
    assert os.path.exists(file_path), "指定されたfile_pathがありません: " + file_path
    file_path = os.path.abspath(file_path)  # 絶対パス
    bat_path = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(
        USER_NAME)
    # print(bat_path)
    with open("komati.bat", "w+") as bat_file:
        text = "cd " + os.path.dirname(file_path) + "\n"
        text += 'python {}\n'.format(file_path)
        text += ""
        bat_file.write(text)

    with open(bat_path + '\\' + "komati_no_window.vbs", "w+") as vbs_file:
        text = 'Set ws = CreateObject("Wscript.Shell")' + "\n"
        src_path = os.path.dirname(file_path)
        text += 'ws.run "cmd /c {}/komati.bat", vbhid'.format(src_path) + "\n"
        text += ""
        vbs_file.write(text)
    print(file_path + " をスタートアップに登録しました")


if __name__ == "__main__":
    add_to_startup("main.py")
