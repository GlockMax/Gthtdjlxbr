from datetime import datetime


text = input("Введите текст для перевода:\n")

answer = ''

eng = dict(zip(" qwertyuiop[]asdfghjkl;'zxcvbnm,./?@#$%^&*()-_=+\\|`~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>\n", 
            " йцукенгшщзхъфывапролджэячсмитьбю.,\"№;%:?*()-_=+\\/ёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\n"))

for i in range(len(text)):
    try:
        answer += eng[text[i]]
    except:
        answer += text[i]

print(answer)

