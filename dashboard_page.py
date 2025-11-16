from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QFrame,QPushButton
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QIcon

class ColorChangingFrame(QFrame):
    def __init__(self, label_text):
        super().__init__()
        self.label = QLabel(label_text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMinimumHeight(100)
        self.setStyleSheet("font-size: 18px;")

        self.flag = False
        self.update_color()

    def update_color(self):
        if self.flag == 1:
            self.setStyleSheet("background-color: lightgreen;")
        else:
            self.setStyleSheet("background-color: lightcoral;")

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create layout
        self.DashboardLayout = QVBoxLayout()
    
        self.FlagLabel1 = ColorChangingFrame("Flag 1")
        self.FlagLabel1.setObjectName("1FlagLabel")
        self.DashboardLayout.addWidget(self.FlagLabel1)

        self.FlagLabel2 = ColorChangingFrame("Flag 2")
        self.FlagLabel2.setObjectName("2FlagLabel")
        self.DashboardLayout.addWidget(self.FlagLabel2)

        self.FlagLabel3 = ColorChangingFrame("Flag 3")
        self.FlagLabel3.setObjectName("1FlagLabel")
        self.DashboardLayout.addWidget(self.FlagLabel3)

        self.FlagLabel4 = ColorChangingFrame("Flag 4")
        self.FlagLabel4.setObjectName("4FlagLabel")
        self.DashboardLayout.addWidget(self.FlagLabel4)

        self.setLayout(self.DashboardLayout)

    