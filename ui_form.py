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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout = QGridLayout(self.page_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_ssonumber = QLineEdit(self.page_1)
        self.lineEdit_ssonumber.setObjectName(u"lineEdit_ssonumber")

        self.gridLayout.addWidget(self.lineEdit_ssonumber, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_ssonumber = QLabel(self.page_1)
        self.label_ssonumber.setObjectName(u"label_ssonumber")

        self.gridLayout.addWidget(self.label_ssonumber, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_password = QLabel(self.page_1)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_password = QLineEdit(self.page_1)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_bottom, 7, 1, 1, 1)

        self.pushButton_login = QPushButton(self.page_1)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.gridLayout.addWidget(self.pushButton_login, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_right, 3, 2, 1, 1)

        self.horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_left, 3, 0, 1, 1)

        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_top, 0, 1, 1, 1)

        self.label_message = QLabel(self.page_1)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setFrameShadow(QFrame.Shadow.Plain)
        self.label_message.setTextFormat(Qt.TextFormat.AutoText)
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_message, 6, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_top_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_top_2, 0, 0, 1, 1)

        self.label_pastelink = QLabel(self.page_3)
        self.label_pastelink.setObjectName(u"label_pastelink")
        self.label_pastelink.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_pastelink, 1, 0, 1, 1)

        self.lineEdit_pastelink = QLineEdit(self.page_3)
        self.lineEdit_pastelink.setObjectName(u"lineEdit_pastelink")

        self.gridLayout_3.addWidget(self.lineEdit_pastelink, 2, 0, 1, 1)

        self.verticalSpacer_bottom_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_bottom_2, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 743, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_ssonumber.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_message.setText("")
        self.label_pastelink.setText(QCoreApplication.translate("MainWindow", u"Paste the link", None))
    # retranslateUi

