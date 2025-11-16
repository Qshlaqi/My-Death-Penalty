from PySide6.QtWidgets import QMainWindow, QMenu, QMessageBox, QApplication, QFrame
from PySide6.QtGui import QAction, QIcon # Added QIcon for completeness (if you want to customize dialog icon)
from PySide6.QtCore import QCoreApplication,Qt
from menubar import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Nexa')
        self.showMaximized()
        
        # Connect the exit button to the exit_app method
        self.exit_Button.clicked.connect(self.exit_app)

################################################ Exit Message box #####################################
    def exit_app(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.quit()
        else:
            self.exit_Button.setChecked(False) #
#######################################################################################################

