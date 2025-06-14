# -*- coding: utf-8 -*-
import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

from ui_form import Ui_MainWindow  # Make sure this is generated from form.ui

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.credentials = {"admin": "password"}
        self.logged_in = False

        # Replace QTextBrowser with QWebEngineView for embedded browser
        self.browser = QWebEngineView()
        self.ui.gridLayout_3.replaceWidget(self.ui.textBrowser, self.browser)
        self.ui.textBrowser.deleteLater()
        self.ui.textBrowser = None  # Optional cleanup

        # Button connections
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.pushButton_register.clicked.connect(self.register)
        self.ui.pushButton_register_1.clicked.connect(self.show_register_page)
        self.ui.pushButton_go.clicked.connect(self.display_link_text)

        # Menu setup
        self.menuBACK = self.ui.menubar.addMenu("MENU")
        self.actionBack = self.menuBACK.addAction("Go Back")
        self.actionBack.triggered.connect(self.go_back)

        # Page change signal
        self.ui.stackedWidget.currentChanged.connect(self.handle_page_change)

    def login(self):
        sso_id = self.ui.lineEdit_ssonumber.text()
        password = self.ui.lineEdit_password.text()
        self.ui.lineEdit_ssonumber.clear()
        self.ui.lineEdit_password.clear()

        if sso_id in self.credentials:
            if self.credentials[sso_id] == password:
                self.ui.label_message.setText("Login successful!")
                self.logged_in = True
                self.ui.stackedWidget.setCurrentIndex(2)
            else:
                self.ui.label_message.setText("Incorrect password!")
        else:
            self.ui.label_message.setText("SSO number not found! Please register.")
            self.ui.stackedWidget.setCurrentIndex(1)

    def register(self):
        sso_id = self.ui.lineEdit_ssonumber_registration.text()
        password = self.ui.lineEdit_password_registration.text()

        if sso_id and password:
            if sso_id in self.credentials:
                self.ui.label_message.setText("User already exists. Please log in.")
                self.ui.stackedWidget.setCurrentIndex(0)
            else:
                self.credentials[sso_id] = password
                self.ui.lineEdit_ssonumber_registration.clear()
                self.ui.lineEdit_password_registration.clear()
                self.ui.label_message.setText("Registration successful! Please log in.")
                self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.label_message.setText("Please enter both SSO number and password.")

    def show_register_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_back(self):
        self.ui.label_message.clear()
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index <= 0:
            self.ui.label_message.setText("Cannot go back from here.")
        elif current_index == 2:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)



    def handle_page_change(self, index):
        if self.logged_in:
            self.menuBACK.menuAction().setVisible(True)
        else:
            self.menuBACK.menuAction().setVisible(index != 0)

    def display_link_text(self):
        url = self.ui.lineEdit_link.text().strip()
        if url:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
            self.browser.load(QUrl(url))
        else:
            self.browser.setHtml("<h3>No link entered.</h3>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
