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

    connect(ui->btn_1, SIGNAL(clicked(bool)), this, SLOT(set_style()));
    connect(ui->btn_2, SIGNAL(clicked(bool)), this, SLOT(set_style()));
    connect(ui->btn_3, SIGNAL(clicked(bool)), this, SLOT(set_style()));
    connect(ui->btn_4, SIGNAL(clicked(bool)), this, SLOT(set_style()));

    connect(ui->Camera,SIGNAL(clicked()),this,SLOT(changeCamera()));
    ui->Camera->setStyleSheet("border-image:url(:/res/pic/record.png)");
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
    // 获取按钮对象
    QPushButton *btn = qobject_cast<QPushButton*>(sender());

    // 获取按钮当前的样式表
    QString currentStyleSheet = btn->styleSheet();

    // 检查当前样式表中是否包含 "record.jpg"，如果包含则切换为 "recording.png"，否则切换为 "record.png"
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

