import count_docx
import sound
import activity_log
import config


def generate_text(event) -> str:

    if event == "start":
        txt = "今日もいちにち頑張りましょう!"

    if event == "terminate":
        txt = count_docx.count_docx("test.docx")
        txt = str(txt) + "文字記載おつかれさまです"

    if event == "cheer":
        working_time_second = activity_log.get_working_time_on_current_window(
            interval=2)
        working_time_hour = working_time_second // 3600
        txt = str(working_time_hour) + "時間の作業お疲れ様です。ちょっと休憩しましょうか?"

    if event == "praise":
        txt = "よく頑張っていますね!"

    if event == None:
        txt = "eventが指定されていません"

    user_name = config.USER_NAME
    txt = user_name + "さん、" + txt
    return txt

# TODO たまに名前で読んでくれる?


if __name__ == '__main__':
    event = "cheer"
    txt = generate_text(event)
    print(txt)
    sound.play_sound(txt)
