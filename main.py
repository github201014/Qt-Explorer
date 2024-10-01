import sys
from ctypes.wintypes import MSG

import win32con
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon, QCursor

from Shell import NativeWindow
from Shell.WebUnit import WebUnit


class EP(NativeWindow):
    tab_list: list[WebUnit]
    activeTab: WebUnit
    def __init__(self):
        super().__init__()
        self.tab_list = []
        self.setWindowIcon(QIcon("WindowPicture/icon.png"))
        w = WebUnit(QUrl("https://www.douyin.com/?ug_source=microsoft_mz03"))
        self.append(w)
        self.onActive(w)
        w.show()

    def append(self, webview: WebUnit):
        self.tab_list.append(webview)

    def onActive(self, a0: WebUnit):
        self.activeTab = a0
        self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + 10,
                                   self.width() - self.BORDER_WIDTH * 2,
                                   self.height() - self.title_height - self.BORDER_WIDTH - 10)
        self.activeTab.raise_()

    def closeEvent(self, event):
        sys.exit()

    def getActive(self):
        return self.activeTab

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if len(self.tab_list) >= 1:
            self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + 10,
                              self.width() - self.BORDER_WIDTH * 2,
                              self.height() - self.title_height - self.BORDER_WIDTH - 10)
        self.activeTab.raise_()

    def moveEvent(self, event):
        try:
            if len(self.tab_list) >= 1:
                self.activeTab.setGeometry(self.x() + self.BORDER_WIDTH, self.y() + self.title_height + 10,
                                  self.width() - self.BORDER_WIDTH * 2,
                                  self.height() - self.title_height - self.BORDER_WIDTH - 10)
                self.activeTab.raise_()
        except:
            pass

    def nativeEvent(self, eventType, message):
        msg = MSG.from_address(message.__int__())
        pos = QCursor.pos()
        x = pos.x() - self.frameGeometry().x()
        y = pos.y() - self.frameGeometry().y()
        if msg.message == win32con.WM_NCHITTEST:
            if (self.pos().y() <= QCursor.pos().y() <= self.pos().y() + self.title_height and
                    self.childAt(x,y) == self.titleBar):
                self.activeTab.raise_()
        return super().nativeEvent(eventType, message)



