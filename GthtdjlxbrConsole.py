from datetime import datetime

text = input("Введите текст для перевода:\n")

start_time = datetime.now()
s = ''
eng = dict(zip(" qwertyuiop[]asdfghjkl;'zxcvbnm,./?@#$%^&*()-_=+\\|`~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>\n", 
            " йцукенгшщзхъфывапролджэячсмитьбю.,\"№;%:?*()-_=+\\/ёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\n"))

for i in range(len(text)):
    s += eng[text[i]]

print(s)
print(datetime.now() - start_time)

