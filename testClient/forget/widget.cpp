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

    ui->username->setPlaceholderText("User name");
    ui->security_answer->setPlaceholderText("Security answer");
    ui->new_password->setPlaceholderText("New password");

    // 创建一个QPalette对象
   QPalette palette;

   // 加载背景图片
   QPixmap backgroundImage(":/res/pic/login.jpg");

   // 缩放背景图片以适应MainWindow的大小
   backgroundImage = backgroundImage.scaled(size(), Qt::IgnoreAspectRatio);

   // 将背景图片设置为QPalette的背景
   palette.setBrush(QPalette::Background, backgroundImage);

   // 将QPalette应用到MainWindow中
   setPalette(palette);

}



Widget::~Widget()
{
    delete ui;
}