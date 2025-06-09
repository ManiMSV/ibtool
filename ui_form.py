# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_ssonumber = QLineEdit(self.centralwidget)
        self.lineEdit_ssonumber.setObjectName(u"lineEdit_ssonumber")

        self.gridLayout.addWidget(self.lineEdit_ssonumber, 2, 0, 1, 2)

        self.pushButton_login = QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.gridLayout.addWidget(self.pushButton_login, 6, 0, 1, 1)

        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_top, 0, 0, 1, 2)

        self.label_ssonumber = QLabel(self.centralwidget)
        self.label_ssonumber.setObjectName(u"label_ssonumber")

        self.gridLayout.addWidget(self.label_ssonumber, 1, 0, 1, 2)

        self.pushButton_register = QPushButton(self.centralwidget)
        self.pushButton_register.setObjectName(u"pushButton_register")

        self.gridLayout.addWidget(self.pushButton_register, 6, 1, 1, 1)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 4, 0, 1, 2)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 5, 0, 1, 2)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_bottom, 7, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1056, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_ssonumber.setText(QCoreApplication.translate("MainWindow", u"SSO NUMBER", None))
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
    # retranslateUi

