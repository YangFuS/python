import os
import re

obj = re.compile(r"第(?P<chapter>.*?)章.*?", re.S)


def my_cmp(s1: str):
    chapter1 = obj.search(s1)
    if chapter1:
        chapter1 = chapter1.group('chapter')
        return int(chapter1)
    else:
        print(s1)
        return 0


file_list = os.listdir("files//仙魔同修")
file_list.sort(key=my_cmp)
f_all = open('files//仙魔同修.txt', mode='w', encoding='utf-8')
for file in file_list:
    f = open('files//仙魔同修//' + file, mode='r', encoding='utf-8')
    data = f.read()
    f.close()
    title = file.replace('.txt', '')
    f_all.write(title + '\n')
    data = data.replace(title.replace(' ', ''), '')
    data = data.replace('    ', '\n\t')
    data = data.replace(' 一秒记住，精彩小说无弹窗免费阅读！', '')
    f_all.write(data + '\n')
    f_all.flush()
    print(f'{title}  写入完成')
f_all.close()
