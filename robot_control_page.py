from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class RobotControlPage(QWidget):
    def __init__(self):
        super().__init__()

        self.horizontalLayout_45 = QHBoxLayout(self)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_10)

        self.User_SignUp_frame = QFrame(self.frame)
        self.User_SignUp_frame.setObjectName(u"User_SignUp_frame")
        self.User_SignUp_frame.setFrameShape(QFrame.Box)
        self.User_SignUp_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.User_SignUp_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.User_Sign_Up_label = QLabel(self.User_SignUp_frame)
        self.User_Sign_Up_label.setObjectName(u"User_Sign_Up_label")
        self.User_Sign_Up_label.setMinimumSize(QSize(0, 18))
        self.User_Sign_Up_label.setMaximumSize(QSize(16777215, 18))
        self.User_Sign_Up_label.setStyleSheet(u"")
        self.User_Sign_Up_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.User_Sign_Up_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.user_ID_signup_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.user_ID_signup_lineEdit.setObjectName(u"user_ID_signup_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_ID_signup_lineEdit.sizePolicy().hasHeightForWidth())
        self.user_ID_signup_lineEdit.setSizePolicy(sizePolicy)
        self.user_ID_signup_lineEdit.setMinimumSize(QSize(80, 30))
        self.user_ID_signup_lineEdit.setMaximumSize(QSize(80, 30))
        self.user_ID_signup_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.user_ID_signup_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.user_ID_signup_lineEdit)

        self.Name_and_LastName_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.Name_and_LastName_lineEdit.setObjectName(u"Name_and_LastName_lineEdit")
        sizePolicy.setHeightForWidth(self.Name_and_LastName_lineEdit.sizePolicy().hasHeightForWidth())
        self.Name_and_LastName_lineEdit.setSizePolicy(sizePolicy)
        self.Name_and_LastName_lineEdit.setMinimumSize(QSize(0, 30))
        self.Name_and_LastName_lineEdit.setMaximumSize(QSize(500, 30))
        self.Name_and_LastName_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.Name_and_LastName_lineEdit)

        self.add_user_Button = QPushButton(self.User_SignUp_frame)
        self.add_user_Button.setObjectName(u"add_user_Button")
        self.add_user_Button.setMinimumSize(QSize(140, 30))
        self.add_user_Button.setMaximumSize(QSize(140, 30))
        self.add_user_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_user_Button.setStyleSheet(u"#add_user_Button {\n"
"background-color: rgba(107, 245, 155, 1);\n"
"font-weight :800;\n"
"border-radius:10px;\n"
"}\n"
"#add_user_Button:hover{\n"
"background-color: rgba(107, 245, 155, 1);\n"
"font-weight :800;\n"
"border-radius:10px;\n"
"}\n"
"#add_user_Button:pressed{\n"
"background-color: rgba(76, 150, 61, 1);\n"
"font-weight :800;\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.add_user_Button)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox = QComboBox(self.User_SignUp_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 30))
        self.comboBox.setEditable(False)

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.Age_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.Age_lineEdit.setObjectName(u"Age_lineEdit")
        sizePolicy.setHeightForWidth(self.Age_lineEdit.sizePolicy().hasHeightForWidth())
        self.Age_lineEdit.setSizePolicy(sizePolicy)
        self.Age_lineEdit.setMinimumSize(QSize(0, 30))
        self.Age_lineEdit.setMaximumSize(QSize(500, 30))
        self.Age_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Age_lineEdit)

        self.Height_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.Height_lineEdit.setObjectName(u"Height_lineEdit")
        sizePolicy.setHeightForWidth(self.Height_lineEdit.sizePolicy().hasHeightForWidth())
        self.Height_lineEdit.setSizePolicy(sizePolicy)
        self.Height_lineEdit.setMinimumSize(QSize(0, 30))
        self.Height_lineEdit.setMaximumSize(QSize(500, 30))
        self.Height_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Height_lineEdit)

        self.Weight_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.Weight_lineEdit.setObjectName(u"Weight_lineEdit")
        sizePolicy.setHeightForWidth(self.Weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.Weight_lineEdit.setSizePolicy(sizePolicy)
        self.Weight_lineEdit.setMinimumSize(QSize(0, 30))
        self.Weight_lineEdit.setMaximumSize(QSize(500, 30))
        self.Weight_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.Weight_lineEdit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.User_Login_verticalLayout = QVBoxLayout()
        self.User_Login_verticalLayout.setObjectName(u"User_Login_verticalLayout")
        self.User_Login_label = QLabel(self.User_SignUp_frame)
        self.User_Login_label.setObjectName(u"User_Login_label")
        self.User_Login_label.setMaximumSize(QSize(16777215, 18))
        self.User_Login_label.setStyleSheet(u"")
        self.User_Login_label.setAlignment(Qt.AlignCenter)

        self.User_Login_verticalLayout.addWidget(self.User_Login_label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.user_ID_login_lineEdit = QLineEdit(self.User_SignUp_frame)
        self.user_ID_login_lineEdit.setObjectName(u"user_ID_login_lineEdit")
        sizePolicy.setHeightForWidth(self.user_ID_login_lineEdit.sizePolicy().hasHeightForWidth())
        self.user_ID_login_lineEdit.setSizePolicy(sizePolicy)
        self.user_ID_login_lineEdit.setMinimumSize(QSize(0, 0))
        self.user_ID_login_lineEdit.setMaximumSize(QSize(500, 30))
        self.user_ID_login_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.user_ID_login_lineEdit)

        self.Sign_In_Button = QPushButton(self.User_SignUp_frame)
        self.Sign_In_Button.setObjectName(u"Sign_In_Button")
        self.Sign_In_Button.setMinimumSize(QSize(0, 30))
        self.Sign_In_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Sign_In_Button.setStyleSheet(u"#Sign_In_Button {\n"
"background-color:rgba(99, 144, 248, 1);\n"
"font-weight :800;\n"
"border-radius:10px;\n"
"}\n"
"#Sign_In_Button:hover{\n"
"background-color:rgba(99, 144, 248, 1);\n"
"font-weight :800;\n"
"border-radius:10px;\n"
"}\n"
"#Sign_In_Button:pressed{\n"
"background-color: rgba(82, 120, 208, 1);\n"
"font-weight :800;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.Sign_In_Button)


        self.User_Login_verticalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addLayout(self.User_Login_verticalLayout)

        self.pushButton = QPushButton(self.User_SignUp_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_13.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.User_SignUp_frame)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Automatic_Mode_Button = QPushButton(self.groupBox)
        self.Automatic_Mode_Button.setObjectName(u"Automatic_Mode_Button")
        self.Automatic_Mode_Button.setMinimumSize(QSize(52, 39))
        font = QFont()
        self.Automatic_Mode_Button.setFont(font)
        self.Automatic_Mode_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Automatic_Mode_Button.setStyleSheet(u"#Automatic_Mode_Button{\n"
"background-color:rgba(63, 81, 181, 1);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"#Automatic_Mode_Button:hover{\n"
"background-color: rgba(121, 134, 203, 1);\n"
"border-radius:10px;\n"
"}\n"
"#Automatic_Mode_Button:checked{\n"
"background-color: rgba(0, 188, 212, 1);\n"
"font-weight :800;\n"
"}\n"
"")
        self.Automatic_Mode_Button.setCheckable(True)
        self.Automatic_Mode_Button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.Automatic_Mode_Button)

        self.Squat_Mode_Button = QPushButton(self.groupBox)
        self.Squat_Mode_Button.setObjectName(u"Squat_Mode_Button")
        self.Squat_Mode_Button.setMinimumSize(QSize(52, 39))
        self.Squat_Mode_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Squat_Mode_Button.setStyleSheet(u"#Squat_Mode_Button{\n"
"background-color:rgba(63, 81, 181, 1);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"#Squat_Mode_Button:hover{\n"
"background-color: rgba(121, 134, 203, 1);\n"
"border-radius:10px;\n"
"}\n"
"#Squat_Mode_Button:checked{\n"
"background-color: rgba(0, 188, 212, 1);\n"
"font-weight :800;\n"
"}\n"
"")
        self.Squat_Mode_Button.setCheckable(True)
        self.Squat_Mode_Button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.Squat_Mode_Button)

        self.Stand2Sit_and_Sit2Stand_Mode_Button = QPushButton(self.groupBox)
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setObjectName(u"Stand2Sit_and_Sit2Stand_Mode_Button")
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setMinimumSize(QSize(52, 39))
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setStyleSheet(u"#Stand2Sit_and_Sit2Stand_Mode_Button {\n"
"background-color: rgba(63, 81, 181, 1);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"#Stand2Sit_and_Sit2Stand_Mode_Button:hover {\n"
"background-color: rgba(121, 134, 203, 1);\n"
"border-radius:10px;\n"
"}\n"
"#Stand2Sit_and_Sit2Stand_Mode_Button:checked{\n"
"background-color: rgba(0, 188, 212, 1);\n"
"font-weight :800;\n"
"}\n"
"")
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setCheckable(True)
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.Stand2Sit_and_Sit2Stand_Mode_Button)

        self.zeroTorque_Mode_Button = QPushButton(self.groupBox)
        self.zeroTorque_Mode_Button.setObjectName(u"zeroTorque_Mode_Button")
        self.zeroTorque_Mode_Button.setMinimumSize(QSize(52, 40))
        self.zeroTorque_Mode_Button.setFont(font)
        self.zeroTorque_Mode_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.zeroTorque_Mode_Button.setStyleSheet(u"#zeroTorque_Mode_Button{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(63, 81, 181, 1);\n"
"	border-radius:8px;\n"
"}\n"
"#zeroTorque_Mode_Button:hover{\n"
"	background-color: rgba(121, 134, 203, 1);\n"
"	border-radius:8px;\n"
"}\n"
"#zeroTorque_Mode_Button:checked{\n"
"	background-color: rgba(0, 188, 212, 1);\n"
"	border-radius:8px;\n"
"	font-weight :800;\n"
"}\n"
"")
        self.zeroTorque_Mode_Button.setCheckable(True)
        self.zeroTorque_Mode_Button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.zeroTorque_Mode_Button)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Apply_PT_Parameters_Run_Button = QPushButton(self.groupBox_2)
        self.Apply_PT_Parameters_Run_Button.setObjectName(u"Apply_PT_Parameters_Run_Button")
        self.Apply_PT_Parameters_Run_Button.setMinimumSize(QSize(120, 40))
        font1 = QFont()
        font1.setBold(False)
        self.Apply_PT_Parameters_Run_Button.setFont(font1)
        self.Apply_PT_Parameters_Run_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Apply_PT_Parameters_Run_Button.setStyleSheet(u"#Apply_PT_Parameters_Run_Button { \n"
"color: white;\n"
"background-color:rgba(0, 121, 107, 1);\n"
"border-radius: 8px;\n"
"padding: 8px;\n"
"\n"
"}\n"
"\n"
"#Apply_PT_Parameters_Run_Button:hover {\n"
"\n"
"color: white;\n"
"background-color:rgba(0, 121, 107, 1);\n"
"padding: 8px;\n"
"}\n"
"\n"
"#Apply_PT_Parameters_Run_Button:pressed {\n"
"border: solid ;\n"
"background-color: rgba(241, 196, 15, 1);\n"
"padding: 8px;\n"
"}\n"
"")
        self.Apply_PT_Parameters_Run_Button.setCheckable(False)
        self.Apply_PT_Parameters_Run_Button.setChecked(False)
        self.Apply_PT_Parameters_Run_Button.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Apply_PT_Parameters_Run_Button)

        self.SavePT_Parameters_Button = QPushButton(self.groupBox_2)
        self.SavePT_Parameters_Button.setObjectName(u"SavePT_Parameters_Button")
        self.SavePT_Parameters_Button.setMinimumSize(QSize(120, 40))
        self.SavePT_Parameters_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SavePT_Parameters_Button.setStyleSheet(u"#SavePT_Parameters_Button { \n"
"color: white;\n"
"background-color: rgba(40, 167, 69, 1);\n"
"border-radius: 8px;\n"
"padding: 8px;\n"
"\n"
"}\n"
"\n"
"#SavePT_Parameters_Button:hover {\n"
"\n"
"color: white;\n"
"background-color: rgba(40, 167, 69, 1);\n"
"padding: 8px;\n"
"}\n"
"\n"
"#SavePT_Parameters_Button:pressed {\n"
"border: solid ;\n"
"background-color: rgba(241, 196, 15, 1);\n"
"padding: 8px;\n"
"}\n"
"")
        self.SavePT_Parameters_Button.setCheckable(False)
        self.SavePT_Parameters_Button.setChecked(False)
        self.SavePT_Parameters_Button.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.SavePT_Parameters_Button)

        self.Reset_PT_Parameters_Button = QPushButton(self.groupBox_2)
        self.Reset_PT_Parameters_Button.setObjectName(u"Reset_PT_Parameters_Button")
        self.Reset_PT_Parameters_Button.setMinimumSize(QSize(120, 40))
        self.Reset_PT_Parameters_Button.setFont(font1)
        self.Reset_PT_Parameters_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Reset_PT_Parameters_Button.setStyleSheet(u"#Reset_PT_Parameters_Button { \n"
"color: white;\n"
"background-color: rgba(220, 53, 69, 1);\n"
"border-radius: 8px;\n"
"padding: 8px;\n"
"\n"
"}\n"
"\n"
"#Reset_PT_Parameters_Button:hover {\n"
"\n"
"color: white;\n"
"background-color: rgba(220, 53, 69, 1);\n"
"padding: 8px;\n"
"}\n"
"\n"
"#Reset_PT_Parameters_Button:pressed {\n"
"border: solid ;\n"
"background-color: rgba(241, 196, 15, 1);\n"
"padding: 8px;\n"
"}\n"
"")
        self.Reset_PT_Parameters_Button.setCheckable(False)
        self.Reset_PT_Parameters_Button.setChecked(False)
        self.Reset_PT_Parameters_Button.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Reset_PT_Parameters_Button)

        self.record_Frame = QFrame(self.groupBox_2)
        self.record_Frame.setObjectName(u"record_Frame")
        self.record_Frame.setFrameShape(QFrame.StyledPanel)
        self.record_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.record_Frame)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.record_Button = QPushButton(self.record_Frame)
        self.record_Button.setObjectName(u"record_Button")
        self.record_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.record_Button.setStyleSheet(u"#record_Button { \n"
"	background: transparent; \n"
"	border: none;    	\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icon/icon/record_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.record_Button.setIcon(icon)
        self.record_Button.setIconSize(QSize(50, 50))
        self.record_Button.setCheckable(True)
        
        
        self.horizontalLayout_43.addWidget(self.record_Button)

        self.Record_Button_label = QLabel(self.record_Frame)
        self.Record_Button_label.setObjectName(u"Record_Button_label")
        
        self.horizontalLayout_43.addWidget(self.Record_Button_label)

        self.Record_Button_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.Record_Button_horizontalSpacer)


        self.verticalLayout_5.addWidget(self.record_Frame)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.horizontalLayout_45.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.Automatic_Page = QWidget()
        self.Automatic_Page.setObjectName(u"Automatic_Page")
        self.verticalLayout_14 = QVBoxLayout(self.Automatic_Page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_5 = QFrame(self.Automatic_Page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_41 = QLabel(self.frame_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 18))
        font2 = QFont()
        font2.setBold(True)
        self.label_41.setFont(font2)
        self.label_41.setScaledContents(False)
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_41.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_41)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_47 = QLabel(self.frame_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 18))
        self.label_47.setScaledContents(False)
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_47.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_47)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_52 = QLabel(self.frame_5)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 0))
        self.label_52.setMaximumSize(QSize(16777215, 44))
        self.label_52.setFrameShape(QFrame.Box)
        self.label_52.setFrameShadow(QFrame.Plain)
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_52.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_52)

        self.lineEdit_29 = QLineEdit(self.frame_5)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(50, 0))
        self.lineEdit_29.setMaximumSize(QSize(50, 500))
        self.lineEdit_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_29)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_69 = QLabel(self.frame_5)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 0))
        self.label_69.setMaximumSize(QSize(16777215, 44))
        self.label_69.setFrameShape(QFrame.Box)
        self.label_69.setFrameShadow(QFrame.Plain)
        self.label_69.setAlignment(Qt.AlignCenter)
        self.label_69.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_69)

        self.lineEdit_33 = QLineEdit(self.frame_5)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(50, 0))
        self.lineEdit_33.setMaximumSize(QSize(50, 500))
        self.lineEdit_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_33)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_70 = QLabel(self.frame_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 0))
        self.label_70.setMaximumSize(QSize(16777215, 44))
        self.label_70.setFrameShape(QFrame.Box)
        self.label_70.setFrameShadow(QFrame.Plain)
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_70.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_70)

        self.lineEdit_34 = QLineEdit(self.frame_5)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(50, 0))
        self.lineEdit_34.setMaximumSize(QSize(50, 500))
        self.lineEdit_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_34)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_46 = QLabel(self.frame_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 18))
        self.label_46.setScaledContents(False)
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_46.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_46)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_71 = QLabel(self.frame_5)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 0))
        self.label_71.setMaximumSize(QSize(16777215, 44))
        self.label_71.setFrameShape(QFrame.Box)
        self.label_71.setFrameShadow(QFrame.Plain)
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_71.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_71)

        self.lineEdit_36 = QLineEdit(self.frame_5)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(50, 0))
        self.lineEdit_36.setMaximumSize(QSize(50, 500))
        self.lineEdit_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_36)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_72 = QLabel(self.frame_5)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 0))
        self.label_72.setMaximumSize(QSize(16777215, 44))
        self.label_72.setFrameShape(QFrame.Box)
        self.label_72.setFrameShadow(QFrame.Plain)
        self.label_72.setAlignment(Qt.AlignCenter)
        self.label_72.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_72)

        self.lineEdit_35 = QLineEdit(self.frame_5)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(50, 0))
        self.lineEdit_35.setMaximumSize(QSize(50, 500))
        self.lineEdit_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_35)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_73 = QLabel(self.frame_5)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 0))
        self.label_73.setMaximumSize(QSize(16777215, 44))
        self.label_73.setFrameShape(QFrame.Box)
        self.label_73.setFrameShadow(QFrame.Plain)
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_73.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_73)

        self.lineEdit_37 = QLineEdit(self.frame_5)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(50, 0))
        self.lineEdit_37.setMaximumSize(QSize(50, 500))
        self.lineEdit_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_37)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_54 = QLabel(self.frame_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 0))
        self.label_54.setMaximumSize(QSize(16777215, 500))
        self.label_54.setFrameShape(QFrame.Box)
        self.label_54.setFrameShadow(QFrame.Plain)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_54.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.label_54)

        self.lineEdit_38 = QLineEdit(self.frame_5)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(50, 0))
        self.lineEdit_38.setMaximumSize(QSize(40, 500))
        self.lineEdit_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_38)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_55 = QLabel(self.frame_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 0))
        self.label_55.setMaximumSize(QSize(16777215, 500))
        self.label_55.setFrameShape(QFrame.Box)
        self.label_55.setFrameShadow(QFrame.Plain)
        self.label_55.setAlignment(Qt.AlignCenter)
        self.label_55.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.label_55)

        self.lineEdit_39 = QLineEdit(self.frame_5)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(50, 0))
        self.lineEdit_39.setMaximumSize(QSize(40, 500))
        self.lineEdit_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_39)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 0))
        self.label_56.setMaximumSize(QSize(16777215, 500))
        self.label_56.setFrameShape(QFrame.Box)
        self.label_56.setFrameShadow(QFrame.Plain)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.label_56)

        self.lineEdit_40 = QLineEdit(self.frame_5)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setMinimumSize(QSize(50, 0))
        self.lineEdit_40.setMaximumSize(QSize(40, 500))
        self.lineEdit_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_40)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_57 = QLabel(self.frame_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 0))
        self.label_57.setMaximumSize(QSize(16777215, 500))
        self.label_57.setFrameShape(QFrame.Box)
        self.label_57.setFrameShadow(QFrame.Plain)
        self.label_57.setAlignment(Qt.AlignCenter)
        self.label_57.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.label_57)

        self.lineEdit_41 = QLineEdit(self.frame_5)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setMinimumSize(QSize(50, 0))
        self.lineEdit_41.setMaximumSize(QSize(40, 500))
        self.lineEdit_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lineEdit_41)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_29.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_58 = QLabel(self.frame_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 0))
        self.label_58.setMaximumSize(QSize(16777215, 500))
        self.label_58.setFrameShape(QFrame.Box)
        self.label_58.setFrameShadow(QFrame.Plain)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.label_58)

        self.lineEdit_42 = QLineEdit(self.frame_5)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(50, 0))
        self.lineEdit_42.setMaximumSize(QSize(40, 500))
        self.lineEdit_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit_42)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_59 = QLabel(self.frame_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 0))
        self.label_59.setMaximumSize(QSize(16777215, 500))
        self.label_59.setFrameShape(QFrame.Box)
        self.label_59.setFrameShadow(QFrame.Plain)
        self.label_59.setAlignment(Qt.AlignCenter)
        self.label_59.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_59)

        self.lineEdit_43 = QLineEdit(self.frame_5)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setMinimumSize(QSize(50, 0))
        self.lineEdit_43.setMaximumSize(QSize(40, 500))
        self.lineEdit_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lineEdit_43)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 0))
        self.label_60.setMaximumSize(QSize(16777215, 500))
        self.label_60.setFrameShape(QFrame.Box)
        self.label_60.setFrameShadow(QFrame.Plain)
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_60.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.label_60)

        self.lineEdit_44 = QLineEdit(self.frame_5)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMinimumSize(QSize(50, 0))
        self.lineEdit_44.setMaximumSize(QSize(40, 500))
        self.lineEdit_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lineEdit_44)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_61 = QLabel(self.frame_5)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setMaximumSize(QSize(16777215, 500))
        self.label_61.setFrameShape(QFrame.Box)
        self.label_61.setFrameShadow(QFrame.Plain)
        self.label_61.setAlignment(Qt.AlignCenter)
        self.label_61.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.label_61)

        self.lineEdit_45 = QLineEdit(self.frame_5)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setMinimumSize(QSize(50, 0))
        self.lineEdit_45.setMaximumSize(QSize(40, 500))
        self.lineEdit_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lineEdit_45)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_29.addLayout(self.verticalLayout_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_64 = QLabel(self.frame_5)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setMaximumSize(QSize(16777215, 500))
        self.label_64.setFrameShape(QFrame.Box)
        self.label_64.setFrameShadow(QFrame.Plain)
        self.label_64.setAlignment(Qt.AlignCenter)
        self.label_64.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_64)

        self.lineEdit_48 = QLineEdit(self.frame_5)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setMinimumSize(QSize(50, 0))
        self.lineEdit_48.setMaximumSize(QSize(40, 500))
        self.lineEdit_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lineEdit_48)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_65 = QLabel(self.frame_5)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setMaximumSize(QSize(16777215, 500))
        self.label_65.setFrameShape(QFrame.Box)
        self.label_65.setFrameShadow(QFrame.Plain)
        self.label_65.setAlignment(Qt.AlignCenter)
        self.label_65.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_65)

        self.lineEdit_49 = QLineEdit(self.frame_5)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setMinimumSize(QSize(50, 0))
        self.lineEdit_49.setMaximumSize(QSize(40, 500))
        self.lineEdit_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.lineEdit_49)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_30.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_62 = QLabel(self.frame_5)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 0))
        self.label_62.setMaximumSize(QSize(16777215, 500))
        self.label_62.setFrameShape(QFrame.Box)
        self.label_62.setFrameShadow(QFrame.Plain)
        self.label_62.setAlignment(Qt.AlignCenter)
        self.label_62.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.label_62)

        self.lineEdit_46 = QLineEdit(self.frame_5)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setMinimumSize(QSize(50, 0))
        self.lineEdit_46.setMaximumSize(QSize(40, 500))
        self.lineEdit_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_46)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_63 = QLabel(self.frame_5)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setMaximumSize(QSize(16777215, 500))
        self.label_63.setFrameShape(QFrame.Box)
        self.label_63.setFrameShadow(QFrame.Plain)
        self.label_63.setAlignment(Qt.AlignCenter)
        self.label_63.setWordWrap(True)

        self.horizontalLayout_21.addWidget(self.label_63)

        self.lineEdit_47 = QLineEdit(self.frame_5)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setMinimumSize(QSize(50, 0))
        self.lineEdit_47.setMaximumSize(QSize(40, 500))
        self.lineEdit_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_47)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_30.addLayout(self.verticalLayout_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_66 = QLabel(self.frame_5)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 0))
        self.label_66.setMaximumSize(QSize(16777215, 500))
        self.label_66.setFrameShape(QFrame.Box)
        self.label_66.setFrameShadow(QFrame.Plain)
        self.label_66.setAlignment(Qt.AlignCenter)
        self.label_66.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.label_66)

        self.lineEdit_50 = QLineEdit(self.frame_5)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setMinimumSize(QSize(50, 0))
        self.lineEdit_50.setMaximumSize(QSize(40, 500))
        self.lineEdit_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.lineEdit_50)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_67 = QLabel(self.frame_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 0))
        self.label_67.setMaximumSize(QSize(16777215, 500))
        self.label_67.setFrameShape(QFrame.Box)
        self.label_67.setFrameShadow(QFrame.Plain)
        self.label_67.setAlignment(Qt.AlignCenter)
        self.label_67.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.label_67)

        self.lineEdit_51 = QLineEdit(self.frame_5)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setMinimumSize(QSize(50, 0))
        self.lineEdit_51.setMaximumSize(QSize(40, 500))
        self.lineEdit_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lineEdit_51)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_25)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_2)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_74 = QLabel(self.frame_5)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 0))
        self.label_74.setMaximumSize(QSize(16777215, 500))
        self.label_74.setFrameShape(QFrame.Box)
        self.label_74.setFrameShadow(QFrame.Plain)
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_74.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.label_74)

        self.lineEdit_52 = QLineEdit(self.frame_5)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setMinimumSize(QSize(50, 0))
        self.lineEdit_52.setMaximumSize(QSize(40, 500))
        self.lineEdit_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.lineEdit_52)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_75 = QLabel(self.frame_5)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(0, 0))
        self.label_75.setMaximumSize(QSize(16777215, 500))
        self.label_75.setFrameShape(QFrame.Box)
        self.label_75.setFrameShadow(QFrame.Plain)
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_75.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_75)

        self.lineEdit_53 = QLineEdit(self.frame_5)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setMinimumSize(QSize(50, 0))
        self.lineEdit_53.setMaximumSize(QSize(40, 500))
        self.lineEdit_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.lineEdit_53)


        self.verticalLayout_10.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_31.addLayout(self.verticalLayout_10)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_31)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_3)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_76 = QLabel(self.frame_5)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(0, 0))
        self.label_76.setMaximumSize(QSize(16777215, 500))
        self.label_76.setFrameShape(QFrame.Box)
        self.label_76.setFrameShadow(QFrame.Plain)
        self.label_76.setAlignment(Qt.AlignCenter)
        self.label_76.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.label_76)

        self.lineEdit_54 = QLineEdit(self.frame_5)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setMinimumSize(QSize(50, 0))
        self.lineEdit_54.setMaximumSize(QSize(40, 500))
        self.lineEdit_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lineEdit_54)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_32.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)


        self.verticalLayout_14.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.Automatic_Page)
        self.Squat_Page = QWidget()
        self.Squat_Page.setObjectName(u"Squat_Page")
        self.verticalLayout_21 = QVBoxLayout(self.Squat_Page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.standingStill_Up_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.standingStill_Up_verticalSpacer)

        self.standingstill_and_squatparameters_label = QLabel(self.Squat_Page)
        self.standingstill_and_squatparameters_label.setObjectName(u"standingstill_and_squatparameters_label")
        self.standingstill_and_squatparameters_label.setMaximumSize(QSize(16777215, 25))
        self.standingstill_and_squatparameters_label.setFont(font2)
        self.standingstill_and_squatparameters_label.setAlignment(Qt.AlignCenter)
        self.standingstill_and_squatparameters_label.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.standingstill_and_squatparameters_label)

        self.standinStill_and_SquatParameters_horizontalLayout = QHBoxLayout()
        self.standinStill_and_SquatParameters_horizontalLayout.setObjectName(u"standinStill_and_SquatParameters_horizontalLayout")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.SSEMTSSTS_verticalLayout = QVBoxLayout()
        self.SSEMTSSTS_verticalLayout.setObjectName(u"SSEMTSSTS_verticalLayout")
        self.SSEMT_horizontalLayout = QHBoxLayout()
        self.SSEMT_horizontalLayout.setSpacing(0)
        self.SSEMT_horizontalLayout.setObjectName(u"SSEMT_horizontalLayout")
        self.sq_ssEccMaxTorque_label = QLabel(self.Squat_Page)
        self.sq_ssEccMaxTorque_label.setObjectName(u"sq_ssEccMaxTorque_label")
        self.sq_ssEccMaxTorque_label.setMinimumSize(QSize(0, 0))
        self.sq_ssEccMaxTorque_label.setMaximumSize(QSize(16777215, 500))
        self.sq_ssEccMaxTorque_label.setFrameShape(QFrame.Box)
        self.sq_ssEccMaxTorque_label.setFrameShadow(QFrame.Plain)
        self.sq_ssEccMaxTorque_label.setAlignment(Qt.AlignCenter)
        self.sq_ssEccMaxTorque_label.setWordWrap(True)

        self.SSEMT_horizontalLayout.addWidget(self.sq_ssEccMaxTorque_label)

        self.sq_ssEccMaxTorque_lineEdit = QLineEdit(self.Squat_Page)
        self.sq_ssEccMaxTorque_lineEdit.setObjectName(u"sq_ssEccMaxTorque_lineEdit")
        self.sq_ssEccMaxTorque_lineEdit.setMinimumSize(QSize(50, 0))
        self.sq_ssEccMaxTorque_lineEdit.setMaximumSize(QSize(40, 500))
        self.sq_ssEccMaxTorque_lineEdit.setAlignment(Qt.AlignCenter)

        self.SSEMT_horizontalLayout.addWidget(self.sq_ssEccMaxTorque_lineEdit)


        self.SSEMTSSTS_verticalLayout.addLayout(self.SSEMT_horizontalLayout)

        self.sq_ssEccK_horizontalLayout = QHBoxLayout()
        self.sq_ssEccK_horizontalLayout.setSpacing(0)
        self.sq_ssEccK_horizontalLayout.setObjectName(u"sq_ssEccK_horizontalLayout")
        self.sq_ssEccK_label = QLabel(self.Squat_Page)
        self.sq_ssEccK_label.setObjectName(u"sq_ssEccK_label")
        self.sq_ssEccK_label.setMinimumSize(QSize(0, 0))
        self.sq_ssEccK_label.setMaximumSize(QSize(16777215, 500))
        self.sq_ssEccK_label.setFrameShape(QFrame.Box)
        self.sq_ssEccK_label.setFrameShadow(QFrame.Plain)
        self.sq_ssEccK_label.setAlignment(Qt.AlignCenter)
        self.sq_ssEccK_label.setWordWrap(True)

        self.sq_ssEccK_horizontalLayout.addWidget(self.sq_ssEccK_label)

        self.sq_ssEccK_lineEdit = QLineEdit(self.Squat_Page)
        self.sq_ssEccK_lineEdit.setObjectName(u"sq_ssEccK_lineEdit")
        self.sq_ssEccK_lineEdit.setMinimumSize(QSize(50, 0))
        self.sq_ssEccK_lineEdit.setMaximumSize(QSize(40, 500))
        self.sq_ssEccK_lineEdit.setAlignment(Qt.AlignCenter)

        self.sq_ssEccK_horizontalLayout.addWidget(self.sq_ssEccK_lineEdit)


        self.SSEMTSSTS_verticalLayout.addLayout(self.sq_ssEccK_horizontalLayout)


        self.horizontalLayout_44.addLayout(self.SSEMTSSTS_verticalLayout)


        self.standinStill_and_SquatParameters_horizontalLayout.addLayout(self.horizontalLayout_44)

        self.AW_SAW_verticalLayout = QVBoxLayout()
        self.AW_SAW_verticalLayout.setObjectName(u"AW_SAW_verticalLayout")
        self.squatAssistWeight_label = QLabel(self.Squat_Page)
        self.squatAssistWeight_label.setObjectName(u"squatAssistWeight_label")
        self.squatAssistWeight_label.setAlignment(Qt.AlignCenter)
        self.squatAssistWeight_label.setWordWrap(True)

        self.AW_SAW_verticalLayout.addWidget(self.squatAssistWeight_label)

        self.sq_assistWeight_horizontalLayout = QHBoxLayout()
        self.sq_assistWeight_horizontalLayout.setSpacing(0)
        self.sq_assistWeight_horizontalLayout.setObjectName(u"sq_assistWeight_horizontalLayout")
        self.sq_assistWeight_label = QLabel(self.Squat_Page)
        self.sq_assistWeight_label.setObjectName(u"sq_assistWeight_label")
        self.sq_assistWeight_label.setMinimumSize(QSize(0, 0))
        self.sq_assistWeight_label.setMaximumSize(QSize(16777215, 500))
        self.sq_assistWeight_label.setFrameShape(QFrame.Box)
        self.sq_assistWeight_label.setFrameShadow(QFrame.Plain)
        self.sq_assistWeight_label.setAlignment(Qt.AlignCenter)
        self.sq_assistWeight_label.setWordWrap(True)

        self.sq_assistWeight_horizontalLayout.addWidget(self.sq_assistWeight_label)

        self.sq_assistWeight_lineEdit = QLineEdit(self.Squat_Page)
        self.sq_assistWeight_lineEdit.setObjectName(u"sq_assistWeight_lineEdit")
        self.sq_assistWeight_lineEdit.setMinimumSize(QSize(50, 0))
        self.sq_assistWeight_lineEdit.setMaximumSize(QSize(40, 500))
        self.sq_assistWeight_lineEdit.setAlignment(Qt.AlignCenter)

        self.sq_assistWeight_horizontalLayout.addWidget(self.sq_assistWeight_lineEdit)


        self.AW_SAW_verticalLayout.addLayout(self.sq_assistWeight_horizontalLayout)


        self.standinStill_and_SquatParameters_horizontalLayout.addLayout(self.AW_SAW_verticalLayout)


        self.verticalLayout_21.addLayout(self.standinStill_and_SquatParameters_horizontalLayout)

        self.standingStill_Down_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.standingStill_Down_verticalSpacer)

        self.stackedWidget.addWidget(self.Squat_Page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_15 = QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"#label_4 {\n"
"color:white;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page)
        self.Sit2Stand_and_Stand2Sit_Page = QWidget()
        self.Sit2Stand_and_Stand2Sit_Page.setObjectName(u"Sit2Stand_and_Stand2Sit_Page")
        self.verticalLayout_24 = QVBoxLayout(self.Sit2Stand_and_Stand2Sit_Page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_7 = QSpacerItem(20, 416, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_7)

        self.SS_and_SS_Parameters_label = QLabel(self.Sit2Stand_and_Stand2Sit_Page)
        self.SS_and_SS_Parameters_label.setObjectName(u"SS_and_SS_Parameters_label")
        self.SS_and_SS_Parameters_label.setMaximumSize(QSize(16777215, 25))
        self.SS_and_SS_Parameters_label.setFont(font2)
        self.SS_and_SS_Parameters_label.setAlignment(Qt.AlignCenter)
        self.SS_and_SS_Parameters_label.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.SS_and_SS_Parameters_label)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.ssEccK_verticalLayout = QVBoxLayout()
        self.ssEccK_verticalLayout.setObjectName(u"ssEccK_verticalLayout")
        self.s2s_ssEccMaxTorque_horizontalLayout = QHBoxLayout()
        self.s2s_ssEccMaxTorque_horizontalLayout.setSpacing(0)
        self.s2s_ssEccMaxTorque_horizontalLayout.setObjectName(u"s2s_ssEccMaxTorque_horizontalLayout")
        self.s2s_ssEccMaxTorque_label = QLabel(self.Sit2Stand_and_Stand2Sit_Page)
        self.s2s_ssEccMaxTorque_label.setObjectName(u"s2s_ssEccMaxTorque_label")
        self.s2s_ssEccMaxTorque_label.setMinimumSize(QSize(0, 0))
        self.s2s_ssEccMaxTorque_label.setMaximumSize(QSize(16777215, 500))
        font4 = QFont()
        font4.setPointSize(8)
        self.s2s_ssEccMaxTorque_label.setFont(font4)
        self.s2s_ssEccMaxTorque_label.setFrameShape(QFrame.Box)
        self.s2s_ssEccMaxTorque_label.setFrameShadow(QFrame.Plain)
        self.s2s_ssEccMaxTorque_label.setAlignment(Qt.AlignCenter)
        self.s2s_ssEccMaxTorque_label.setWordWrap(True)

        self.s2s_ssEccMaxTorque_horizontalLayout.addWidget(self.s2s_ssEccMaxTorque_label)

        self.s2s_ssEccMaxTorque_lineEdit = QLineEdit(self.Sit2Stand_and_Stand2Sit_Page)
        self.s2s_ssEccMaxTorque_lineEdit.setObjectName(u"s2s_ssEccMaxTorque_lineEdit")
        self.s2s_ssEccMaxTorque_lineEdit.setMinimumSize(QSize(50, 0))
        self.s2s_ssEccMaxTorque_lineEdit.setMaximumSize(QSize(40, 500))
        self.s2s_ssEccMaxTorque_lineEdit.setAlignment(Qt.AlignCenter)

        self.s2s_ssEccMaxTorque_horizontalLayout.addWidget(self.s2s_ssEccMaxTorque_lineEdit)


        self.ssEccK_verticalLayout.addLayout(self.s2s_ssEccMaxTorque_horizontalLayout)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.s2s_ssEccK_label = QLabel(self.Sit2Stand_and_Stand2Sit_Page)
        self.s2s_ssEccK_label.setObjectName(u"s2s_ssEccK_label")
        self.s2s_ssEccK_label.setMinimumSize(QSize(0, 0))
        self.s2s_ssEccK_label.setMaximumSize(QSize(16777215, 500))
        self.s2s_ssEccK_label.setFrameShape(QFrame.Box)
        self.s2s_ssEccK_label.setFrameShadow(QFrame.Plain)
        self.s2s_ssEccK_label.setAlignment(Qt.AlignCenter)
        self.s2s_ssEccK_label.setWordWrap(True)

        self.horizontalLayout_52.addWidget(self.s2s_ssEccK_label)

        self.s2s_ssEccK_lineEdit = QLineEdit(self.Sit2Stand_and_Stand2Sit_Page)
        self.s2s_ssEccK_lineEdit.setObjectName(u"s2s_ssEccK_lineEdit")
        self.s2s_ssEccK_lineEdit.setMinimumSize(QSize(50, 0))
        self.s2s_ssEccK_lineEdit.setMaximumSize(QSize(40, 500))
        self.s2s_ssEccK_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.s2s_ssEccK_lineEdit)


        self.ssEccK_verticalLayout.addLayout(self.horizontalLayout_52)


        self.horizontalLayout_50.addLayout(self.ssEccK_verticalLayout)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_50)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.s2s_s2s_assistweight_Label = QLabel(self.Sit2Stand_and_Stand2Sit_Page)
        self.s2s_s2s_assistweight_Label.setObjectName(u"s2s_s2s_assistweight_Label")
        self.s2s_s2s_assistweight_Label.setAlignment(Qt.AlignCenter)
        self.s2s_s2s_assistweight_Label.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.s2s_s2s_assistweight_Label)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.auto_assistweight_label = QLabel(self.Sit2Stand_and_Stand2Sit_Page)
        self.auto_assistweight_label.setObjectName(u"auto_assistweight_label")
        self.auto_assistweight_label.setMinimumSize(QSize(0, 0))
        self.auto_assistweight_label.setMaximumSize(QSize(16777215, 500))
        self.auto_assistweight_label.setFrameShape(QFrame.Box)
        self.auto_assistweight_label.setFrameShadow(QFrame.Plain)
        self.auto_assistweight_label.setAlignment(Qt.AlignCenter)
        self.auto_assistweight_label.setWordWrap(True)

        self.horizontalLayout_53.addWidget(self.auto_assistweight_label)

        self.auto_assistweight_lineEdit = QLineEdit(self.Sit2Stand_and_Stand2Sit_Page)
        self.auto_assistweight_lineEdit.setObjectName(u"auto_assistweight_lineEdit")
        self.auto_assistweight_lineEdit.setMinimumSize(QSize(50, 0))
        self.auto_assistweight_lineEdit.setMaximumSize(QSize(40, 500))
        self.auto_assistweight_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.auto_assistweight_lineEdit)


        self.verticalLayout_23.addLayout(self.horizontalLayout_53)


        self.horizontalLayout_49.addLayout(self.verticalLayout_23)


        self.verticalLayout_24.addLayout(self.horizontalLayout_49)

        self.verticalSpacer_8 = QSpacerItem(20, 415, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.Sit2Stand_and_Stand2Sit_Page)

        self.horizontalLayout_45.addWidget(self.stackedWidget)


        self.retranslateUi(self)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(self)
    # setupUi

        self.stackedWidget.addWidget(self.Automatic_Page)     # index 0
        self.stackedWidget.addWidget(self.Squat_Page)         # index 1
        self.stackedWidget.addWidget(self.Sit2Stand_and_Stand2Sit_Page)  # index 2
        self.stackedWidget.addWidget(self.page) #index3

        
        self.Automatic_Mode_Button.clicked.connect(lambda: self.set_mode_page(0))
        self.Squat_Mode_Button.clicked.connect(lambda: self.set_mode_page(1))
        self.Stand2Sit_and_Sit2Stand_Mode_Button.clicked.connect(lambda: self.set_mode_page(2))
        self.zeroTorque_Mode_Button.clicked.connect(lambda: self.set_mode_page(3))

        self.retranslateUi(self)
        self.stackedWidget.setCurrentIndex(0)  # صفحه‌ی پیش‌فرض
        QMetaObject.connectSlotsByName(self)

    def set_mode_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def setMode(self,Mode):
        self.Mode = Mode


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.User_Sign_Up_label.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.user_ID_signup_lineEdit.setInputMask("")
        self.user_ID_signup_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"User ID", None))
        self.Name_and_LastName_lineEdit.setInputMask("")
        self.Name_and_LastName_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Name and Last Name", None))
        self.add_user_Button.setText(QCoreApplication.translate("Form", u"Add User", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Female", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"Male", None))
        self.Age_lineEdit.setInputMask("")
        self.Age_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Age ", None))
        self.Height_lineEdit.setInputMask("")
        self.Height_lineEdit.setText("")
        self.Height_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Height (cm)", None))
        self.Weight_lineEdit.setInputMask("")
        self.Weight_lineEdit.setText("")
        self.Weight_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Weight (kg)", None))
        self.User_Login_label.setText(QCoreApplication.translate("Form", u"Login", None))
        self.user_ID_login_lineEdit.setText("")
        self.user_ID_login_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"User ID", None))
        self.Sign_In_Button.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Show All Users", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Select Mode:", None))
        self.Automatic_Mode_Button.setText(QCoreApplication.translate("Form", u"Automatic", None))
        self.Squat_Mode_Button.setText(QCoreApplication.translate("Form", u"Squat", None))
        self.Stand2Sit_and_Sit2Stand_Mode_Button.setText(QCoreApplication.translate("Form", u"Stant2Sit and Sit2Stand", None))
        self.zeroTorque_Mode_Button.setText(QCoreApplication.translate("Form", u"Zero Torque", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Actions:", None))
        self.Apply_PT_Parameters_Run_Button.setText(QCoreApplication.translate("Form", u"Apply PT Parameters and Run", None))
        self.SavePT_Parameters_Button.setText(QCoreApplication.translate("Form", u"Save PT Parameters", None))
        self.Reset_PT_Parameters_Button.setText(QCoreApplication.translate("Form", u"Reset PT Parameters", None))
        self.record_Button.setText("")
        self.Record_Button_label.setText(QCoreApplication.translate("Form", u"Record Button", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Walking Parameters", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Left Leg", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"Left Flextion Angle Limit (deg)", None))
        self.lineEdit_29.setText(QCoreApplication.translate("Form", u"50", None))
        self.lineEdit_29.setPlaceholderText(QCoreApplication.translate("Form", u"50", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"Left Extension Angle Limit (deg)", None))
        self.lineEdit_33.setText(QCoreApplication.translate("Form", u"10", None))
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"Left Flextion Minimum Allowed Angle (deg)", None))
        self.lineEdit_34.setText(QCoreApplication.translate("Form", u"10", None))
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Right Legh", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"Right Flexion Angle Limit(deg)", None))
        self.lineEdit_36.setText(QCoreApplication.translate("Form", u"60", None))
        self.lineEdit_36.setPlaceholderText(QCoreApplication.translate("Form", u"60", None))
        self.label_72.setText(QCoreApplication.translate("Form", u"Right Extension Angle Limit (deg)", None))
        self.lineEdit_35.setText(QCoreApplication.translate("Form", u"10", None))
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.label_73.setText(QCoreApplication.translate("Form", u"Right Flextion Minimum Allowed Angle (deg)", None))
        self.lineEdit_37.setText(QCoreApplication.translate("Form", u"10", None))
        self.lineEdit_37.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"Left Flextion Maximum Torque (n.m)", None))
        self.lineEdit_38.setText(QCoreApplication.translate("Form", u"7.5", None))
        self.lineEdit_38.setPlaceholderText(QCoreApplication.translate("Form", u"7.5", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Maximum Torque (n.m)", None))
        self.lineEdit_39.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.lineEdit_39.setPlaceholderText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Maximum Torque (n.m)", None))
        self.lineEdit_40.setText(QCoreApplication.translate("Form", u"3.5", None))
        self.lineEdit_40.setPlaceholderText(QCoreApplication.translate("Form", u"3.5", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Maximum Torque (n.m)", None))
        self.lineEdit_41.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.lineEdit_41.setPlaceholderText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Right Flextion Maximum Torque (n.m)", None))
        self.lineEdit_42.setText(QCoreApplication.translate("Form", u"7.5", None))
        self.lineEdit_42.setPlaceholderText(QCoreApplication.translate("Form", u"7.5", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"Right Flexion Steepness ", None))
        self.lineEdit_43.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.lineEdit_43.setPlaceholderText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Right Extension Maximum Torque (n.m)", None))
        self.lineEdit_44.setText(QCoreApplication.translate("Form", u"3.5", None))
        self.lineEdit_44.setPlaceholderText(QCoreApplication.translate("Form", u"3.5", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"Right Extension Steepness", None))
        self.lineEdit_45.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.lineEdit_45.setPlaceholderText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"Left Walking Eccentric Maximum Torque (n.m)", None))
        self.lineEdit_48.setText(QCoreApplication.translate("Form", u"4", None))
        self.lineEdit_48.setPlaceholderText(QCoreApplication.translate("Form", u"4", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"Left Walking Eccentric Steepness", None))
        self.lineEdit_49.setText(QCoreApplication.translate("Form", u"2", None))
        self.lineEdit_49.setPlaceholderText(QCoreApplication.translate("Form", u"2", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"Right Walking Eccentric Maximum Torque (n.m)", None))
        self.lineEdit_46.setText(QCoreApplication.translate("Form", u"4", None))
        self.lineEdit_46.setPlaceholderText(QCoreApplication.translate("Form", u"4", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"Right Walking Eccentric Steepness", None))
        self.lineEdit_47.setText(QCoreApplication.translate("Form", u"2", None))
        self.lineEdit_47.setPlaceholderText(QCoreApplication.translate("Form", u"2", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"Shank Length (cm)", None))
        self.lineEdit_50.setText(QCoreApplication.translate("Form", u"54", None))
        self.lineEdit_50.setPlaceholderText(QCoreApplication.translate("Form", u"54", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"Thigh Length (cm)", None))
        self.lineEdit_51.setText(QCoreApplication.translate("Form", u"45", None))
        self.lineEdit_51.setPlaceholderText(QCoreApplication.translate("Form", u"45", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Standing Still and Stand2Sit/Sit2Stand Parameters", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"Standing Still Maximum Torque (n.m)", None))
        self.lineEdit_52.setText(QCoreApplication.translate("Form", u"8", None))
        self.lineEdit_52.setPlaceholderText(QCoreApplication.translate("Form", u"8", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Steepness", None))
        self.lineEdit_53.setText(QCoreApplication.translate("Form", u"0.25", None))
        self.lineEdit_53.setPlaceholderText(QCoreApplication.translate("Form", u"0.25", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Stand2Sit, Sit2Stand and Squat Assist Weight", None))
        self.label_76.setText(QCoreApplication.translate("Form", u"Assist Weight (kg)", None))
        self.lineEdit_54.setText(QCoreApplication.translate("Form", u"70", None))
        self.lineEdit_54.setPlaceholderText(QCoreApplication.translate("Form", u"70", None))
        self.standingstill_and_squatparameters_label.setText(QCoreApplication.translate("Form", u"Standing Still and Squat Parameters", None))
        self.sq_ssEccMaxTorque_label.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Maximum Torque (n.m)", None))
        self.sq_ssEccMaxTorque_lineEdit.setText(QCoreApplication.translate("Form", u"8", None))
        self.sq_ssEccMaxTorque_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"8", None))
        self.sq_ssEccK_label.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Steepness", None))
        self.sq_ssEccK_lineEdit.setText(QCoreApplication.translate("Form", u"0.25", None))
        self.sq_ssEccK_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.25", None))
        self.squatAssistWeight_label.setText(QCoreApplication.translate("Form", u"Squat Assist Weight", None))
        self.sq_assistWeight_label.setText(QCoreApplication.translate("Form", u"Assist Weight (kg)", None))
        self.sq_assistWeight_lineEdit.setText(QCoreApplication.translate("Form", u"70", None))
        self.sq_assistWeight_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"70", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Zero Torque Mode is ON", None))
        self.SS_and_SS_Parameters_label.setText(QCoreApplication.translate("Form", u"Standing Still and Stand2Sit/Sit2Stand Parameters", None))
        self.s2s_ssEccMaxTorque_label.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Maximum Torque (n.m)", None))
        self.s2s_ssEccMaxTorque_lineEdit.setText(QCoreApplication.translate("Form", u"8", None))
        self.s2s_ssEccMaxTorque_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"8", None))
        self.s2s_ssEccK_label.setText(QCoreApplication.translate("Form", u"Standing Still Eccentric Steepness", None))
        self.s2s_ssEccK_lineEdit.setText(QCoreApplication.translate("Form", u"0.25", None))
        self.s2s_ssEccK_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.25", None))
        self.s2s_s2s_assistweight_Label.setText(QCoreApplication.translate("Form", u"Stand2Sit/Sit2Stand Assist Weight", None))
        self.auto_assistweight_label.setText(QCoreApplication.translate("Form", u"Assist Weight (kg)", None))
        self.auto_assistweight_lineEdit.setText(QCoreApplication.translate("Form", u"70", None))
        self.auto_assistweight_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"70", None))
    # retranslateUi
        

        

