#include "mainwindow.h"
#include <string>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    button = new QPushButton("Gthtdtcnb", this);
    edit_answer = new QTextEdit(this);
    edit_search = new QTextEdit(this);

    edit_search -> setGeometry(5, 5, 390, 115);

    button -> setGeometry(100, 125, 200, 45);

    edit_answer -> setGeometry(5, 175, 390, 115);
    edit_answer -> isReadOnly();

    connect(button, SIGNAL (released()), this, SLOT (handleButton()));
}

void MainWindow::handleButton()
{
    // меняем текст
    QString search = edit_search ->toPlainText();
    edit_answer ->setText(MainWindow::translation(search));
}

static int indexof(std::string s, QCharRef x){
    for (int i = 0 ; i < s.size(); i++){
        if (s[i] == x)
            return i;
    }
    return -1;
}

QString MainWindow::translation(QString search){
    //setlocale(LC_ALL, "ru-RU");

    std::string eng = "`1234567890-=\\qwertyuiop[]asdfghjkl;\'zxcvbnm,./\n ~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?";
    const char* rus[96] = {"ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "\\",
                           "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ",
                           "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э",
                           "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".", "\n", " ",
                           "Ё", "!", "\"", "№", ";", "%", ":", "?", "*", "(", ")", "_", "+", "/",
                           "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ",
                           "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э",
                           "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ","};

    QString answer;
    for (int i = 0 ; i < search.size() ; i++){
        answer += rus[indexof(eng, QCharRef(search[i]))];
    }
    return answer;
}

MainWindow::~MainWindow()
{
    //delete ui;
}

