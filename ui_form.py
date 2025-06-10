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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 446)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_top)

        self.label_ssonumber = QLabel(self.centralwidget)
        self.label_ssonumber.setObjectName(u"label_ssonumber")

        self.verticalLayout.addWidget(self.label_ssonumber, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_ssonumber = QLineEdit(self.centralwidget)
        self.lineEdit_ssonumber.setObjectName(u"lineEdit_ssonumber")

        self.verticalLayout.addWidget(self.lineEdit_ssonumber, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout.addWidget(self.label_password, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.verticalLayout.addWidget(self.lineEdit_password, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_login = QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.verticalLayout.addWidget(self.pushButton_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 551, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_ssonumber.setText(QCoreApplication.translate("MainWindow", u"SSO NUMBER", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

