from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QWidget
from Static.EnumClass import LanguageEnum
from Static.language import zh_CN


class WebView(QWebEngineView):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)

    def setLanguage(self, language: LanguageEnum):
        if language == LanguageEnum.zh_CN:
            zh_CN(self)


    def createWindow(self, _type: QWebEnginePage.WebWindowType):
        if _type == QWebEnginePage.WebWindowType.WebBrowserWindow:...
        elif _type == QWebEnginePage.WebWindowType.WebDialog:...
        elif _type == QWebEnginePage.WebWindowType.WebBrowserTab:...
        elif _type == QWebEnginePage.WebWindowType.WebBrowserBackgroundTab:...