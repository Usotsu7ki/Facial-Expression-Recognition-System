#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QTextStream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    /* 背景图设置 */

    connect(ui->recordButton,SIGNAL(clicked()),this,SLOT(changeCamera()));
    ui->recordButton->setStyleSheet("border-image:url(:/res/pic/record.png)");
}

void MainWindow::set_style()
{
    QPushButton *btn = qobject_cast<QPushButton*>(sender()); // 获取发射信号的按钮对象
    QString filePath;
    QString backgroundImagePath;
    QString currentStyleSheet = btn->styleSheet();

    if (btn->objectName() == "btn_1") {
        filePath = ":/res/qss/style.qss";

    } else if (btn->objectName() == "btn_2") {
        filePath = ":/res/qss/style1.qss";

    } else if (btn->objectName() == "btn_3") {
        filePath = ":/res/qss/style2.qss";

    } else if (btn->objectName() == "btn_4") {
        filePath = ":/res/qss/style3.qss";

    }


    /* 皮肤设置 */
    QFile file(filePath);
    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    this->setStyleSheet(stylesheet);
    file.close();

}
void MainWindow::changeCamera()
{
    QPushButton *btn = qobject_cast<QPushButton*>(sender());

    QString currentStyleSheet = btn->styleSheet();

    if (currentStyleSheet.contains("record.png")) {
        btn->setStyleSheet("border-image: url(:/res/pic/recording.png);");
    } else {
        btn->setStyleSheet("border-image: url(:/res/pic/record.png);");
    }
}


MainWindow::~MainWindow()
{
    delete ui;
}

