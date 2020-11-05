import docx

def count_docx(read_path):
    
    doc= docx.Document(read_path)
    txt = []
    
    # ワードから文章を取得
    for par in doc.paragraphs:
        txt.append(par.text)
    
    n = len(txt[0])
    #print("文章は「{}」で、".format(txt[0]))
    #print("文字数は{}です".format(n))
    return n 
    
if __name__ == '__main__':
    read_path = "test.docx"
    count_docx(read_path)