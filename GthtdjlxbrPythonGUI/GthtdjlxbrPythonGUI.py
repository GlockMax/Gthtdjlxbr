import sys
from PyQt5 import QtWidgets
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Gthtdjl.clicked.connect(self.__gthtdjl)

    def __gthtdjl(self):
        text = self.SearchArea.toPlainText()
        answer = ""
        eng = dict(zip(" qwertyuiop[]asdfghjkl;'zxcvbnm,./?@#$%^&*()-_=+\\|`~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>\n", 
            " йцукенгшщзхъфывапролджэячсмитьбю.,\"№;%:?*()-_=+\\/ёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\n"))

        for i in range(len(text)):
            try:
                answer += eng[text[i]]
            except:
                answer += text[i]
        self.AnswerArea.setPlainText(answer)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

