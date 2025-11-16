from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,QFrame,
    QVBoxLayout, QWidget)
from debug_page2 import ColorChangingFrame
from debug_page2 import Ui_Form 
from tunableui import RobotControlPage


class DebugPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        # You can keep this initial resize, but the layouts will handle dynamic resizing.
        # It's good practice to allow the main window to be resizable by default.
        MainWindow.resize(1479, 959) 
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.central_layout = QVBoxLayout(self.centralwidget)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0) # No margins around the main content

        self.layoutWidget = QWidget(self.centralwidget) # Parent is centralwidget
        self.layoutWidget.setObjectName(u"layoutWidget")
        
        # self.layoutWidget.setGeometry(QRect(10, 10, 1461, 911)) 
        self.central_layout.addWidget(self.layoutWidget) # Add layoutWidget to central_layout

        self.horizontalLayout_main = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_main.setSpacing(5)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        
        self.menu_widget = QWidget(self.layoutWidget)
        self.menu_widget.setObjectName(u"menu_widget")
        # --- Set fixed width for the menu_widget ---
        self.menu_widget.setFixedWidth(211) # Enforces a fixed width of 211px
        self.menu_widget.setMaximumSize(QSize(230, 16777215)) 
        self.menu_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(13, -1, -1, -1)
        self.Nexa_icon_label = QLabel(self.menu_widget)
        self.Nexa_icon_label.setObjectName(u"Nexa_icon_label")
        self.Nexa_icon_label.setMaximumSize(QSize(40, 40))
        self.Nexa_icon_label.setPixmap(QPixmap(u":/icon/icon/exoskeleton (1).png"))
        self.Nexa_icon_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Nexa_icon_label)

        self.Nexa_Robot_label = QLabel(self.menu_widget)
        self.Nexa_Robot_label.setObjectName(u"Nexa_Robot_label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Nexa_Robot_label.setFont(font)
        self.Nexa_Robot_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Nexa_Robot_label)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.Connect_Button = QPushButton(self.menu_widget)
        self.Connect_Button.setObjectName(u"Connect_Button")
        self.Connect_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-45px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:none;\n"
"	border-radius:3px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/Group 22.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icon/icon/Group 20.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Connect_Button.setIcon(icon)
        self.Connect_Button.setIconSize(QSize(90, 60))
        self.Connect_Button.setCheckable(True)

        self.verticalLayout.addWidget(self.Connect_Button)

        self.lunch_Button = QPushButton(self.menu_widget)
        self.lunch_Button.setObjectName(u"lunch_Button")
        self.lunch_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-58px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:none;\n"
"	border-radius:3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/Group 23.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icon/icon/Group 21.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.lunch_Button.setIcon(icon1)
        self.lunch_Button.setIconSize(QSize(77, 60))
        self.lunch_Button.setCheckable(True)

        self.verticalLayout.addWidget(self.lunch_Button)

        self.configuratio_Button = QPushButton(self.menu_widget)
        self.configuratio_Button.setObjectName(u"configuratio_Button")
        self.configuratio_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-8px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/Group 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icon/icon/Group 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.configuratio_Button.setIcon(icon2)
        self.configuratio_Button.setIconSize(QSize(120, 60))
        self.configuratio_Button.setCheckable(True)
        self.configuratio_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.configuratio_Button)

        self.robot_control_Button = QPushButton(self.menu_widget)
        self.robot_control_Button.setObjectName(u"robot_control_Button")
        self.robot_control_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-8px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/Group 3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icon/icon/Group 4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.robot_control_Button.setIcon(icon3)
        self.robot_control_Button.setIconSize(QSize(124, 60))
        self.robot_control_Button.setCheckable(True)
        self.robot_control_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.robot_control_Button)

        self.debug_Button = QPushButton(self.menu_widget)
        self.debug_Button.setObjectName(u"debug_Button")
        self.debug_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/Group 19.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icon/icon/Group 18.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.debug_Button.setIcon(icon4)
        self.debug_Button.setIconSize(QSize(78, 60))
        self.debug_Button.setCheckable(True)
        self.debug_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.debug_Button)

        # self.stopWalking_Frame = QFrame(self.frame)
        # self.stopWalking_Frame.setObjectName(u"stopWalking_Frame")
        # self.stopWalking_Frame.setFrameShape(QFrame.Box)
        # self.stopWalking_Frame.setFrameShadow(QFrame.Plain)
        # self.stopWalking_Frame.setLineWidth(0)

        self.flag200_sensor = ColorChangingFrame()
        self.flag200_sensor.setObjectName(u"flag200_sensor")
        self.flag200_sensor.setFont(font)
        self.flag200_sensor.setFrameShape(QFrame.Box)
        self.flag200_sensor.setAlignment(Qt.AlignCenter)
        self.flag200_sensor.setWordWrap(True)
        self.flag200_sensor.setText("Left Motor")
        self.verticalLayout.addWidget(self.flag200_sensor)

        self.flag201_sensor = ColorChangingFrame()
        self.flag201_sensor.setObjectName(u"flag201_sensor")
        self.flag201_sensor.setFont(font)
        self.flag201_sensor.setFrameShape(QFrame.Box)
        self.flag201_sensor.setAlignment(Qt.AlignCenter)
        self.flag201_sensor.setWordWrap(True)
        self.flag201_sensor.setText("Right Motor")
        self.verticalLayout.addWidget(self.flag201_sensor)

        self.flag202_sensor = ColorChangingFrame()
        self.flag202_sensor.setObjectName(u"flag202_sensor")
        self.flag202_sensor.setFont(font)
        self.flag202_sensor.setFrameShape(QFrame.Box)
        self.flag202_sensor.setAlignment(Qt.AlignCenter)
        self.flag202_sensor.setWordWrap(True)
        self.flag202_sensor.setText("Left Encoder")
        self.verticalLayout.addWidget(self.flag202_sensor)

        self.flag203_sensor = ColorChangingFrame()
        self.flag203_sensor.setObjectName(u"flag203_sensor")
        self.flag203_sensor.setFont(font)
        self.flag203_sensor.setFrameShape(QFrame.Box)
        self.flag203_sensor.setAlignment(Qt.AlignCenter)
        self.flag203_sensor.setWordWrap(True)
        self.flag203_sensor.setText("Right Encoder")
        self.verticalLayout.addWidget(self.flag203_sensor)

        self.flag204_sensor = ColorChangingFrame()
        self.flag204_sensor.setObjectName(u"flag204_sensor")
        self.flag204_sensor.setFont(font)
        self.flag204_sensor.setFrameShape(QFrame.Box)
        self.flag204_sensor.setAlignment(Qt.AlignCenter)
        self.flag204_sensor.setWordWrap(True)
        self.flag204_sensor.setText("Left IMU")
        self.verticalLayout.addWidget(self.flag204_sensor)

        self.flag205_sensor = ColorChangingFrame()
        self.flag205_sensor.setObjectName(u"flag205_sensor")
        self.flag205_sensor.setFont(font)
        self.flag205_sensor.setFrameShape(QFrame.Box)
        self.flag205_sensor.setAlignment(Qt.AlignCenter)
        self.flag205_sensor.setWordWrap(True)
        self.flag205_sensor.setText("Right IMU")
        self.verticalLayout.addWidget(self.flag205_sensor)

        self.flag206_sensor = ColorChangingFrame()
        self.flag206_sensor.setObjectName(u"flag206_sensor")
        self.flag206_sensor.setFont(font)
        self.flag206_sensor.setFrameShape(QFrame.Box)
        self.flag206_sensor.setAlignment(Qt.AlignCenter)
        self.flag206_sensor.setWordWrap(True)
        self.flag206_sensor.setText("Left FSR")
        self.verticalLayout.addWidget(self.flag206_sensor)

        self.flag207_sensor = ColorChangingFrame()
        self.flag207_sensor.setObjectName(u"flag207_sensor")
        self.flag207_sensor.setFont(font)
        self.flag207_sensor.setFrameShape(QFrame.Box)
        self.flag207_sensor.setAlignment(Qt.AlignCenter)
        self.flag207_sensor.setWordWrap(True)
        self.flag207_sensor.setText("Right FSR")
        self.verticalLayout.addWidget(self.flag207_sensor)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 351, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.User_label = QLabel(self.menu_widget)
        self.User_label.setObjectName(u"User_label")
        self.User_label.setMinimumSize(QSize(0, 18))
        self.User_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.User_label)

        self.Mode_label = QLabel(self.menu_widget)
        self.Mode_label.setObjectName(u"Mode_label")
        self.Mode_label.setMinimumSize(QSize(18, 18))
        self.Mode_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Mode_label)

        self.exit_Button = QPushButton(self.menu_widget)
        self.exit_Button.setObjectName(u"exit_Button")

        self.exit_Button.setStyleSheet(u"QPushButton {\n"
"	padding-left:-55px;\n"
"   background-color: transparent; /* Default background for the button */\n"
"   border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white; /* Semi-transparent white when checked */\n"
"	border-radius:3px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/Group 7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        icon5.addFile(u":/icon/icon/Group 8.png", QSize(), QIcon.Mode.Normal, QIcon.State.On) # Corrected path if it's a resource
        self.exit_Button.setIcon(icon5)
        self.exit_Button.setIconSize(QSize(60, 30))
        self.exit_Button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.exit_Button)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_main.addWidget(self.menu_widget)

        # --- Directly use self.stackedWidget and allow it to expand ---
        self.stackedWidget = QStackedWidget(self.layoutWidget) # Parent is layoutWidget for proper layout management
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Ensure it expands
        self.horizontalLayout_main.addWidget(self.stackedWidget)
        
        # --- Pages are now added directly to the main stackedWidget ---
        # IMPORTANT: Ensure your custom page classes (DebugPage, ConfigPage, RobotControlPage)
        # are correctly defined in their respective files and can be imported.
       # در متد setupUi از کلاس Ui_MainWindow در menubar.py
        # ...
        # self.page_config_instance = ConfigPage()
        self.page_robot_control_instance = RobotControlPage()
        self.page_debug_instance = DebugPage()

        # این خطوط جدید هستند که مشکل را حل می کنند:
        # MainWindow.page_config = self.page_config_instance
        MainWindow.page_robot_control = self.page_robot_control_instance
        MainWindow.page_debug = self.page_debug_instance
        # ...
        # self.stackedWidget.addWidget(self.page_config_instance)
        self.stackedWidget.addWidget(self.page_robot_control_instance)
        self.stackedWidget.addWidget(self.page_debug_instance)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0) # Set initial page (e.g., ConfigPage)

        QMetaObject.connectSlotsByName(MainWindow)

        # --- Connect buttons to switch stacked widget pages ---
        # Connect buttons to change the current index of the stacked widget
        # self.configuratio_Button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.robot_control_Button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.debug_Button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Nexa_icon_label.setText("")
        self.Nexa_Robot_label.setText(QCoreApplication.translate("MainWindow", u"Nexa Robot", None))
        self.Connect_Button.setText("")
        self.lunch_Button.setText("")
        self.configuratio_Button.setText("")
        self.robot_control_Button.setText("")
        self.debug_Button.setText("")
        self.User_label.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.Mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.exit_Button.setText("")

    # retranslateUi