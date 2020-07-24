#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPushButton>
#include <QTextEdit>

namespace Ui {
 class MainWindow;
}

class MainWindow : public QMainWindow
{
 Q_OBJECT

public:
 explicit MainWindow(QWidget *parent = 0);
 virtual ~MainWindow();

private slots:
 void handleButton();
 QString translation(QString search);

private:
 QPushButton *button;
 QTextEdit *edit_search;
 QTextEdit *edit_answer;
};

#endif // MAINWINDOW_H
