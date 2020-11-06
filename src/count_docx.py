import docx

def count_docx(read_path):
    doc= docx.Document(read_path)
    txts = []
    
    # ワードから文章を取得
    for par in doc.paragraphs:
        txts.append(par.text)
    
    total = 0
    for txt in txts:
        total += len(txt)
    
    #print("文章は「{}」で、".format(txts))
    #print("文字数は{}です".format(total))
    return total 
    
if __name__ == '__main__':
    read_path = "test.docx"
    count_docx(read_path)