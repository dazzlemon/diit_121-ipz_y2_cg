from PyQt5 import QtWidgets, QtCore, QtGui
from forms_py import *

class Cg1:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.mainWindow)
        self.widget = None
        self.uiWidget = None
        
        def settings_clicked():
            markVariants = [
                "Square",
                "Triangle",
                "Circle"
            ]
            open_widget(Ui_SettingsWindow())
            self.uiWidget.marksStyleComboBox.addItems(markVariants)
        
        def plot_clicked(): open_widget(Ui_PlotWindow()) 
        def clear_clicked(): print("clear pressed")
        def close(event): self.widget and self.widget.close()
        def open_widget(uiWidget):
            def widget_closed(event):
                self.widget = None
                self.uiWidget = None

            if self.widget == None:
                self.widget = QtWidgets.QWidget()
                self.uiWidget = uiWidget
                self.uiWidget.setupUi(self.widget)
                self.widget.closeEvent = widget_closed
                self.widget.show() 

        self.mainUi.settingsButton.clicked.connect(settings_clicked)
        self.mainUi.plotButton.clicked.connect(plot_clicked)
        self.mainUi.clearButton.clicked.connect(clear_clicked)
        self.mainWindow.closeEvent = close 
 
        self.scene = QtWidgets.QGraphicsScene()
        self.mainUi.canvas.setScene(self.scene)
        self.mainUi.canvas.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        
        def draw(event):
            x = self.mainUi.canvas.width()
            y = self.mainUi.canvas.height()

            self.scene.setSceneRect(0, 0, x, y)
            self.mainUi.canvas.fitInView(self.scene.sceneRect(), QtCore.Qt.IgnoreAspectRatio)#still leaves some gaps on sides, seems like a bug

            self.scene.clear()

            self.scene.addLine(QtCore.QLineF(0, 0, x, y))
            self.scene.addLine(QtCore.QLineF(0, y, x, 0))
            self.scene.update()

        self.mainUi.canvas.resizeEvent = draw
    

    def run(self):
        self.mainWindow.show()


if __name__ == "__main__":
    import sys
    main_ = QtWidgets.QApplication(sys.argv)
    app = Cg1()
    app.run()
    sys.exit(main_.exec_())
