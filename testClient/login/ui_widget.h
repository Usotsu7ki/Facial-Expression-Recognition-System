/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.13.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QGridLayout *gridLayout_6;
    QFrame *frame_background;
    QGridLayout *gridLayout_3;
    QVBoxLayout *verticalLayout_2;
    QSpacerItem *verticalSpacer_9;
    QHBoxLayout *horizontalLayout_9;
    QSpacerItem *horizontalSpacer_17;
    QFrame *frame;
    QGridLayout *gridLayout_2;
    QHBoxLayout *horizontalLayout_8;
    QFrame *frame_login;
    QGridLayout *gridLayout_5;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer_2;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QLabel *label_login;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_3;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer_7;
    QFrame *frame_pwd_2;
    QGridLayout *gridLayout_4;
    QHBoxLayout *horizontalLayout_11;
    QSpacerItem *horizontalSpacer_8;
    QLabel *label_pwd_2;
    QLineEdit *lineE_username;
    QSpacerItem *horizontalSpacer_23;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer_6;
    QFrame *frame_pwd;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout_3;
    QSpacerItem *horizontalSpacer_5;
    QLabel *label_pwd;
    QLineEdit *lineE_pwd;
    QSpacerItem *horizontalSpacer_19;
    QSpacerItem *verticalSpacer_4;
    QHBoxLayout *horizontalLayout_6;
    QSpacerItem *horizontalSpacer_13;
    QPushButton *btn_login;
    QSpacerItem *horizontalSpacer_14;
    QSpacerItem *verticalSpacer_5;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer_11;
    QPushButton *pushButton_register;
    QSpacerItem *horizontalSpacer_12;
    QHBoxLayout *horizontalLayout_10;
    QSpacerItem *horizontalSpacer_21;
    QPushButton *pushButton_fgtpwd;
    QSpacerItem *horizontalSpacer_22;
    QSpacerItem *verticalSpacer_6;
    QSpacerItem *verticalSpacer_8;
    QPushButton *btn_help;
    QPushButton *btn_contact;
    QLabel *label;
    QFrame *frame_pic;
    QSpacerItem *horizontalSpacer_18;
    QSpacerItem *verticalSpacer_10;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QString::fromUtf8("Widget"));
        Widget->resize(1600, 900);
        Widget->setMinimumSize(QSize(800, 450));
        Widget->setStyleSheet(QString::fromUtf8(""));
        gridLayout_6 = new QGridLayout(Widget);
        gridLayout_6->setSpacing(0);
        gridLayout_6->setContentsMargins(11, 11, 11, 11);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        gridLayout_6->setContentsMargins(0, 0, 0, 0);
        frame_background = new QFrame(Widget);
        frame_background->setObjectName(QString::fromUtf8("frame_background"));
        frame_background->setStyleSheet(QString::fromUtf8(""));
        frame_background->setFrameShape(QFrame::StyledPanel);
        frame_background->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(frame_background);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalSpacer_9 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_9);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setSpacing(6);
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        horizontalSpacer_17 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer_17);

        frame = new QFrame(frame_background);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(frame);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setSpacing(0);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        frame_login = new QFrame(frame);
        frame_login->setObjectName(QString::fromUtf8("frame_login"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_login->sizePolicy().hasHeightForWidth());
        frame_login->setSizePolicy(sizePolicy);
        frame_login->setMinimumSize(QSize(500, 600));
        frame_login->setMaximumSize(QSize(500, 600));
        frame_login->setStyleSheet(QString::fromUtf8(""));
        frame_login->setFrameShape(QFrame::StyledPanel);
        frame_login->setFrameShadow(QFrame::Raised);
        gridLayout_5 = new QGridLayout(frame_login);
        gridLayout_5->setSpacing(6);
        gridLayout_5->setContentsMargins(11, 11, 11, 11);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalSpacer_2 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        label_login = new QLabel(frame_login);
        label_login->setObjectName(QString::fromUtf8("label_login"));
        QFont font;
        font.setFamily(QString::fromUtf8("Arial"));
        font.setPointSize(22);
        label_login->setFont(font);
        label_login->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout->addWidget(label_login);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout);

        verticalSpacer = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        verticalSpacer_3 = new QSpacerItem(20, 17, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalSpacer_7 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_7);

        frame_pwd_2 = new QFrame(frame_login);
        frame_pwd_2->setObjectName(QString::fromUtf8("frame_pwd_2"));
        frame_pwd_2->setFrameShape(QFrame::StyledPanel);
        frame_pwd_2->setFrameShadow(QFrame::Raised);
        gridLayout_4 = new QGridLayout(frame_pwd_2);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setSpacing(6);
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        horizontalSpacer_8 = new QSpacerItem(10, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_8);

        label_pwd_2 = new QLabel(frame_pwd_2);
        label_pwd_2->setObjectName(QString::fromUtf8("label_pwd_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_pwd_2->sizePolicy().hasHeightForWidth());
        label_pwd_2->setSizePolicy(sizePolicy1);
        label_pwd_2->setMinimumSize(QSize(30, 30));
        label_pwd_2->setMaximumSize(QSize(30, 30));

        horizontalLayout_11->addWidget(label_pwd_2);

        lineE_username = new QLineEdit(frame_pwd_2);
        lineE_username->setObjectName(QString::fromUtf8("lineE_username"));

        horizontalLayout_11->addWidget(lineE_username);


        gridLayout_4->addLayout(horizontalLayout_11, 0, 0, 1, 1);


        horizontalLayout_4->addWidget(frame_pwd_2);

        horizontalSpacer_23 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_23);


        verticalLayout->addLayout(horizontalLayout_4);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalSpacer_6 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);

        frame_pwd = new QFrame(frame_login);
        frame_pwd->setObjectName(QString::fromUtf8("frame_pwd"));
        frame_pwd->setFrameShape(QFrame::StyledPanel);
        frame_pwd->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(frame_pwd);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalSpacer_5 = new QSpacerItem(10, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_5);

        label_pwd = new QLabel(frame_pwd);
        label_pwd->setObjectName(QString::fromUtf8("label_pwd"));
        sizePolicy1.setHeightForWidth(label_pwd->sizePolicy().hasHeightForWidth());
        label_pwd->setSizePolicy(sizePolicy1);
        label_pwd->setMinimumSize(QSize(30, 30));
        label_pwd->setMaximumSize(QSize(30, 30));

        horizontalLayout_3->addWidget(label_pwd);

        lineE_pwd = new QLineEdit(frame_pwd);
        lineE_pwd->setObjectName(QString::fromUtf8("lineE_pwd"));

        horizontalLayout_3->addWidget(lineE_pwd);


        gridLayout->addLayout(horizontalLayout_3, 0, 0, 1, 1);


        horizontalLayout_2->addWidget(frame_pwd);

        horizontalSpacer_19 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_19);


        verticalLayout->addLayout(horizontalLayout_2);

        verticalSpacer_4 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout->addItem(verticalSpacer_4);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        horizontalSpacer_13 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_13);

        btn_login = new QPushButton(frame_login);
        btn_login->setObjectName(QString::fromUtf8("btn_login"));
        sizePolicy1.setHeightForWidth(btn_login->sizePolicy().hasHeightForWidth());
        btn_login->setSizePolicy(sizePolicy1);
        btn_login->setMinimumSize(QSize(320, 50));
        btn_login->setMaximumSize(QSize(320, 50));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Arial"));
        font1.setPointSize(12);
        btn_login->setFont(font1);
        btn_login->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_6->addWidget(btn_login);

        horizontalSpacer_14 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_14);


        verticalLayout->addLayout(horizontalLayout_6);

        verticalSpacer_5 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_5);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalSpacer_11 = new QSpacerItem(28, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_11);

        pushButton_register = new QPushButton(frame_login);
        pushButton_register->setObjectName(QString::fromUtf8("pushButton_register"));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Arial"));
        font2.setUnderline(true);
        pushButton_register->setFont(font2);
        pushButton_register->setStyleSheet(QString::fromUtf8("pushButton_register{\n"
"    border: none;//\346\234\200\345\244\226\345\261\202\350\276\271\346\241\206\n"
"}"));

        horizontalLayout_5->addWidget(pushButton_register);

        horizontalSpacer_12 = new QSpacerItem(80, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_12);


        verticalLayout->addLayout(horizontalLayout_5);

        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setSpacing(6);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        horizontalSpacer_21 = new QSpacerItem(28, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_10->addItem(horizontalSpacer_21);

        pushButton_fgtpwd = new QPushButton(frame_login);
        pushButton_fgtpwd->setObjectName(QString::fromUtf8("pushButton_fgtpwd"));
        pushButton_fgtpwd->setFont(font2);

        horizontalLayout_10->addWidget(pushButton_fgtpwd);

        horizontalSpacer_22 = new QSpacerItem(80, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_10->addItem(horizontalSpacer_22);


        verticalLayout->addLayout(horizontalLayout_10);

        verticalSpacer_6 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_6);

        verticalSpacer_8 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_8);

        btn_help = new QPushButton(frame_login);
        btn_help->setObjectName(QString::fromUtf8("btn_help"));
        btn_help->setFont(font2);
        btn_help->setStyleSheet(QString::fromUtf8(""));

        verticalLayout->addWidget(btn_help);

        btn_contact = new QPushButton(frame_login);
        btn_contact->setObjectName(QString::fromUtf8("btn_contact"));
        btn_contact->setFont(font2);

        verticalLayout->addWidget(btn_contact);

        label = new QLabel(frame_login);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout->addWidget(label);


        gridLayout_5->addLayout(verticalLayout, 0, 0, 1, 1);


        horizontalLayout_8->addWidget(frame_login);

        frame_pic = new QFrame(frame);
        frame_pic->setObjectName(QString::fromUtf8("frame_pic"));
        sizePolicy.setHeightForWidth(frame_pic->sizePolicy().hasHeightForWidth());
        frame_pic->setSizePolicy(sizePolicy);
        frame_pic->setMinimumSize(QSize(500, 600));
        frame_pic->setStyleSheet(QString::fromUtf8(""));
        frame_pic->setFrameShape(QFrame::StyledPanel);
        frame_pic->setFrameShadow(QFrame::Raised);

        horizontalLayout_8->addWidget(frame_pic);


        gridLayout_2->addLayout(horizontalLayout_8, 0, 0, 1, 1);


        horizontalLayout_9->addWidget(frame);

        horizontalSpacer_18 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer_18);


        verticalLayout_2->addLayout(horizontalLayout_9);

        verticalSpacer_10 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_10);


        gridLayout_3->addLayout(verticalLayout_2, 0, 0, 1, 1);


        gridLayout_6->addWidget(frame_background, 0, 0, 1, 1);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QCoreApplication::translate("Widget", "Widget", nullptr));
        label_login->setText(QCoreApplication::translate("Widget", "LOGIN", nullptr));
        label_pwd_2->setText(QString());
        label_pwd->setText(QString());
        btn_login->setText(QCoreApplication::translate("Widget", "LOGIN", nullptr));
        pushButton_register->setText(QCoreApplication::translate("Widget", "Register", nullptr));
        pushButton_fgtpwd->setText(QCoreApplication::translate("Widget", "Forget Password", nullptr));
        btn_help->setText(QCoreApplication::translate("Widget", "help", nullptr));
        btn_contact->setText(QCoreApplication::translate("Widget", "contact us", nullptr));
        label->setText(QCoreApplication::translate("Widget", "version 0.0.0", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
