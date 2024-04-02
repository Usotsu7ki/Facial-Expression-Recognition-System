/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.13.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionhelp;
    QAction *actionContact_us;
    QAction *actionLog_out;
    QAction *actionQuit_Ctrl_W;
    QAction *actionstarry_sky;
    QAction *actionsea;
    QAction *actiondesert;
    QAction *actiongrassland;
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QListWidget *listWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QTextEdit *textEdit;
    QPushButton *sendButton;
    QMenuBar *menubar;
    QMenu *menumenu;
    QMenu *menusetting;
    QMenu *menuAppearance;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 600);
        actionhelp = new QAction(MainWindow);
        actionhelp->setObjectName(QString::fromUtf8("actionhelp"));
        actionContact_us = new QAction(MainWindow);
        actionContact_us->setObjectName(QString::fromUtf8("actionContact_us"));
        actionLog_out = new QAction(MainWindow);
        actionLog_out->setObjectName(QString::fromUtf8("actionLog_out"));
        actionQuit_Ctrl_W = new QAction(MainWindow);
        actionQuit_Ctrl_W->setObjectName(QString::fromUtf8("actionQuit_Ctrl_W"));
        actionstarry_sky = new QAction(MainWindow);
        actionstarry_sky->setObjectName(QString::fromUtf8("actionstarry_sky"));
        actionsea = new QAction(MainWindow);
        actionsea->setObjectName(QString::fromUtf8("actionsea"));
        actiondesert = new QAction(MainWindow);
        actiondesert->setObjectName(QString::fromUtf8("actiondesert"));
        actiongrassland = new QAction(MainWindow);
        actiongrassland->setObjectName(QString::fromUtf8("actiongrassland"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));

        gridLayout->addLayout(horizontalLayout, 2, 0, 1, 1);

        listWidget_2 = new QListWidget(centralwidget);
        listWidget_2->setObjectName(QString::fromUtf8("listWidget_2"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(listWidget_2->sizePolicy().hasHeightForWidth());
        listWidget_2->setSizePolicy(sizePolicy);
        listWidget_2->setMinimumSize(QSize(700, 300));

        gridLayout->addWidget(listWidget_2, 0, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        textEdit = new QTextEdit(centralwidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));

        horizontalLayout_2->addWidget(textEdit);

        sendButton = new QPushButton(centralwidget);
        sendButton->setObjectName(QString::fromUtf8("sendButton"));
        sendButton->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(sendButton->sizePolicy().hasHeightForWidth());
        sendButton->setSizePolicy(sizePolicy1);
        sendButton->setMinimumSize(QSize(60, 0));
        QFont font;
        font.setFamily(QString::fromUtf8("Arial"));
        sendButton->setFont(font);

        horizontalLayout_2->addWidget(sendButton);


        gridLayout->addLayout(horizontalLayout_2, 1, 0, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 21));
        menumenu = new QMenu(menubar);
        menumenu->setObjectName(QString::fromUtf8("menumenu"));
        menusetting = new QMenu(menubar);
        menusetting->setObjectName(QString::fromUtf8("menusetting"));
        menuAppearance = new QMenu(menusetting);
        menuAppearance->setObjectName(QString::fromUtf8("menuAppearance"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menumenu->menuAction());
        menubar->addAction(menusetting->menuAction());
        menumenu->addAction(actionhelp);
        menumenu->addAction(actionContact_us);
        menumenu->addSeparator();
        menusetting->addAction(menuAppearance->menuAction());
        menuAppearance->addAction(actionstarry_sky);
        menuAppearance->addAction(actionsea);
        menuAppearance->addAction(actiondesert);
        menuAppearance->addAction(actiongrassland);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionhelp->setText(QCoreApplication::translate("MainWindow", "Help", nullptr));
        actionContact_us->setText(QCoreApplication::translate("MainWindow", "Contact us", nullptr));
        actionLog_out->setText(QCoreApplication::translate("MainWindow", "Log out", nullptr));
        actionQuit_Ctrl_W->setText(QCoreApplication::translate("MainWindow", "Quit               Ctrl+W", nullptr));
        actionstarry_sky->setText(QCoreApplication::translate("MainWindow", "starry sky", nullptr));
        actionsea->setText(QCoreApplication::translate("MainWindow", "sea", nullptr));
        actiondesert->setText(QCoreApplication::translate("MainWindow", "desert", nullptr));
        actiongrassland->setText(QCoreApplication::translate("MainWindow", "grassland", nullptr));
        sendButton->setText(QCoreApplication::translate("MainWindow", "send", nullptr));
        menumenu->setTitle(QCoreApplication::translate("MainWindow", "menu", nullptr));
        menusetting->setTitle(QCoreApplication::translate("MainWindow", "setting", nullptr));
        menuAppearance->setTitle(QCoreApplication::translate("MainWindow", "Appearance", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
