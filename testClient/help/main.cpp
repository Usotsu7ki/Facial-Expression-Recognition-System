#include "dialog.h"
#include <QApplication>
#include <QFile>
#include <QTextStream>
#include <QLabel>
#include <QDesktopServices>
#include <QUrl>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QFile file(":/res/qss/style.qss");/*QSS文件所在的路径*/

    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    a.setStyleSheet(stylesheet);
    file.close();

    Dialog w;
    w.setWindowTitle("Help");
    w.show();
    return a.exec();
}
