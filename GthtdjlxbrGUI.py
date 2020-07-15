import tkinter
def translate(event):
    text=usr_text.get(1.0, tkinter.END)
    s=''
    eng=dict(zip(" qwertyuiop[]asdfghjkl;'zxcvbnm,./?@#$%^&*()-_=+\\|`~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>\n", 
                " йцукенгшщзхъфывапролджэячсмитьбю.,\"№;%:?*()-_=+\\/ёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\n"))
    for i in range(len(text)):
        s+=eng[text[i]]
    translate_text.delete(1.0, tkinter.END)
    translate_text.insert(1.0, s)

root = tkinter.Tk()
root.geometry('300x240')
root.title('Gthtdjlxbr')

frame1=tkinter.Frame(root,bg='red',bd=3)
frame2=tkinter.Frame(root,bg='green',bd=1)
frame3=tkinter.Frame(root, bg='blue', bd=3)

usr_text=tkinter.Text(frame1, width=200, height=5,
                      font='consolas',
                     wrap=tkinter.WORD)
translate_text=tkinter.Text(frame3, width=200, height=5,
                            font='consolas',
                     wrap=tkinter.WORD)
button_translate=tkinter.Button(frame2, text="Gthtdtcnb!")

frame1.pack()
frame2.pack()
frame3.pack()
usr_text.pack()
translate_text.pack()
button_translate.pack()

button_translate.bind('<Button-1>', translate)

root.mainloop()
