from PyQt5 import QtWidgets
from forms_py import Ui_SettingsWindow
from plotter import Plotter

class PlotterPickerDialog:
    def __init__(self, closeEvent, parent):
        self.widget = QtWidgets.QWidget()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self.widget)
        self.widget.closeEvent = closeEvent

        self.ui.axesWidthSpinBox.setValue(parent._plotter.axesWidth)
        self.ui.marksSizeSpinBox.setValue(parent._plotter.marksSize)
        self.ui.textSizeSpinBox.setValue(parent._plotter.textSize)
        self.ui.markupSizeSpinBox.setValue(parent._plotter.markupSize)
        self.ui.markupCheckBox.setChecked(parent._plotter.markupOn)

        self.parent = parent
        
        markVariants = [
            "Square",
            "Circle"
        ]

        self.ui.marksStyleComboBox.addItems(markVariants)

        if self.parent._plotter.marksStyle == Plotter.MarksStyle.SQUARE:
            idx = 0
        elif self.parent._plotter.marksStyle == Plotter.MarksStyle.CIRCLE:
            idx = 1
        self.ui.marksStyleComboBox.setCurrentIndex(idx)

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

        def marks_color_clicked():
            colorDialog = QtWidgets.QColorDialog()
            newColor = colorDialog.getColor(self.parent._plotter.marksColor)
            if newColor.isValid():
                self.parent._plotter.marksColor = newColor
                parent.plot()

        def marks_size_changed(val):
            parent._plotter.marksSize = val
            parent.plot()

        def marks_style_changed(val):
            if val == 0:
                style = Plotter.MarksStyle.SQUARE
            elif val == 1:
                style = Plotter.MarksStyle.CIRCLE
            self.parent._plotter.marksStyle = style
            parent.plot()

        def text_color_clicked():
            colorDialog = QtWidgets.QColorDialog()
            newColor = colorDialog.getColor(self.parent._plotter.textColor)
            if newColor.isValid():
                self.parent._plotter.textColor = newColor
                parent.plot()

        def text_size_changed(val):
            parent._plotter.textSize = val
            parent.plot()

        def markup_size_changed(val):
            parent._plotter.markupSize = val
            parent.plot()

        def markup_color_clicked():
            colorDialog = QtWidgets.QColorDialog()
            newColor = colorDialog.getColor(self.parent._plotter.markupColor)
            if newColor.isValid():
                self.parent._plotter.markupColor = newColor
                parent.plot()

        def markup_toggled(val):
            parent._plotter.markupOn = val
            parent.plot()

        self.ui.axesColorButton.clicked.connect(axes_color_clicked)
        self.ui.bgColorButton.clicked.connect(bg_color_clicked)
        self.ui.axesWidthSpinBox.valueChanged.connect(axes_width_changed)
        self.ui.marksColorButton.clicked.connect(marks_color_clicked)
        self.ui.marksSizeSpinBox.valueChanged.connect(marks_size_changed)
        self.ui.marksStyleComboBox.currentIndexChanged.connect(marks_style_changed)
        self.ui.textSizeSpinBox.valueChanged.connect(text_size_changed)
        self.ui.textColorButton.clicked.connect(text_color_clicked)
        self.ui.markupColorButton.clicked.connect(markup_color_clicked)
        self.ui.markupSizeSpinBox.valueChanged.connect(markup_size_changed)
        self.ui.markupCheckBox.stateChanged.connect(markup_toggled)


    def show(self):
        self.widget.show()
    

    def close(self):
        self.widget.close()
