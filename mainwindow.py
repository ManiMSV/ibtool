# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from ui_form import Ui_MainWindow
from database import init_db, register_user, validate_user

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        init_db()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.web_view = QWebEngineView()
        layout = self.ui.page_3.layout()
        layout.replaceWidget(self.ui.textBrowser, self.web_view)
        self.ui.textBrowser.deleteLater()
        self.ui.pushButton_go.clicked.connect(self.display_link)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.pushButton_register.clicked.connect(self.register)
        self.ui.pushButton_register_1.clicked.connect(self.show_register_page)
        self.menuBACK = self.ui.menubar.addMenu("MENU")
        self.actionBack = self.menuBACK.addAction("Go Back")
        self.actionBack.triggered.connect(self.go_back)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.logged_in = False

    def login(self):
        sso_id = self.ui.lineEdit_ssonumber.text().strip()
        password = self.ui.lineEdit_password.text().strip()
        self.ui.lineEdit_ssonumber.clear()
        self.ui.lineEdit_password.clear()

        if validate_user(sso_id, password):
            self.ui.label_message.setText("Login successful!")
            self.logged_in = True
            self.ui.stackedWidget.setCurrentIndex(2)
        else:
            self.ui.label_message.setText("Invalid SSO or password.")

    def register(self):
        sso_id = self.ui.lineEdit_ssonumber_registration.text().strip()
        password = self.ui.lineEdit_password_registration.text().strip()

        if not sso_id or not password:
            self.ui.label_message.setText("Enter both SSO and password.")
            return

        if register_user(sso_id, password):
            self.ui.label_message.setText("Registration successful! Please log in.")
            self.ui.lineEdit_ssonumber_registration.clear()
            self.ui.lineEdit_password_registration.clear()
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.label_message.setText("User already exists. Please log in.")
            self.ui.stackedWidget.setCurrentIndex(0)

    def show_register_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_back(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if self.logged_in and current_index == 2:
            self.ui.label_message.setText("You are already logged in.")
            return
        if current_index > 0:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)

    def display_link(self):
        url_text = self.ui.lineEdit_link.text().strip()
        if not url_text:
            return
        if not url_text.startswith("http"):
            url_text = "http://" + url_text
        self.web_view.load(QUrl(url_text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
