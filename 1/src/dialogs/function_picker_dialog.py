from PyQt5.QtWidgets import QWidget, QGraphicsScene, QColorDialog
from PyQt5.QtGui import QColor, QPen, QBrush, QColorConstants
from PyQt5.QtCore import QRectF, Qt
from forms_py import Ui_PlotWindow
from plotter import PlottableFunction
from math import cos

class FunctionPickerDialog:
    def __init__(self, closeEvent, parent):
        self.widget = QWidget()
        self.ui = Ui_PlotWindow()
        self.ui.setupUi(self.widget)
        self.widget.closeEvent = closeEvent

        self._init_color_view()

        self.parent = parent
        self._new_function()

        styleVariants = [
            "Normal",
            "Dotted"
        ]
        self.ui.funcStyleComboBox.addItems(styleVariants)

        def plot_clicked():
            self._function.rangeX = (
                self.ui.xMinDoubleSpinBox.value(),
                self.ui.xMaxDoubleSpinBox.value()
            )

            a = self.ui.aDoubleSpinBox.value()
            b = self.ui.bDoubleSpinBox.value()
            self._function.f = lambda x: abs(x) + a * cos(b * x)
            self._function.width = self.ui.widthSpinBox.value()

            if self.ui.funcStyleComboBox.currentIndex() == 0:
                self._function.style = PlottableFunction.Style.NORMAL
            else:
                self._function.style = PlottableFunction.Style.DOTTED
                
            self.parent._funcs.append(self._function)
            self._new_function()

            self.parent.plot()

        def color_clicked():
            colorDialog = QColorDialog()
            newColor = colorDialog.getColor(self._function.color)
            if newColor.isValid():
                self._function.color = newColor
                self._color_changed()

        self.ui.plotButton.clicked.connect(plot_clicked)
        self.ui.colorButton.clicked.connect(color_clicked)


    def _new_function(self):
        self._function = PlottableFunction(QColor(0, 0, 0), 4, (-3, 3), lambda x: abs(x) + 2 * cos(-x))
        self._color_changed()
    

    def show(self):
        self.widget.show()

    
    def close(self):
        self.widget.close()


    def _color_changed(self):
        pen = QPen()
        brush = QBrush(self._function.color)

        self._colorScene.addRect(self._colorScene.sceneRect(), pen, brush)
        self._colorScene.update()


    def _init_color_view(self):
        self._colorScene = QGraphicsScene()
        self.ui.colorView.setScene(self._colorScene)
        self.ui.colorView.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        x = self.ui.colorView.width()
        y = self.ui.colorView.height()
        self.ui.colorView.setFixedSize(x, y)
        self._colorScene.setSceneRect(0, 0, x, y)
        self.ui.colorView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.colorView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
