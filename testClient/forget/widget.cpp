#include "widget.h"
#include "ui_widget.h"
#include <QFile>
#include <QTextStream>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    ui->label_pwd_2->setScaledContents(true);         //图片自适应label大小
    ui->label_pwd_3->setScaledContents(true);         //图片自适应label大小
    ui->label_pwd_4->setScaledContents(true);         //图片自适应label大小
    ui->label_pwd_5->setScaledContents(true);         //图片自适应label大小
    ui->label_pwd_6->setScaledContents(true);         //图片自适应label大小

    ui->new_password->setEchoMode(QLineEdit::Password);//设置为小黑点
    ui->check_password->setEchoMode(QLineEdit::Password);//设置为小黑点
    ui->username->setPlaceholderText("User name");
    ui->security_answer->setPlaceholderText("Security answer");
    ui->new_password->setPlaceholderText("New password");
    ui->check_password->setPlaceholderText("Check password");
    /* 背景图设置 */


}

void Widget::set_style()
{
    QPushButton *btn = qobject_cast<QPushButton*>(sender()); // 获取发射信号的按钮对象
    QString filePath;
    QString backgroundImagePath;

    if (btn->objectName() == "btn_1") {
        filePath = ":/res/qss/style-1.qss";

    } else if (btn->objectName() == "btn_2") {
        filePath = ":/res/qss/style-2.qss";

    } else if (btn->objectName() == "btn_3") {
        filePath = ":/res/qss/style-3.qss";

    } else if (btn->objectName() == "btn_4") {
        filePath = ":/res/qss/style-4.qss";

    }

    /* 皮肤设置 */
    QFile file(filePath);
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
