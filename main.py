# Form implementation generated from reading ui file 'kold_launcher_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

from ui_main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui_main_window = Ui_MainWindow(self)
        self.ui_main_window.setupUi()
        self.offset = None
        self.ui_main_window.title.installEventFilter(self)

    def eventFilter(self, source, event):
        ## Window Move
        if source == self.ui_main_window.title:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.Type.MouseMove and self.offset is not None:
                # no need for complex computations: just use the offset to compute
                # "delta" position, and add that to the current one
                self.move(self.pos() - self.offset + event.pos())
                # return True to tell Qt that the event has been accepted and
                # should not be processed any further
                return True
            elif event.type() == QtCore.QEvent.Type.MouseButtonRelease:
                self.offset = None

        ##########################################################
        return super().eventFilter(source, event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_ = MainWindow()
    MainWindow_.show()
    sys.exit(app.exec())
