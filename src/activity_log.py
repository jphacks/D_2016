import time
import datetime
from win32gui import GetWindowText, GetForegroundWindow

# This code is based from
# https://github.com/aikige/homeBinWin/blob/master/dumpForegroundWindow.py


def get_active_window_title():
    return GetWindowText(GetForegroundWindow())


def get_log_string(title: str, state: str = "A"):
    """
    ログ出力文字列を取得
    - A: Active window
    - S: プログラムが起動
    - T: プログラムが終了
    """
    assert state in ("A", "S", "T"), "stateは、A, S, Tのいずれかを指定"
    now = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S, ')
    return state + ", " + now + title


def format_date(date):
    return date.strftime("%Y%m%d")


def get_log_filename(date):
    return "log/" + date + "-Window_Log.txt"


def get_old_activity() -> str:
    tmp_file_path = "log/tmp.txt"
    with open(tmp_file_path, "r", encoding="UTF-8", errors="ignore") as f:
        old = f.readline()
    return old


def set_old_activity(old_activity: str):
    tmp_file_path = "log/tmp.txt"
    with open(tmp_file_path, "w", encoding="UTF-8", errors="ignore") as f:
        f.write(old_activity)


def print_to_file(title: str, state: str):
    out = get_log_string(title, state)
    print(out)
    day = format_date(datetime.datetime.today())

    with open(get_log_filename(day), "a", encoding="UTF-8", errors="ignore") as f:
        f.write(out + "\n")
        f.flush()


def get_title_of_active_window(skip_duplicate) -> str:
    """skip_duplicate: trueの場合、
    前回と同じアクティブウィンドウなら "" を返す
    """
    old = get_old_activity()
    title = get_active_window_title()
    if (skip_duplicate and title == old):
        return ""

    set_old_activity(title)
    return title


def get_all_windows() -> list:
    import ctypes

    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool,
                                         ctypes.POINTER(ctypes.c_int),
                                         ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)

    # 以下のブラックリストは表示しない（これらは裏で常駐してるみたい）
    # TODO: 随時追加していく
    black_list = {"",
                  "Microsoft Text Input Application",  # なにこれ
                  "設定",  # なぜか裏で動いてる
                  "映画 & テレビ",  # なぜかおる
                  "Program Manager",  # 強制終了やトラブルシューティングのために常駐
                  "Xbox Game bar",
                  'Virtual desktop switching preview',  # 仮想デスクトップ切り替え
                  'タスクの切り替え',  # Alt+Tab
                  }
    # 重複、ブラックリストを省く
    titles = set(titles) - black_list
    # print("起動中プログラム一覧を取得しました")
    # print(*titles)
    return list(titles)


def get_title_of_terminated_program(previous_program_list: list, current_program_list: list) -> str:
    # FIXME: ブラウザの場合、タブを変えるだけで開始、終了判定してしまう
    diff = set(previous_program_list) - set(current_program_list)
    if diff:
        title = list(diff)[0]  # 差分はひとつである前提
        # out = get_log_string(title, "T")
        # print(out)
        return title
    return ""


def get_title_of_started_program(previous_program_list: list, current_program_list: list) -> str:
    # FIXME: ブラウザの場合、タブを変えるだけで開始、終了判定してしまう
    diff = set(current_program_list) - set(previous_program_list)
    if diff:
        title = list(diff)[0]  # 差分はひとつである前提
        # out = get_log_string(title, "S")
        # print(out)
        return title
    return ""


def keep_logging(interval, skip_duplicate):
    previous_program_list = get_all_windows()

    while True:
        # プログラムの起動と終了を検知
        current_program_list = get_all_windows()
        started = get_title_of_started_program(
            previous_program_list=previous_program_list,
            current_program_list=current_program_list)
        terminated = get_title_of_terminated_program(
            previous_program_list=previous_program_list,
            current_program_list=current_program_list)

        if terminated:
            title = terminated
            state = "T"
            print_to_file(title, state)

        if started:
            title = started
            state = "S"
            print_to_file(title, state)

        # アクティブウィンドウの記録
        title = get_title_of_active_window(skip_duplicate)
        state = "A"
        if title:
            print_to_file(title, state)

        previous_program_list = current_program_list
        time.sleep(interval)


def main():
    import argparse
    # 引数を指定しない場合は、2秒ごとに記録し、重複タイトルはスキップし変更のタイミングで切り替え
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval',
                        help='set interval of logging in seconds. default interval is 120',
                        type=int,
                        default=2)
    parser.add_argument('-s', '--skip_duplicate',
                        help='if this argument is set, skip logging of duplicated title',
                        action='store_true',
                        default=True)
    args = parser.parse_args()

    # 処理ループ
    keep_logging(args.interval, args.skip_duplicate)


if __name__ == '__main__':
    main()
