import os


def add_to_startup(file_path: str):
    """file_path を、PC立ち上げ時に実行するように設定
    もしファイルパスを指定しなければ、このファイルを登録

    # TODO: venv=Trueなら仮想環境を立ち上げてから実行
    """
    import getpass

    USER_NAME = getpass.getuser()
    assert os.path.exists(file_path), "指定されたfile_pathがありません: " + file_path
    abs_file_path = os.path.abspath(file_path)  # 絶対パス
    bat_path = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(
        USER_NAME)
    # print(bat_path)

    # スタートアップ/配下 と src/配下 にbatを作成
    ask = input("はかどり小町ちゃんをスタートアップに登録しますか？(y/n): ")
    need_to_add_startup = (ask in ("", "y", "yes", "Yes"))

    if need_to_add_startup:
        with open(bat_path + '\\'"komati.bat", "w+") as bat_file:
            text = "cd " + os.path.dirname(abs_file_path) + "\n"
            text += 'python {}'.format(file_path)
            bat_file.write(text)
        print(file_path + " を実行する bat ファイルをスタートアップに登録しました")

    ask = input("src/配下にバッチファイルを作成しますか？(y/n): ")
    need_to_make_bat = (ask in ("", "y", "yes", "Yes"))
    if need_to_make_bat:
        with open("komati.bat", "w+") as bat_file:
            text = "cd " + os.path.dirname(abs_file_path) + "\n"
            text += 'python {}'.format(file_path)
            bat_file.write(text)
    print(file_path + " を実行する bat ファイルを src配下に作成しました")

    # 黒画面を出さない
    # src_path = os.path.dirname(abs_file_path)
    # with open(bat_path + '\\' + "komati_no_window.vbs", "w+") as vbs_file:
    #     text = 'Set ws = CreateObject("Wscript.Shell")' + "\n"
    #     text += 'ws.CurrentDirectory = "{}"'.format(src_path) + "\n"
    #     text += 'ws.run "cmd /c /komati.bat", vbhid' + "\n"
    #     text += ""
    #     vbs_file.write(text)


def set_user_setting(name: str):
    path = "config.py"
    text = "USER_NAME = '" + name + "'\n"
    with open(path, "w+", encoding="utf-8") as f:
        f.write(text)
    print("ユーザー名" + name + "を config.py に登録しました")


if __name__ == "__main__":
    name = input("小町ちゃんに呼んでほしい名前をひらがなで入力してください：")
    set_user_setting(name)
    add_to_startup("main.py")
