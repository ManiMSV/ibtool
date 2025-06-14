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
    QSpacerItem, QStackedWidget, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(456, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_message = QLabel(self.centralwidget)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_message, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout = QGridLayout(self.page_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_password = QLabel(self.page_1)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_password, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_ssonumber = QLineEdit(self.page_1)
        self.lineEdit_ssonumber.setObjectName(u"lineEdit_ssonumber")
        self.lineEdit_ssonumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_ssonumber, 2, 1, 1, 1)

        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_right, 4, 2, 1, 1)

        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_top, 0, 1, 1, 1)

        self.lineEdit_password = QLineEdit(self.page_1)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 6, 1, 1, 1)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_bottom, 13, 1, 1, 1)

        self.pushButton_register_1 = QPushButton(self.page_1)
        self.pushButton_register_1.setObjectName(u"pushButton_register_1")

        self.gridLayout.addWidget(self.pushButton_register_1, 12, 1, 1, 1)

        self.pushButton_login = QPushButton(self.page_1)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.gridLayout.addWidget(self.pushButton_login, 11, 1, 1, 1)

        self.horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_left, 4, 0, 1, 1)

        self.label_ssonumber = QLabel(self.page_1)
        self.label_ssonumber.setObjectName(u"label_ssonumber")
        self.label_ssonumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_ssonumber, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_top_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_top_2, 1, 1, 1, 1)

        self.label_ssonumber_registraton = QLabel(self.page_2)
        self.label_ssonumber_registraton.setObjectName(u"label_ssonumber_registraton")
        self.label_ssonumber_registraton.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_ssonumber_registraton, 2, 1, 1, 1)

        self.horizontalSpacer_left_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_left_2, 4, 0, 1, 1)

        self.label_password_registration = QLabel(self.page_2)
        self.label_password_registration.setObjectName(u"label_password_registration")
        self.label_password_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_password_registration, 4, 1, 1, 1)

        self.lineEdit_ssonumber_registration = QLineEdit(self.page_2)
        self.lineEdit_ssonumber_registration.setObjectName(u"lineEdit_ssonumber_registration")
        self.lineEdit_ssonumber_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_ssonumber_registration, 3, 1, 1, 1)

        self.verticalSpacer_bottom_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_bottom_2, 7, 1, 1, 1)

        self.horizontalSpacer_right_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_right_2, 4, 2, 1, 1)

        self.pushButton_register = QPushButton(self.page_2)
        self.pushButton_register.setObjectName(u"pushButton_register")

        self.gridLayout_4.addWidget(self.pushButton_register, 6, 1, 1, 1)

        self.lineEdit_password_registration = QLineEdit(self.page_2)
        self.lineEdit_password_registration.setObjectName(u"lineEdit_password_registration")
        self.lineEdit_password_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_password_registration, 5, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_go = QPushButton(self.page_3)
        self.pushButton_go.setObjectName(u"pushButton_go")

        self.gridLayout_3.addWidget(self.pushButton_go, 0, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.page_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_3.addWidget(self.textBrowser, 2, 0, 1, 2)

        self.lineEdit_link = QLineEdit(self.page_3)
        self.lineEdit_link.setObjectName(u"lineEdit_link")
        self.lineEdit_link.setEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_link, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 456, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_ssonumber, self.lineEdit_password)
        QWidget.setTabOrder(self.lineEdit_password, self.lineEdit_ssonumber_registration)
        QWidget.setTabOrder(self.lineEdit_ssonumber_registration, self.lineEdit_password_registration)
        QWidget.setTabOrder(self.lineEdit_password_registration, self.pushButton_register)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_message.setText("")
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.pushButton_register_1.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_ssonumber.setText(QCoreApplication.translate("MainWindow", u"SSO NUMBER", None))
        self.label_ssonumber_registraton.setText(QCoreApplication.translate("MainWindow", u"SSO NUMBER", None))
        self.label_password_registration.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.pushButton_go.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.lineEdit_link.setInputMask("")
        self.lineEdit_link.setText("")
        self.lineEdit_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste the link here", None))
    # retranslateUi

