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
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionhelp;
    QAction *actioncontact_us;
    QAction *actionLog_out;
    QAction *actionOpen_record_folder;
    QAction *actionstarry_sky;
    QAction *actionsea;
    QAction *actiondesert;
    QAction *actiongrassland;
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *shotButton;
    QGraphicsView *graphicsView;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer;
    QPushButton *recordButton;
    QSpacerItem *horizontalSpacer_3;
    QLabel *label;
    QTextEdit *textEdit;
    QMenuBar *menubar;
    QMenu *menumenu;
    QMenu *menusetting;
    QMenu *menuAppearance;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(700, 900);
        actionhelp = new QAction(MainWindow);
        actionhelp->setObjectName(QString::fromUtf8("actionhelp"));
        actioncontact_us = new QAction(MainWindow);
        actioncontact_us->setObjectName(QString::fromUtf8("actioncontact_us"));
        actionLog_out = new QAction(MainWindow);
        actionLog_out->setObjectName(QString::fromUtf8("actionLog_out"));
        actionOpen_record_folder = new QAction(MainWindow);
        actionOpen_record_folder->setObjectName(QString::fromUtf8("actionOpen_record_folder"));
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
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        shotButton = new QPushButton(centralwidget);
        shotButton->setObjectName(QString::fromUtf8("shotButton"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(shotButton->sizePolicy().hasHeightForWidth());
        shotButton->setSizePolicy(sizePolicy);
        shotButton->setMinimumSize(QSize(130, 50));
        QFont font;
        font.setFamily(QString::fromUtf8("Arial"));
        shotButton->setFont(font);

        horizontalLayout->addWidget(shotButton);


        gridLayout->addLayout(horizontalLayout, 0, 0, 1, 1);

        graphicsView = new QGraphicsView(centralwidget);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Arial"));
        font1.setPointSize(10);
        graphicsView->setFont(font1);

        gridLayout->addWidget(graphicsView, 1, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        recordButton = new QPushButton(centralwidget);
        recordButton->setObjectName(QString::fromUtf8("recordButton"));
        sizePolicy.setHeightForWidth(recordButton->sizePolicy().hasHeightForWidth());
        recordButton->setSizePolicy(sizePolicy);
        recordButton->setMinimumSize(QSize(80, 80));
        recordButton->setFont(font);
        recordButton->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_2->addWidget(recordButton);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_3);


        gridLayout->addLayout(horizontalLayout_2, 2, 0, 1, 1);

        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setFont(font);

        gridLayout->addWidget(label, 3, 0, 1, 1);

        textEdit = new QTextEdit(centralwidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(textEdit->sizePolicy().hasHeightForWidth());
        textEdit->setSizePolicy(sizePolicy1);
        textEdit->setFocusPolicy(Qt::NoFocus);
        textEdit->setInputMethodHints(Qt::ImhNone);

        gridLayout->addWidget(textEdit, 4, 0, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 700, 21));
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
        menumenu->addSeparator();
        menumenu->addAction(actionhelp);
        menumenu->addAction(actioncontact_us);
        menumenu->addSeparator();
        menumenu->addAction(actionOpen_record_folder);
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
        actioncontact_us->setText(QCoreApplication::translate("MainWindow", "Contact Us", nullptr));
        actionLog_out->setText(QCoreApplication::translate("MainWindow", "return", nullptr));
        actionOpen_record_folder->setText(QCoreApplication::translate("MainWindow", "Open record folder", nullptr));
        actionstarry_sky->setText(QCoreApplication::translate("MainWindow", "starry sky", nullptr));
        actionsea->setText(QCoreApplication::translate("MainWindow", "sea", nullptr));
        actiondesert->setText(QCoreApplication::translate("MainWindow", "desert", nullptr));
        actiongrassland->setText(QCoreApplication::translate("MainWindow", "grassland", nullptr));
        shotButton->setText(QCoreApplication::translate("MainWindow", "screen shot", nullptr));
        recordButton->setText(QString());
        label->setText(QCoreApplication::translate("MainWindow", "ConsoleText", nullptr));
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
