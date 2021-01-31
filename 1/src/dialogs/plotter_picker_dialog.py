from PyQt5 import QtWidgets
from forms_py import Ui_SettingsWindow

class PlotterPickerDialog:
    def __init__(self, closeEvent, parent):
        self.widget = QtWidgets.QWidget()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self.widget)
        self.widget.closeEvent = closeEvent

        self.ui.axesWidthSpinBox.setValue(parent._plotter.axesWidth)

        self.parent = parent
        
        markVariants = [
            "Square",
            "Triangle",
            "Circle"
        ]

        self.ui.marksStyleComboBox.addItems(markVariants)

        def axes_color_clicked():
            colorDialog = QtWidgets.QColorDialog()
            newColor = colorDialog.getColor(self.parent._plotter.axesColor)
            if newColor.isValid():
                self.parent._plotter.axesColor = newColor
                self.parent.plot()
            
        def bg_color_clicked():
            colorDialog = QtWidgets.QColorDialog()
            newColor = colorDialog.getColor(self.parent._plotter.bgColor)
            if newColor.isValid():
                self.parent._plotter.bgColor = newColor
                parent.plot()
        
        def axes_width_changed(val):
            parent._plotter.axesWidth = val
            parent.plot()

        self.ui.axesColorButton.clicked.connect(axes_color_clicked)
        self.ui.bgColorButton.clicked.connect(bg_color_clicked)
        self.ui.axesWidthSpinBox.valueChanged.connect(axes_width_changed)


    def show(self):
        self.widget.show()
    

    def close(self):
        self.widget.close()
