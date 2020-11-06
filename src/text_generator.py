import count_docx
import sound

def get_start_word_num() -> int:
    file_path = "log/start_word_num.txt"
    with open(file_path, "r", encoding="UTF-8", errors="ignore") as f:
        word_num = f.readline()
    return int(word_num)

def generate_text(event) -> str:
    txt = ""
    if event == "start":
        txt = "今日もいちにち頑張りましょう!"

    if event == "terminate":
        f_num = count_docx.count_docx("test.docx")
        s_num = get_start_word_num()
        txt = int(f_num) - int(s_num)
        txt = str(txt) + "文字の記載進みましたね！"
    
    if event == "cheer":
        txt = "お疲れ様です。ちょっと休憩しましょうか?"
        
    if event == "praise":
        txt = "よく頑張っていますね!"
    
    if event == None:
        txt = "eventが指定されていません"

    return txt

# TODO たまに名前で読んでくれる?

if __name__ == '__main__':
    event = "cheer"
    txt = generate_text(event)
    print(txt)
    sound.play_sound(txt)
    