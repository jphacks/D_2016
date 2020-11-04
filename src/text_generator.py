import count_docx

def generate_text() -> str:
    """話す文章を返す
    """
    # TODO: 変える
    txt = count_docx.count_docx("test.docx")
    txt = str(txt) + "文字記載おつかれさまです"

    return txt