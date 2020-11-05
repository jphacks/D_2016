import count_docx
import sound
def generate_text(event) -> str:
    
    if event == "start":
        txt = "今日もいちにち頑張りましょう!"

    if event == "terminate":
        txt = count_docx.count_docx("test.docx")
        txt = str(txt) + "文字記載おつかれさまです"
    
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
    