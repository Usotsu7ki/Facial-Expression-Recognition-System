#include "widget.h"
#include "ui_widget.h"
#include <QFile>
#include <QTextStream>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    ui->label_pwd->setScaledContents(true);         //图片自适应label大小

    ui->lineE_pwd->setEchoMode(QLineEdit::Password);//设置为小黑点

    /* 背景图设置 */


}

/*
* 槽函数-皮肤设置
*/
void Widget::set_style()
{
    QPushButton *btn = qobject_cast<QPushButton*>(sender()); // 获取发射信号的按钮对象
    QString filePath;
    QString backgroundImagePath;

    if (btn->objectName() == "btn_5") {
        filePath = ":/res/qss/style-1.qss";

    } else if (btn->objectName() == "btn_6") {
        filePath = ":/res/qss/style-2.qss";

    } else if (btn->objectName() == "btn_7") {
        filePath = ":/res/qss/style-3.qss";

    } else if (btn->objectName() == "btn_8") {
        filePath = ":/res/qss/style-4.qss";

    }

    /*皮肤设置*/
    QFile file(filePath);/*QSS文件所在的路径*/
    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    this->setStyleSheet(stylesheet);
    file.close();
}

Widget::~Widget()
{
    delete ui;
}
