from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QWidget
from WebView import WebView
from Static.EnumClass import LanguageEnum

class WebUnit(QWidget):
    toTop = 45
    def __init__(self, args: QUrl):
        super().__init__(parent=None)
        self.web = WebView(self)
        self.web.setLanguage(LanguageEnum.zh_CN)
        self.web.load(args)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def resizeEvent(self, event):
        self.web.setGeometry(0, self.toTop, self.width(), self.height() - self.toTop)

    def load(self, url: QUrl):
        self.web.load(url)