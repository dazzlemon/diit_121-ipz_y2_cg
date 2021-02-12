"""
MAIN
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_py import Ui_MainWindow

class Cg2(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._mainWindow = QMainWindow()
        self._mainUi = Ui_MainWindow()
        self._mainUi.setupUi(self._mainWindow)


    def exec_(self):
        self._mainWindow.show()
        QApplication.exec_()


if __name__ == '__main__':
    import sys
    app = Cg2(sys.argv)
    sys.exit(app.exec_())
