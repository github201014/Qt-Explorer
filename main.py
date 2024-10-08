import sys
from ctypes.wintypes import MSG
import win32con
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QTextEdit
from Shell import NativeWindow
from Static.EnumClass import LanguageEnum, StatusEnum
from Static.language import zh_CN



class WebBar(QWidget):
    def __init__(self, parent: QWidget, border_left: int = 50,
                 border_up: int = 5):
        super().__init__()
        self.pa = parent
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.edit = QTextEdit(self)
        self.edit.setGeometry(border_left,
                              border_up,
                              self.edit.width() - 2 * border_left,
                              self.edit.height() - 2 * border_up)
class WebUnit(QWidget):
    toTop = 0
    def __init__(self, args: QUrl, parent: QWidget):
        super().__init__(parent=None)
        self.web = WebView(self)
        self.web.setLanguage(LanguageEnum.zh_CN)
        self.web.load(args)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.pa = parent

    def closeEvent(self, event):
        self.pa.close()

    def resizeEvent(self, event):
        self.web.setGeometry(0, self.toTop, self.width(), self.height() - self.toTop)

    def load(self, url: QUrl):
        self.web.load(url)

    def nativeEvent(self, eventType, message):
        msg = MSG.from_address(message.__int__())
        if msg.message == win32con.WM_LBUTTONDOWN:
            if self == self.pa.activeTab:
                self.pa.raise_()
                self.raise_()
        return super().nativeEvent(eventType, message)
class WebView(QWebEngineView):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)

    def setLanguage(self, language: LanguageEnum):
        if language == LanguageEnum.zh_CN:
            zh_CN(self)

    def createWindow(self, _type: QWebEnginePage.WebWindowType):
        if _type == QWebEnginePage.WebWindowType.WebBrowserWindow:
            self.window1 = EP()
            self.window1.show()
            return self.window1.activeTab.web
        elif _type == QWebEnginePage.WebWindowType.WebDialog:
            ...
        elif _type == QWebEnginePage.WebWindowType.WebBrowserTab:
            ...
        elif _type == QWebEnginePage.WebWindowType.WebBrowserBackgroundTab:
            ...
class EP(NativeWindow):
    toUp = 45
    tab_list: list[WebUnit]
    activeTab: WebUnit
    status: StatusEnum
    def __init__(self, url: str = None):
        W_LIST.append(self)
        super().__init__()
        print(W_LIST)
        self.tab_list = []
        self.setWindowIcon(QIcon("WindowPicture/icon.png"))
        if url is not None: w = WebUnit(QUrl(url), self)
        else: w = WebUnit(QUrl("https://www.baidu.com"), self)
        self.setMinimumSize(500, self.title_height + self.toUp + 6)
        self.resize(800,700)
        self.append(w)
        self.onActive(w)
        self.status = StatusEnum.MAIN_NO_WINDOW_YES
        w.show()

    def append(self, webview: WebUnit):
        self.tab_list.append(webview)

    def onActive(self, a0: WebUnit):
        self.activeTab = a0
        self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + self.toUp,
                                   self.width() - self.BORDER_WIDTH * 2,
                                   self.height() - self.title_height - self.BORDER_WIDTH - self.toUp)
        self.activeTab.raise_()

    def closeEvent(self, event):
        for i in self.tab_list:
            i.close()

    def showMinimized(self):
        self.activeTab.setGeometry(-10,-10,5,5)
        super().showMinimized()


    def show(self):
        super().show()
        self.activeTab.show()
        self.raise_()

    def getActive(self):
        return self.activeTab

    def activateWindow(self):
        self.activeTab.activateWindow()
        super().activateWindow()


    def raise_(self):
        a = W_LIST[:]
        a.remove(self)
        for i in a:
            if i.isActiveWindow() or i.activeTab.isActiveWindow():
                self.activateWindow()
        if not self.isActiveWindow() and not self.activeTab.isActiveWindow():
            self.status = StatusEnum.MAIN_NO_WINDOW_NO
            return
        elif self.status == StatusEnum.MAIN_NO_WINDOW_YES:
            self.activateWindow()
            self.status = StatusEnum.MAIN_YES_WINDOW_YES
        elif self.status == StatusEnum.MAIN_YES_WINDOW_YES:
            self.activeTab.raise_()
        elif self.status == StatusEnum.MAIN_NO_WINDOW_NO:...

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if len(self.tab_list) >= 1:
            self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + self.toUp,
                              self.width() - self.BORDER_WIDTH * 2,
                              self.height() - self.title_height - self.BORDER_WIDTH - self.toUp)
        self.raise_()

    def moveEvent(self, event):
        try:
            if len(self.tab_list) >= 1:
                self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + self.toUp,
                                  self.width() - self.BORDER_WIDTH * 2,
                                  self.height() - self.title_height - self.BORDER_WIDTH - self.toUp)
                self.raise_()
        except:
            pass

    def mousePressEvent(self, event):
        self.raise_()

    def mouseReleaseEvent(self, event):
        self.raise_()

global W_LIST
W_LIST: list[EP] = []









