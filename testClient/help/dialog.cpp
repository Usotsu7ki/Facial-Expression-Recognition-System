#include "dialog.h"
#include "ui_dialog.h"
#include <QFile>
#include <QTextStream>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);

    /* 背景图设置 */

}
void Dialog::set_style()
{
    QPalette palette;
    QPushButton *btn = qobject_cast<QPushButton*>(sender()); // 获取发射信号的按钮对象
    QString filePath;
    QString backgroundImagePath;

    if (btn->objectName() == "btn_1") {
        filePath = ":/qss/style.qss";

    } else if (btn->objectName() == "btn_2") {
        filePath = ":/qss/style1.qss";

    } else if (btn->objectName() == "btn_3") {
        filePath = ":/qss/style2.qss";

    } else if (btn->objectName() == "btn_4") {
        filePath = ":/qss/style3.qss";

    }

    /* 皮肤设置 */
    QFile file(filePath);
    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    this->setStyleSheet(stylesheet);
    file.close();


}

Dialog::~Dialog()
{
    delete ui;
}

