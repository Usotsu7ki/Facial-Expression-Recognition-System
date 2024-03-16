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
    QGridLayout *gridLayout_7;
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
    QGridLayout *gridLayout_10;
    QSpacerItem *verticalSpacer_12;
    QGridLayout *gridLayout_9;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QLabel *label_login;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_16;
    QSpacerItem *verticalSpacer_7;
    QPushButton *btn_forget_2;
    QHBoxLayout *horizontalLayout_6;
    QSpacerItem *horizontalSpacer_13;
    QPushButton *btn_forget;
    QSpacerItem *horizontalSpacer_14;
    QSpacerItem *verticalSpacer_6;
    QHBoxLayout *horizontalLayout_7;
    QSpacerItem *horizontalSpacer_8;
    QFrame *frame_pwd_2;
    QGridLayout *gridLayout_4;
    QHBoxLayout *horizontalLayout_10;
    QSpacerItem *horizontalSpacer_9;
    QLabel *label_pwd_2;
    QLineEdit *username;
    QSpacerItem *horizontalSpacer_20;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer_12;
    QFrame *frame_pwd_4;
    QGridLayout *gridLayout_6;
    QHBoxLayout *horizontalLayout_13;
    QSpacerItem *horizontalSpacer_15;
    QLabel *label_pwd_4;
    QLineEdit *security_answer;
    QSpacerItem *horizontalSpacer_22;
    QPushButton *btn_forget_3;
    QLabel *label;
    QHBoxLayout *horizontalLayout_11;
    QSpacerItem *horizontalSpacer_10;
    QFrame *frame_pwd_3;
    QGridLayout *gridLayout_5;
    QHBoxLayout *horizontalLayout_12;
    QSpacerItem *horizontalSpacer_11;
    QLabel *label_pwd_3;
    QLabel *security_label;
    QSpacerItem *horizontalSpacer_21;
    QSpacerItem *verticalSpacer_15;
    QHBoxLayout *horizontalLayout_15;
    QSpacerItem *horizontalSpacer_23;
    QFrame *frame_pwd_5;
    QGridLayout *gridLayout_8;
    QHBoxLayout *horizontalLayout_16;
    QSpacerItem *horizontalSpacer_24;
    QLabel *label_pwd_5;
    QLineEdit *new_password;
    QSpacerItem *horizontalSpacer_25;
    QSpacerItem *verticalSpacer_8;
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
        gridLayout_7 = new QGridLayout(Widget);
        gridLayout_7->setSpacing(6);
        gridLayout_7->setContentsMargins(11, 11, 11, 11);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
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
        gridLayout_10 = new QGridLayout(frame_login);
        gridLayout_10->setSpacing(6);
        gridLayout_10->setContentsMargins(11, 11, 11, 11);
        gridLayout_10->setObjectName(QString::fromUtf8("gridLayout_10"));
        verticalSpacer_12 = new QSpacerItem(17, 18, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_10->addItem(verticalSpacer_12, 0, 0, 1, 1);

        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(6);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
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


        gridLayout_9->addLayout(horizontalLayout, 0, 0, 1, 2);

        verticalSpacer = new QSpacerItem(17, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer, 1, 0, 1, 2);

        verticalSpacer_16 = new QSpacerItem(17, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_16, 3, 0, 1, 2);

        verticalSpacer_7 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_7, 7, 0, 1, 2);

        btn_forget_2 = new QPushButton(frame_login);
        btn_forget_2->setObjectName(QString::fromUtf8("btn_forget_2"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Arial"));
        font1.setUnderline(true);
        btn_forget_2->setFont(font1);

        gridLayout_9->addWidget(btn_forget_2, 13, 0, 1, 2);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        horizontalSpacer_13 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_13);

        btn_forget = new QPushButton(frame_login);
        btn_forget->setObjectName(QString::fromUtf8("btn_forget"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(btn_forget->sizePolicy().hasHeightForWidth());
        btn_forget->setSizePolicy(sizePolicy1);
        btn_forget->setMinimumSize(QSize(320, 50));
        btn_forget->setMaximumSize(QSize(320, 50));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Arial"));
        font2.setPointSize(12);
        font2.setUnderline(false);
        btn_forget->setFont(font2);

        horizontalLayout_6->addWidget(btn_forget);

        horizontalSpacer_14 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_14);


        gridLayout_9->addLayout(horizontalLayout_6, 10, 0, 1, 2);

        verticalSpacer_6 = new QSpacerItem(17, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_6, 9, 0, 1, 2);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalSpacer_8 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_8);

        frame_pwd_2 = new QFrame(frame_login);
        frame_pwd_2->setObjectName(QString::fromUtf8("frame_pwd_2"));
        frame_pwd_2->setFrameShape(QFrame::StyledPanel);
        frame_pwd_2->setFrameShadow(QFrame::Raised);
        gridLayout_4 = new QGridLayout(frame_pwd_2);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setSpacing(6);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        horizontalSpacer_9 = new QSpacerItem(10, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_10->addItem(horizontalSpacer_9);

        label_pwd_2 = new QLabel(frame_pwd_2);
        label_pwd_2->setObjectName(QString::fromUtf8("label_pwd_2"));
        sizePolicy1.setHeightForWidth(label_pwd_2->sizePolicy().hasHeightForWidth());
        label_pwd_2->setSizePolicy(sizePolicy1);
        label_pwd_2->setMinimumSize(QSize(30, 30));
        label_pwd_2->setMaximumSize(QSize(30, 30));

        horizontalLayout_10->addWidget(label_pwd_2);

        username = new QLineEdit(frame_pwd_2);
        username->setObjectName(QString::fromUtf8("username"));

        horizontalLayout_10->addWidget(username);


        gridLayout_4->addLayout(horizontalLayout_10, 0, 0, 1, 1);


        horizontalLayout_7->addWidget(frame_pwd_2);

        horizontalSpacer_20 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_20);


        gridLayout_9->addLayout(horizontalLayout_7, 2, 0, 1, 2);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalSpacer_12 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_12);

        frame_pwd_4 = new QFrame(frame_login);
        frame_pwd_4->setObjectName(QString::fromUtf8("frame_pwd_4"));
        frame_pwd_4->setFrameShape(QFrame::StyledPanel);
        frame_pwd_4->setFrameShadow(QFrame::Raised);
        gridLayout_6 = new QGridLayout(frame_pwd_4);
        gridLayout_6->setSpacing(6);
        gridLayout_6->setContentsMargins(11, 11, 11, 11);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setSpacing(6);
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        horizontalSpacer_15 = new QSpacerItem(10, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_13->addItem(horizontalSpacer_15);

        label_pwd_4 = new QLabel(frame_pwd_4);
        label_pwd_4->setObjectName(QString::fromUtf8("label_pwd_4"));
        sizePolicy1.setHeightForWidth(label_pwd_4->sizePolicy().hasHeightForWidth());
        label_pwd_4->setSizePolicy(sizePolicy1);
        label_pwd_4->setMinimumSize(QSize(30, 30));
        label_pwd_4->setMaximumSize(QSize(30, 30));

        horizontalLayout_13->addWidget(label_pwd_4);

        security_answer = new QLineEdit(frame_pwd_4);
        security_answer->setObjectName(QString::fromUtf8("security_answer"));

        horizontalLayout_13->addWidget(security_answer);


        gridLayout_6->addLayout(horizontalLayout_13, 0, 0, 1, 1);


        horizontalLayout_5->addWidget(frame_pwd_4);

        horizontalSpacer_22 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_22);


        gridLayout_9->addLayout(horizontalLayout_5, 6, 0, 1, 2);

        btn_forget_3 = new QPushButton(frame_login);
        btn_forget_3->setObjectName(QString::fromUtf8("btn_forget_3"));
        btn_forget_3->setFont(font1);
        btn_forget_3->setStyleSheet(QString::fromUtf8(""));

        gridLayout_9->addWidget(btn_forget_3, 12, 0, 1, 2);

        label = new QLabel(frame_login);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_9->addWidget(label, 14, 0, 1, 2);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setSpacing(6);
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        horizontalSpacer_10 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_10);

        frame_pwd_3 = new QFrame(frame_login);
        frame_pwd_3->setObjectName(QString::fromUtf8("frame_pwd_3"));
        frame_pwd_3->setFrameShape(QFrame::StyledPanel);
        frame_pwd_3->setFrameShadow(QFrame::Raised);
        gridLayout_5 = new QGridLayout(frame_pwd_3);
        gridLayout_5->setSpacing(6);
        gridLayout_5->setContentsMargins(11, 11, 11, 11);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setSpacing(6);
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        horizontalSpacer_11 = new QSpacerItem(13, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_12->addItem(horizontalSpacer_11);

        label_pwd_3 = new QLabel(frame_pwd_3);
        label_pwd_3->setObjectName(QString::fromUtf8("label_pwd_3"));
        sizePolicy1.setHeightForWidth(label_pwd_3->sizePolicy().hasHeightForWidth());
        label_pwd_3->setSizePolicy(sizePolicy1);
        label_pwd_3->setMinimumSize(QSize(30, 30));
        label_pwd_3->setMaximumSize(QSize(30, 30));

        horizontalLayout_12->addWidget(label_pwd_3);

        security_label = new QLabel(frame_pwd_3);
        security_label->setObjectName(QString::fromUtf8("security_label"));
        QFont font3;
        font3.setFamily(QString::fromUtf8("Arial"));
        security_label->setFont(font3);

        horizontalLayout_12->addWidget(security_label);


        gridLayout_5->addLayout(horizontalLayout_12, 0, 0, 1, 1);


        horizontalLayout_11->addWidget(frame_pwd_3);

        horizontalSpacer_21 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_21);


        gridLayout_9->addLayout(horizontalLayout_11, 4, 0, 1, 2);

        verticalSpacer_15 = new QSpacerItem(20, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_15, 5, 0, 1, 2);

        horizontalLayout_15 = new QHBoxLayout();
        horizontalLayout_15->setSpacing(6);
        horizontalLayout_15->setObjectName(QString::fromUtf8("horizontalLayout_15"));
        horizontalSpacer_23 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_15->addItem(horizontalSpacer_23);

        frame_pwd_5 = new QFrame(frame_login);
        frame_pwd_5->setObjectName(QString::fromUtf8("frame_pwd_5"));
        frame_pwd_5->setFrameShape(QFrame::StyledPanel);
        frame_pwd_5->setFrameShadow(QFrame::Raised);
        gridLayout_8 = new QGridLayout(frame_pwd_5);
        gridLayout_8->setSpacing(6);
        gridLayout_8->setContentsMargins(11, 11, 11, 11);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        horizontalLayout_16 = new QHBoxLayout();
        horizontalLayout_16->setSpacing(6);
        horizontalLayout_16->setObjectName(QString::fromUtf8("horizontalLayout_16"));
        horizontalSpacer_24 = new QSpacerItem(10, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_16->addItem(horizontalSpacer_24);

        label_pwd_5 = new QLabel(frame_pwd_5);
        label_pwd_5->setObjectName(QString::fromUtf8("label_pwd_5"));
        sizePolicy1.setHeightForWidth(label_pwd_5->sizePolicy().hasHeightForWidth());
        label_pwd_5->setSizePolicy(sizePolicy1);
        label_pwd_5->setMinimumSize(QSize(30, 30));
        label_pwd_5->setMaximumSize(QSize(30, 30));

        horizontalLayout_16->addWidget(label_pwd_5);

        new_password = new QLineEdit(frame_pwd_5);
        new_password->setObjectName(QString::fromUtf8("new_password"));

        horizontalLayout_16->addWidget(new_password);


        gridLayout_8->addLayout(horizontalLayout_16, 0, 0, 1, 1);


        horizontalLayout_15->addWidget(frame_pwd_5);

        horizontalSpacer_25 = new QSpacerItem(80, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        horizontalLayout_15->addItem(horizontalSpacer_25);


        gridLayout_9->addLayout(horizontalLayout_15, 8, 0, 1, 2);

        verticalSpacer_8 = new QSpacerItem(17, 13, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_8, 11, 0, 1, 2);


        gridLayout_10->addLayout(gridLayout_9, 1, 0, 1, 1);


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


        gridLayout_7->addWidget(frame_background, 0, 0, 1, 1);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QCoreApplication::translate("Widget", "Widget", nullptr));
        label_login->setText(QCoreApplication::translate("Widget", "Forget password", nullptr));
        btn_forget_2->setText(QCoreApplication::translate("Widget", "contact us", nullptr));
        btn_forget->setText(QCoreApplication::translate("Widget", "Submit it", nullptr));
        label_pwd_2->setText(QString());
        label_pwd_4->setText(QString());
        btn_forget_3->setText(QCoreApplication::translate("Widget", "help", nullptr));
        label->setText(QCoreApplication::translate("Widget", "version 0.0.0", nullptr));
        label_pwd_3->setText(QString());
        security_label->setText(QCoreApplication::translate("Widget", "Security", nullptr));
        label_pwd_5->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
