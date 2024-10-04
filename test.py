from main import EP
from PySide6.QtWidgets import QApplication
app = QApplication([])
w = EP("https://www.woaimoon.net/")
w.show()
app.exec()