# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Debbug.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(1250, 807)
        self.Main_widget = QWidget(Form)
        self.Main_widget.setObjectName(u"Main_widget")
        self.Main_widget.setGeometry(QRect(10, 10, 1221, 801))
        self.verticalLayout_17 = QVBoxLayout(self.Main_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.Main_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.flagn1_label = ColorChangingFrame(self.frame)
        self.flagn1_label.setObjectName(u"flagn1_label")
        font = QFont()
        font.setPointSize(6)
        self.flagn1_label.setFont(font)
        self.flagn1_label.setFrameShape(QFrame.Shape.Box)
        self.flagn1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.flagn1_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stopWalking_Frame = QFrame(self.frame)
        self.stopWalking_Frame.setObjectName(u"stopWalking_Frame")
        self.stopWalking_Frame.setFrameShape(QFrame.Shape.Box)
        self.stopWalking_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.stopWalking_Frame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.stopWalking_Frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StopWalking_label = ColorChangingFrame(self.stopWalking_Frame)
        self.StopWalking_label.setObjectName(u"StopWalking_label")
        self.StopWalking_label.setMinimumSize(QSize(120, 0))
        self.StopWalking_label.setMaximumSize(QSize(16777215, 18))
        self.StopWalking_label.setFont(font)
        self.StopWalking_label.setFrameShape(QFrame.Shape.Box)
        self.StopWalking_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.StopWalking_label)

        self.flagn2_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flagn2_label.setObjectName(u"flagn2_label")
        self.flagn2_label.setMinimumSize(QSize(120, 0))
        self.flagn2_label.setMaximumSize(QSize(16777215, 18))
        self.flagn2_label.setFont(font)
        self.flagn2_label.setFrameShape(QFrame.Shape.Box)
        self.flagn2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.flagn2_label)

        self.stopWalking_stateNumber0_Label = QLabel(self.stopWalking_Frame)
        self.stopWalking_stateNumber0_Label.setObjectName(u"stopWalking_stateNumber0_Label")
        self.stopWalking_stateNumber0_Label.setMinimumSize(QSize(120, 0))
        self.stopWalking_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.stopWalking_stateNumber0_Label.setFont(font)
        self.stopWalking_stateNumber0_Label.setFrameShape(QFrame.Shape.Box)
        self.stopWalking_stateNumber0_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.stopWalking_stateNumber0_Label)

        self.stoWalking_Flag1_horizontalLayout = QHBoxLayout()
        self.stoWalking_Flag1_horizontalLayout.setSpacing(0)
        self.stoWalking_Flag1_horizontalLayout.setObjectName(u"stoWalking_Flag1_horizontalLayout")
        self.flagn16_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flagn16_label.setObjectName(u"flagn16_label")
        self.flagn16_label.setFont(font)
        self.flagn16_label.setFrameShape(QFrame.Shape.Box)
        self.flagn16_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn16_label.setWordWrap(True)

        self.stoWalking_Flag1_horizontalLayout.addWidget(self.flagn16_label)

        self.flagn19_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flagn19_lineEdit.setObjectName(u"flagn19_lineEdit")
        self.flagn19_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn19_lineEdit.setMaximumSize(QSize(30, 1560000))
        self.flagn19_lineEdit.setFont(font)
        self.flagn19_lineEdit.setFrame(True)
        self.flagn19_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stoWalking_Flag1_horizontalLayout.addWidget(self.flagn19_lineEdit)


        self.verticalLayout_4.addLayout(self.stoWalking_Flag1_horizontalLayout)

        self.stoWalking_Flag2_horizontalLayout = QHBoxLayout()
        self.stoWalking_Flag2_horizontalLayout.setSpacing(0)
        self.stoWalking_Flag2_horizontalLayout.setObjectName(u"stoWalking_Flag2_horizontalLayout")
        self.flagn17_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flagn17_label.setObjectName(u"flagn17_label")
        self.flagn17_label.setFont(font)
        self.flagn17_label.setFrameShape(QFrame.Shape.Box)
        self.flagn17_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn17_label.setWordWrap(True)

        self.stoWalking_Flag2_horizontalLayout.addWidget(self.flagn17_label)

        self.flagn16_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flagn16_lineEdit.setObjectName(u"flagn16_lineEdit")
        self.flagn16_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn16_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn16_lineEdit.setFont(font)
        self.flagn16_lineEdit.setFrame(True)
        self.flagn16_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stoWalking_Flag2_horizontalLayout.addWidget(self.flagn16_lineEdit)


        self.verticalLayout_4.addLayout(self.stoWalking_Flag2_horizontalLayout)

        self.StopWalking_Flag1and14_horizontalLayout = QHBoxLayout()
        self.StopWalking_Flag1and14_horizontalLayout.setSpacing(0)
        self.StopWalking_Flag1and14_horizontalLayout.setObjectName(u"StopWalking_Flag1and14_horizontalLayout")
        self.StopWalking_Flag1and14_verticalLayout = QVBoxLayout()
        self.StopWalking_Flag1and14_verticalLayout.setSpacing(0)
        self.StopWalking_Flag1and14_verticalLayout.setObjectName(u"StopWalking_Flag1and14_verticalLayout")
        self.flagn18_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flagn18_label.setObjectName(u"flagn18_label")
        self.flagn18_label.setFont(font)
        self.flagn18_label.setFrameShape(QFrame.Shape.Box)
        self.flagn18_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn18_label.setWordWrap(True)

        self.StopWalking_Flag1and14_verticalLayout.addWidget(self.flagn18_label)

        self.flagn19_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flagn19_label.setObjectName(u"flagn19_label")
        self.flagn19_label.setFont(font)
        self.flagn19_label.setFrameShape(QFrame.Shape.Box)
        self.flagn19_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn19_label.setWordWrap(True)

        self.StopWalking_Flag1and14_verticalLayout.addWidget(self.flagn19_label)


        self.StopWalking_Flag1and14_horizontalLayout.addLayout(self.StopWalking_Flag1and14_verticalLayout)

        self.flagn17_and_flagn18_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flagn17_and_flagn18_lineEdit.setObjectName(u"flagn17_and_flagn18_lineEdit")
        self.flagn17_and_flagn18_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn17_and_flagn18_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn17_and_flagn18_lineEdit.setFont(font)
        self.flagn17_and_flagn18_lineEdit.setFrame(True)
        self.flagn17_and_flagn18_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.StopWalking_Flag1and14_horizontalLayout.addWidget(self.flagn17_and_flagn18_lineEdit)


        self.verticalLayout_4.addLayout(self.StopWalking_Flag1and14_horizontalLayout)


        self.horizontalLayout.addWidget(self.stopWalking_Frame)

        self.ss2w_Frame = QFrame(self.frame)
        self.ss2w_Frame.setObjectName(u"ss2w_Frame")
        self.ss2w_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.ss2w_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ss2w_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ss2w_verticalLayout = QVBoxLayout()
        self.ss2w_verticalLayout.setSpacing(0)
        self.ss2w_verticalLayout.setObjectName(u"ss2w_verticalLayout")
        self.ss2w_label = ColorChangingFrame(self.ss2w_Frame)
        self.ss2w_label.setObjectName(u"ss2w_label")
        self.ss2w_label.setMaximumSize(QSize(900, 18))
        self.ss2w_label.setFont(font)
        self.ss2w_label.setFrameShape(QFrame.Shape.Box)
        self.ss2w_label.setFrameShadow(QFrame.Shadow.Plain)
        self.ss2w_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.ss2w_label)

        self.flagn3_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn3_label.setObjectName(u"flagn3_label")
        self.flagn3_label.setMaximumSize(QSize(900, 18))
        self.flagn3_label.setFont(font)
        self.flagn3_label.setFrameShape(QFrame.Shape.Box)
        self.flagn3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.flagn3_label)

        self.stateNumber1_Label = ColorChangingFrame(self.ss2w_Frame)
        self.stateNumber1_Label.setObjectName(u"stateNumber1_Label")
        self.stateNumber1_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber1_Label.setFont(font)
        self.stateNumber1_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber1_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.stateNumber1_Label)

        self.wstartHipTh_horizontalLayout = QHBoxLayout()
        self.wstartHipTh_horizontalLayout.setSpacing(0)
        self.wstartHipTh_horizontalLayout.setObjectName(u"wstartHipTh_horizontalLayout")
        self.walkingStart_Flag12_verticalLayout = QVBoxLayout()
        self.walkingStart_Flag12_verticalLayout.setSpacing(0)
        self.walkingStart_Flag12_verticalLayout.setObjectName(u"walkingStart_Flag12_verticalLayout")
        self.flagn20_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn20_label.setObjectName(u"flagn20_label")
        self.flagn20_label.setFont(font)
        self.flagn20_label.setFrameShape(QFrame.Shape.Box)
        self.flagn20_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn20_label.setWordWrap(True)

        self.walkingStart_Flag12_verticalLayout.addWidget(self.flagn20_label)

        self.flagn21_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn21_label.setObjectName(u"flagn21_label")
        self.flagn21_label.setFont(font)
        self.flagn21_label.setFrameShape(QFrame.Shape.Box)
        self.flagn21_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn21_label.setWordWrap(True)

        self.walkingStart_Flag12_verticalLayout.addWidget(self.flagn21_label)


        self.wstartHipTh_horizontalLayout.addLayout(self.walkingStart_Flag12_verticalLayout)

        self.flagn20_and_flagn21_lineEdit = QLineEdit(self.ss2w_Frame)
        self.flagn20_and_flagn21_lineEdit.setObjectName(u"flagn20_and_flagn21_lineEdit")
        self.flagn20_and_flagn21_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn20_and_flagn21_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flagn20_and_flagn21_lineEdit.setFont(font)
        self.flagn20_and_flagn21_lineEdit.setFrame(True)
        self.flagn20_and_flagn21_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn20_and_flagn21_lineEdit.textChanged.connect(
            lambda txt:self.label.setText(txt)
        )

        self.wstartHipTh_horizontalLayout.addWidget(self.flagn20_and_flagn21_lineEdit)


        self.ss2w_verticalLayout.addLayout(self.wstartHipTh_horizontalLayout)

        self.walkingStart_Flag3_horizontalLayout = QHBoxLayout()
        self.walkingStart_Flag3_horizontalLayout.setSpacing(0)
        self.walkingStart_Flag3_horizontalLayout.setObjectName(u"walkingStart_Flag3_horizontalLayout")
        self.flagn22_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn22_label.setObjectName(u"flagn22_label")
        self.flagn22_label.setMinimumSize(QSize(80, 0))
        self.flagn22_label.setFont(font)
        self.flagn22_label.setFrameShape(QFrame.Shape.Box)
        self.flagn22_label.setTextFormat(Qt.TextFormat.AutoText)
        self.flagn22_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn22_label.setWordWrap(True)

        self.walkingStart_Flag3_horizontalLayout.addWidget(self.flagn22_label)

        self.flagn22_lineEdit = QLineEdit(self.ss2w_Frame)
        self.flagn22_lineEdit.setObjectName(u"flagn22_lineEdit")
        self.flagn22_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn22_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flagn22_lineEdit.setFont(font)
        self.flagn22_lineEdit.setFrame(True)
        self.flagn22_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.walkingStart_Flag3_horizontalLayout.addWidget(self.flagn22_lineEdit)


        self.ss2w_verticalLayout.addLayout(self.walkingStart_Flag3_horizontalLayout)

        self.flagn23_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn23_label.setObjectName(u"flagn23_label")
        self.flagn23_label.setMaximumSize(QSize(16777215, 18))
        self.flagn23_label.setFont(font)
        self.flagn23_label.setFrameShape(QFrame.Shape.Box)
        self.flagn23_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn23_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flagn23_label)

        self.flagn24_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn24_label.setObjectName(u"flagn24_label")
        self.flagn24_label.setMaximumSize(QSize(16777215, 18))
        self.flagn24_label.setFont(font)
        self.flagn24_label.setFrameShape(QFrame.Shape.Box)
        self.flagn24_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn24_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flagn24_label)

        self.flagn25_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn25_label.setObjectName(u"flagn25_label")
        self.flagn25_label.setMaximumSize(QSize(16777215, 18))
        self.flagn25_label.setFont(font)
        self.flagn25_label.setFrameShape(QFrame.Shape.Box)
        self.flagn25_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn25_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flagn25_label)

        self.flagn26_label = ColorChangingFrame(self.ss2w_Frame)
        self.flagn26_label.setObjectName(u"flagn26_label")
        self.flagn26_label.setMaximumSize(QSize(16777215, 18))
        self.flagn26_label.setFont(font)
        self.flagn26_label.setFrameShape(QFrame.Shape.Box)
        self.flagn26_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn26_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flagn26_label)


        self.horizontalLayout_3.addLayout(self.ss2w_verticalLayout)


        self.horizontalLayout.addWidget(self.ss2w_Frame)

        self.walking_verticalLayout = QVBoxLayout()
        self.walking_verticalLayout.setSpacing(0)
        self.walking_verticalLayout.setObjectName(u"walking_verticalLayout")
        self.walking_w_label = ColorChangingFrame(self.frame)
        self.walking_w_label.setObjectName(u"walking_w_label")
        self.walking_w_label.setFont(font)
        self.walking_w_label.setFrameShape(QFrame.Shape.Box)
        self.walking_w_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.walking_verticalLayout.addWidget(self.walking_w_label)

        self.walikng_horizontalLayout = QHBoxLayout()
        self.walikng_horizontalLayout.setSpacing(0)
        self.walikng_horizontalLayout.setObjectName(u"walikng_horizontalLayout")
        self.RLS_Frame = QFrame(self.frame)
        self.RLS_Frame.setObjectName(u"RLS_Frame")
        self.RLS_Frame.setFrameShape(QFrame.Shape.Box)
        self.RLS_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.RLS_Frame.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.RLS_Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.RLS_verticalLayout = QVBoxLayout()
        self.RLS_verticalLayout.setSpacing(0)
        self.RLS_verticalLayout.setObjectName(u"RLS_verticalLayout")
        self.flagn4_label = ColorChangingFrame(self.RLS_Frame)
        self.flagn4_label.setObjectName(u"flagn4_label")
        self.flagn4_label.setMinimumSize(QSize(0, 18))
        self.flagn4_label.setMaximumSize(QSize(16777215, 18))
        self.flagn4_label.setFont(font)
        self.flagn4_label.setFrameShape(QFrame.Shape.Box)
        self.flagn4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RLS_verticalLayout.addWidget(self.flagn4_label)

        self.stateNumber2_label = ColorChangingFrame(self.RLS_Frame)
        self.stateNumber2_label.setObjectName(u"stateNumber2_label")
        self.stateNumber2_label.setMinimumSize(QSize(0, 18))
        self.stateNumber2_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber2_label.setFont(font)
        self.stateNumber2_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RLS_verticalLayout.addWidget(self.stateNumber2_label)

        self.RLS_Flag1_horizontallLayout = QHBoxLayout()
        self.RLS_Flag1_horizontallLayout.setSpacing(0)
        self.RLS_Flag1_horizontallLayout.setObjectName(u"RLS_Flag1_horizontallLayout")
        self.flagn27_label = ColorChangingFrame(self.RLS_Frame)
        self.flagn27_label.setObjectName(u"flagn27_label")
        self.flagn27_label.setMinimumSize(QSize(0, 0))
        self.flagn27_label.setMaximumSize(QSize(8000, 900))
        self.flagn27_label.setFont(font)
        self.flagn27_label.setFrameShape(QFrame.Shape.Box)
        self.flagn27_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn27_label.setWordWrap(True)

        self.RLS_Flag1_horizontallLayout.addWidget(self.flagn27_label)

        self.label = QLabel(self.RLS_Frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.Box)

        self.RLS_Flag1_horizontallLayout.addWidget(self.label)


        self.RLS_verticalLayout.addLayout(self.RLS_Flag1_horizontallLayout)

        self.RLS_Flag1_horizontallLayout_3 = QHBoxLayout()
        self.RLS_Flag1_horizontallLayout_3.setSpacing(0)
        self.RLS_Flag1_horizontallLayout_3.setObjectName(u"RLS_Flag1_horizontallLayout_3")
        self.flagn28_label = ColorChangingFrame(self.RLS_Frame)
        self.flagn28_label.setObjectName(u"flagn28_label")
        self.flagn28_label.setMinimumSize(QSize(0, 0))
        self.flagn28_label.setMaximumSize(QSize(8000, 900))
        self.flagn28_label.setFont(font)
        self.flagn28_label.setFrameShape(QFrame.Shape.Box)
        self.flagn28_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn28_label.setWordWrap(True)

        self.RLS_Flag1_horizontallLayout_3.addWidget(self.flagn28_label)

        self.flagn28_lineEdit = QLineEdit(self.RLS_Frame)
        self.flagn28_lineEdit.setObjectName(u"flagn28_lineEdit")
        self.flagn28_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn28_lineEdit.setMaximumSize(QSize(30, 900))
        self.flagn28_lineEdit.setFont(font)
        self.flagn28_lineEdit.setFrame(True)
        self.flagn28_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.flagn28_lineEdit.textChanged.connect(
            lambda txt: self.flagn29_lineEdit.setText(txt)
        )

        self.RLS_Flag1_horizontallLayout_3.addWidget(self.flagn28_lineEdit)


        self.RLS_verticalLayout.addLayout(self.RLS_Flag1_horizontallLayout_3)


        self.horizontalLayout_6.addLayout(self.RLS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RLS_Frame)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.flagn5_label = ColorChangingFrame(self.frame_6)
        self.flagn5_label.setObjectName(u"flagn5_label")
        self.flagn5_label.setEnabled(True)
        self.flagn5_label.setMinimumSize(QSize(120, 18))
        self.flagn5_label.setMaximumSize(QSize(1550, 18))
        self.flagn5_label.setFont(font)
        self.flagn5_label.setFrameShape(QFrame.Shape.Box)
        self.flagn5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.flagn5_label)

        self.stateNumber3_label = ColorChangingFrame(self.frame_6)
        self.stateNumber3_label.setObjectName(u"stateNumber3_label")
        self.stateNumber3_label.setMinimumSize(QSize(120, 18))
        self.stateNumber3_label.setMaximumSize(QSize(1550, 18))
        self.stateNumber3_label.setFont(font)
        self.stateNumber3_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.stateNumber3_label)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.RHS_Flag1_horizontalLayout = QHBoxLayout()
        self.RHS_Flag1_horizontalLayout.setSpacing(0)
        self.RHS_Flag1_horizontalLayout.setObjectName(u"RHS_Flag1_horizontalLayout")
        self.flagn29_label = ColorChangingFrame(self.frame_6)
        self.flagn29_label.setObjectName(u"flagn29_label")
        self.flagn29_label.setFont(font)
        self.flagn29_label.setFrameShape(QFrame.Shape.Box)
        self.flagn29_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn29_label.setWordWrap(True)

        self.RHS_Flag1_horizontalLayout.addWidget(self.flagn29_label)

        self.flagn29_lineEdit = QLabel(self.frame_6)
        self.flagn29_lineEdit.setObjectName(u"flagn29_lineEdit")
        self.flagn29_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn29_lineEdit.setMaximumSize(QSize(30, 500))
        self.flagn29_lineEdit.setFont(font)
        self.flagn29_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        


        self.RHS_Flag1_horizontalLayout.addWidget(self.flagn29_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag1_horizontalLayout)

        self.RHS_Flag2_horizontalLayout = QHBoxLayout()
        self.RHS_Flag2_horizontalLayout.setSpacing(0)
        self.RHS_Flag2_horizontalLayout.setObjectName(u"RHS_Flag2_horizontalLayout")
        self.flagn30_label = ColorChangingFrame(self.frame_6)
        self.flagn30_label.setObjectName(u"flagn30_label")
        self.flagn30_label.setFont(font)
        self.flagn30_label.setFrameShape(QFrame.Shape.Box)
        self.flagn30_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn30_label.setWordWrap(True)

        self.RHS_Flag2_horizontalLayout.addWidget(self.flagn30_label)

        self.flagn30_lineEdit = QLineEdit(self.frame_6)
        self.flagn30_lineEdit.setObjectName(u"flagn30_lineEdit")
        self.flagn30_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn30_lineEdit.setMaximumSize(QSize(30, 500))
        self.flagn30_lineEdit.setFont(font)
        self.flagn30_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RHS_Flag2_horizontalLayout.addWidget(self.flagn30_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag2_horizontalLayout)

        self.RHS_Flag3_horizontalLayout = QHBoxLayout()
        self.RHS_Flag3_horizontalLayout.setSpacing(0)
        self.RHS_Flag3_horizontalLayout.setObjectName(u"RHS_Flag3_horizontalLayout")
        self.flagn31_label = ColorChangingFrame(self.frame_6)
        self.flagn31_label.setObjectName(u"flagn31_label")
        self.flagn31_label.setFont(font)
        self.flagn31_label.setFrameShape(QFrame.Shape.Box)
        self.flagn31_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn31_label.setWordWrap(True)

        self.RHS_Flag3_horizontalLayout.addWidget(self.flagn31_label)

        self.flagn32_label = ColorChangingFrame(self.frame_6)
        self.flagn32_label.setObjectName(u"flagn32_label")
        self.flagn32_label.setFont(font)
        self.flagn32_label.setFrameShape(QFrame.Shape.Box)
        self.flagn32_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn32_label.setWordWrap(True)

        self.RHS_Flag3_horizontalLayout.addWidget(self.flagn32_label)

        self.flagn31_and_flagn32_lineEdit = QLineEdit(self.frame_6)
        self.flagn31_and_flagn32_lineEdit.setObjectName(u"flagn31_and_flagn32_lineEdit")
        self.flagn31_and_flagn32_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn31_and_flagn32_lineEdit.setMaximumSize(QSize(30, 500))
        self.flagn31_and_flagn32_lineEdit.setFont(font)
        self.flagn31_and_flagn32_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn31_and_flagn32_lineEdit.textChanged.connect(
            lambda txt:self.label_8.setText(txt)
        )

        self.RHS_Flag3_horizontalLayout.addWidget(self.flagn31_and_flagn32_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag3_horizontalLayout)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.walikng_horizontalLayout.addWidget(self.frame_6)

        self.LHO2MF_Frame = QFrame(self.frame)
        self.LHO2MF_Frame.setObjectName(u"LHO2MF_Frame")
        self.LHO2MF_Frame.setFrameShape(QFrame.Shape.Box)
        self.LHO2MF_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.LHO2MF_Frame.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.LHO2MF_Frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.LHO2MF_Flag1_verticalLayout = QVBoxLayout()
        self.LHO2MF_Flag1_verticalLayout.setSpacing(0)
        self.LHO2MF_Flag1_verticalLayout.setObjectName(u"LHO2MF_Flag1_verticalLayout")
        self.flagn6_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.flagn6_label.setObjectName(u"flagn6_label")
        self.flagn6_label.setMinimumSize(QSize(120, 18))
        self.flagn6_label.setMaximumSize(QSize(1550, 18))
        self.flagn6_label.setFont(font)
        self.flagn6_label.setFrameShape(QFrame.Shape.Box)
        self.flagn6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LHO2MF_Flag1_verticalLayout.addWidget(self.flagn6_label)

        self.stateNumber4_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.stateNumber4_label.setObjectName(u"stateNumber4_label")
        self.stateNumber4_label.setMinimumSize(QSize(120, 18))
        self.stateNumber4_label.setMaximumSize(QSize(1550, 18))
        self.stateNumber4_label.setFont(font)
        self.stateNumber4_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LHO2MF_Flag1_verticalLayout.addWidget(self.stateNumber4_label)

        self.LHO2MF_Flag1_horizontalLayout = QHBoxLayout()
        self.LHO2MF_Flag1_horizontalLayout.setSpacing(0)
        self.LHO2MF_Flag1_horizontalLayout.setObjectName(u"LHO2MF_Flag1_horizontalLayout")
        self.flagn33_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.flagn33_label.setObjectName(u"flagn33_label")
        self.flagn33_label.setMaximumSize(QSize(8000, 16777215))
        self.flagn33_label.setFont(font)
        self.flagn33_label.setFrameShape(QFrame.Shape.Box)
        self.flagn33_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn33_label.setWordWrap(True)
        self.flagn33_label.setMargin(0)

        self.LHO2MF_Flag1_horizontalLayout.addWidget(self.flagn33_label)

        self.flagn33_lineEdit = QLineEdit(self.LHO2MF_Frame)
        self.flagn33_lineEdit.setObjectName(u"flagn33_lineEdit")
        self.flagn33_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn33_lineEdit.setMaximumSize(QSize(30, 1500))
        self.flagn33_lineEdit.setFont(font)
        self.flagn33_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LHO2MF_Flag1_horizontalLayout.addWidget(self.flagn33_lineEdit)


        self.LHO2MF_Flag1_verticalLayout.addLayout(self.LHO2MF_Flag1_horizontalLayout)


        self.horizontalLayout_17.addLayout(self.LHO2MF_Flag1_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LHO2MF_Frame)

        self.LF2ET_Frame = QFrame(self.frame)
        self.LF2ET_Frame.setObjectName(u"LF2ET_Frame")
        self.LF2ET_Frame.setFrameShape(QFrame.Shape.Box)
        self.LF2ET_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.LF2ET_Frame.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.LF2ET_Frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.LF2ET_verticalLayout = QVBoxLayout()
        self.LF2ET_verticalLayout.setSpacing(0)
        self.LF2ET_verticalLayout.setObjectName(u"LF2ET_verticalLayout")
        self.flagn7_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flagn7_label.setObjectName(u"flagn7_label")
        self.flagn7_label.setMinimumSize(QSize(0, 18))
        self.flagn7_label.setMaximumSize(QSize(16777215, 18))
        self.flagn7_label.setFont(font)
        self.flagn7_label.setFrameShape(QFrame.Shape.Box)
        self.flagn7_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LF2ET_verticalLayout.addWidget(self.flagn7_label)

        self.stateNumber5_label = ColorChangingFrame(self.LF2ET_Frame)
        self.stateNumber5_label.setObjectName(u"stateNumber5_label")
        self.stateNumber5_label.setMinimumSize(QSize(0, 18))
        self.stateNumber5_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber5_label.setFont(font)
        self.stateNumber5_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LF2ET_verticalLayout.addWidget(self.stateNumber5_label)

        self.LF2ET_Flag12_verticalLayout = QVBoxLayout()
        self.LF2ET_Flag12_verticalLayout.setSpacing(0)
        self.LF2ET_Flag12_verticalLayout.setObjectName(u"LF2ET_Flag12_verticalLayout")
        self.LF2ET_Flag1_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag1_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag1_horizontalLayout.setObjectName(u"LF2ET_Flag1_horizontalLayout")
        self.flagn34_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flagn34_label.setObjectName(u"flagn34_label")
        self.flagn34_label.setFont(font)
        self.flagn34_label.setFrameShape(QFrame.Shape.Box)
        self.flagn34_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn34_label.setWordWrap(True)

        self.LF2ET_Flag1_horizontalLayout.addWidget(self.flagn34_label)

        self.label_2 = QLabel(self.LF2ET_Frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(7)
        self.label_2.setFont(font1)
        self.label_2.setFrameShape(QFrame.Shape.Box)

        self.LF2ET_Flag1_horizontalLayout.addWidget(self.label_2)


        self.LF2ET_Flag12_verticalLayout.addLayout(self.LF2ET_Flag1_horizontalLayout)

        self.StandingStill_label_23 = ColorChangingFrame(self.LF2ET_Frame)
        self.StandingStill_label_23.setObjectName(u"StandingStill_label_23")
        self.StandingStill_label_23.setFont(font)
        self.StandingStill_label_23.setFrameShape(QFrame.Shape.Box)
        self.StandingStill_label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LF2ET_Flag12_verticalLayout.addWidget(self.StandingStill_label_23)

        self.LF2ET_Flag2_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag2_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag2_horizontalLayout.setObjectName(u"LF2ET_Flag2_horizontalLayout")
        self.flagn35_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flagn35_label.setObjectName(u"flagn35_label")
        self.flagn35_label.setFont(font)
        self.flagn35_label.setFrameShape(QFrame.Shape.Box)
        self.flagn35_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn35_label.setWordWrap(True)

        self.LF2ET_Flag2_horizontalLayout.addWidget(self.flagn35_label)

        self.label_3 = QLabel(self.LF2ET_Frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Shape.Box)

        self.LF2ET_Flag2_horizontalLayout.addWidget(self.label_3)


        self.LF2ET_Flag12_verticalLayout.addLayout(self.LF2ET_Flag2_horizontalLayout)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag12_verticalLayout)

        self.LF2ET_Flag3_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag3_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag3_horizontalLayout.setObjectName(u"LF2ET_Flag3_horizontalLayout")
        self.flagn36_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flagn36_label.setObjectName(u"flagn36_label")
        self.flagn36_label.setFont(font)
        self.flagn36_label.setFrameShape(QFrame.Shape.Box)
        self.flagn36_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn36_label.setWordWrap(True)

        self.LF2ET_Flag3_horizontalLayout.addWidget(self.flagn36_label)

        self.label_4 = QLabel(self.LF2ET_Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.Shape.Box)

        self.LF2ET_Flag3_horizontalLayout.addWidget(self.label_4)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag3_horizontalLayout)

        self.LF2ET_Flag4_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag4_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag4_horizontalLayout.setObjectName(u"LF2ET_Flag4_horizontalLayout")
        self.flagn37_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flagn37_label.setObjectName(u"flagn37_label")
        self.flagn37_label.setFont(font)
        self.flagn37_label.setFrameShape(QFrame.Shape.Box)
        self.flagn37_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn37_label.setWordWrap(True)

        self.LF2ET_Flag4_horizontalLayout.addWidget(self.flagn37_label)

        self.flagn37_lineEdit = QLineEdit(self.LF2ET_Frame)
        self.flagn37_lineEdit.setObjectName(u"flagn37_lineEdit")
        self.flagn37_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn37_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flagn37_lineEdit.setFont(font)
        self.flagn37_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn37_lineEdit.textChanged.connect(
            lambda txt:self.label_5.setText(txt)
        )

        self.LF2ET_Flag4_horizontalLayout.addWidget(self.flagn37_lineEdit)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag4_horizontalLayout)


        self.horizontalLayout_16.addLayout(self.LF2ET_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LF2ET_Frame)

        self.Lextension_Frame = QFrame(self.frame)
        self.Lextension_Frame.setObjectName(u"Lextension_Frame")
        self.Lextension_Frame.setFrameShape(QFrame.Shape.Box)
        self.Lextension_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.Lextension_Frame.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.Lextension_Frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Lextension_verticalLayout = QVBoxLayout()
        self.Lextension_verticalLayout.setSpacing(0)
        self.Lextension_verticalLayout.setObjectName(u"Lextension_verticalLayout")
        self.flagn8_label = ColorChangingFrame(self.Lextension_Frame)
        self.flagn8_label.setObjectName(u"flagn8_label")
        self.flagn8_label.setMinimumSize(QSize(0, 18))
        self.flagn8_label.setMaximumSize(QSize(16777215, 18))
        self.flagn8_label.setFont(font)
        self.flagn8_label.setFrameShape(QFrame.Shape.Box)
        self.flagn8_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Lextension_verticalLayout.addWidget(self.flagn8_label)

        self.stateNumber6_label = ColorChangingFrame(self.Lextension_Frame)
        self.stateNumber6_label.setObjectName(u"stateNumber6_label")
        self.stateNumber6_label.setMinimumSize(QSize(0, 18))
        self.stateNumber6_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber6_label.setFont(font)
        self.stateNumber6_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Lextension_verticalLayout.addWidget(self.stateNumber6_label)

        self.Lextension_Flag1_horizontalLayout = QHBoxLayout()
        self.Lextension_Flag1_horizontalLayout.setSpacing(0)
        self.Lextension_Flag1_horizontalLayout.setObjectName(u"Lextension_Flag1_horizontalLayout")
        self.flagn38_label = ColorChangingFrame(self.Lextension_Frame)
        self.flagn38_label.setObjectName(u"flagn38_label")
        self.flagn38_label.setMaximumSize(QSize(16777215, 1000))
        self.flagn38_label.setFont(font)
        self.flagn38_label.setFrameShape(QFrame.Shape.Box)
        self.flagn38_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn38_label.setWordWrap(True)

        self.Lextension_Flag1_horizontalLayout.addWidget(self.flagn38_label)

        self.label_5 = QLabel(self.Lextension_Frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QFrame.Shape.Box)

        self.Lextension_Flag1_horizontalLayout.addWidget(self.label_5)


        self.Lextension_verticalLayout.addLayout(self.Lextension_Flag1_horizontalLayout)


        self.horizontalLayout_19.addLayout(self.Lextension_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Lextension_Frame)

        self.Lextended_Frame = QFrame(self.frame)
        self.Lextended_Frame.setObjectName(u"Lextended_Frame")
        self.Lextended_Frame.setFrameShape(QFrame.Shape.Box)
        self.Lextended_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.Lextended_Frame.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.Lextended_Frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Lextended_verticalLayout = QVBoxLayout()
        self.Lextended_verticalLayout.setSpacing(0)
        self.Lextended_verticalLayout.setObjectName(u"Lextended_verticalLayout")
        self.flagn9_label = ColorChangingFrame(self.Lextended_Frame)
        self.flagn9_label.setObjectName(u"flagn9_label")
        self.flagn9_label.setMinimumSize(QSize(0, 18))
        self.flagn9_label.setMaximumSize(QSize(16777215, 18))
        self.flagn9_label.setFont(font)
        self.flagn9_label.setFrameShape(QFrame.Shape.Box)
        self.flagn9_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Lextended_verticalLayout.addWidget(self.flagn9_label)

        self.stateNumber7_label = ColorChangingFrame(self.Lextended_Frame)
        self.stateNumber7_label.setObjectName(u"stateNumber7_label")
        self.stateNumber7_label.setMinimumSize(QSize(0, 18))
        self.stateNumber7_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber7_label.setFont(font)
        self.stateNumber7_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber7_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Lextended_verticalLayout.addWidget(self.stateNumber7_label)

        self.Lextended_Flag1_horizontalLayout = QHBoxLayout()
        self.Lextended_Flag1_horizontalLayout.setSpacing(0)
        self.Lextended_Flag1_horizontalLayout.setObjectName(u"Lextended_Flag1_horizontalLayout")
        self.flagn39_label = ColorChangingFrame(self.Lextended_Frame)
        self.flagn39_label.setObjectName(u"flagn39_label")
        self.flagn39_label.setFont(font)
        self.flagn39_label.setFrameShape(QFrame.Shape.Box)
        self.flagn39_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn39_label.setWordWrap(True)

        self.Lextended_Flag1_horizontalLayout.addWidget(self.flagn39_label)

        self.label_6 = QLabel(self.Lextended_Frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.Shape.Box)

        self.Lextended_Flag1_horizontalLayout.addWidget(self.label_6)


        self.Lextended_verticalLayout.addLayout(self.Lextended_Flag1_horizontalLayout)


        self.horizontalLayout_21.addLayout(self.Lextended_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Lextended_Frame)

        self.LLS_Frame = QFrame(self.frame)
        self.LLS_Frame.setObjectName(u"LLS_Frame")
        self.LLS_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.LLS_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.LLS_Frame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LLS_verticalLayout = QVBoxLayout()
        self.LLS_verticalLayout.setSpacing(0)
        self.LLS_verticalLayout.setObjectName(u"LLS_verticalLayout")
        self.flagn10_label = ColorChangingFrame(self.LLS_Frame)
        self.flagn10_label.setObjectName(u"flagn10_label")
        self.flagn10_label.setMinimumSize(QSize(0, 18))
        self.flagn10_label.setMaximumSize(QSize(16777215, 18))
        self.flagn10_label.setFont(font)
        self.flagn10_label.setFrameShape(QFrame.Shape.Box)
        self.flagn10_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LLS_verticalLayout.addWidget(self.flagn10_label)

        self.stateNumber8_label = ColorChangingFrame(self.LLS_Frame)
        self.stateNumber8_label.setObjectName(u"stateNumber8_label")
        self.stateNumber8_label.setMinimumSize(QSize(0, 18))
        self.stateNumber8_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber8_label.setFont(font)
        self.stateNumber8_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber8_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LLS_verticalLayout.addWidget(self.stateNumber8_label)

        self.LLS_Flag1_horizontalLayout = QHBoxLayout()
        self.LLS_Flag1_horizontalLayout.setSpacing(0)
        self.LLS_Flag1_horizontalLayout.setObjectName(u"LLS_Flag1_horizontalLayout")
        self.flagn40_label = ColorChangingFrame(self.LLS_Frame)
        self.flagn40_label.setObjectName(u"flagn40_label")
        self.flagn40_label.setMinimumSize(QSize(0, 0))
        self.flagn40_label.setMaximumSize(QSize(16777215, 1000))
        self.flagn40_label.setFont(font)
        self.flagn40_label.setFrameShape(QFrame.Shape.Box)
        self.flagn40_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn40_label.setWordWrap(True)

        self.LLS_Flag1_horizontalLayout.addWidget(self.flagn40_label)

        self.flagn40_lineEdit = QLineEdit(self.LLS_Frame)
        self.flagn40_lineEdit.setObjectName(u"flagn40_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flagn40_lineEdit.sizePolicy().hasHeightForWidth())
        self.flagn40_lineEdit.setSizePolicy(sizePolicy)
        self.flagn40_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn40_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flagn40_lineEdit.setFont(font)
        self.flagn40_lineEdit.setFrame(True)
        self.flagn40_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn40_lineEdit.textChanged.connect(
            lambda txt:self.label_7.setText(txt)
        )

        self.LLS_Flag1_horizontalLayout.addWidget(self.flagn40_lineEdit)


        self.LLS_verticalLayout.addLayout(self.LLS_Flag1_horizontalLayout)


        self.horizontalLayout_23.addLayout(self.LLS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LLS_Frame)

        self.LHS_Frame = QFrame(self.frame)
        self.LHS_Frame.setObjectName(u"LHS_Frame")
        self.LHS_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.LHS_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_28 = QHBoxLayout(self.LHS_Frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.LHS_verticalLayout = QVBoxLayout()
        self.LHS_verticalLayout.setSpacing(0)
        self.LHS_verticalLayout.setObjectName(u"LHS_verticalLayout")
        self.flagn11_label = ColorChangingFrame(self.LHS_Frame)
        self.flagn11_label.setObjectName(u"flagn11_label")
        self.flagn11_label.setMinimumSize(QSize(0, 18))
        self.flagn11_label.setMaximumSize(QSize(16777215, 18))
        self.flagn11_label.setFont(font)
        self.flagn11_label.setFrameShape(QFrame.Shape.Box)
        self.flagn11_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn11_label.setWordWrap(True)

        self.LHS_verticalLayout.addWidget(self.flagn11_label)

        self.stateNumber9_label = ColorChangingFrame(self.LHS_Frame)
        self.stateNumber9_label.setObjectName(u"stateNumber9_label")
        self.stateNumber9_label.setMinimumSize(QSize(0, 18))
        self.stateNumber9_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber9_label.setFont(font)
        self.stateNumber9_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber9_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber9_label.setWordWrap(True)

        self.LHS_verticalLayout.addWidget(self.stateNumber9_label)

        self.LHS_SubverticalLayout = QVBoxLayout()
        self.LHS_SubverticalLayout.setSpacing(0)
        self.LHS_SubverticalLayout.setObjectName(u"LHS_SubverticalLayout")
        self.LHS_Flag1_horizontalLayout = QHBoxLayout()
        self.LHS_Flag1_horizontalLayout.setSpacing(0)
        self.LHS_Flag1_horizontalLayout.setObjectName(u"LHS_Flag1_horizontalLayout")
        self.flagn41_label = ColorChangingFrame(self.LHS_Frame)
        self.flagn41_label.setObjectName(u"flagn41_label")
        self.flagn41_label.setMinimumSize(QSize(0, 0))
        self.flagn41_label.setMaximumSize(QSize(16777215, 5000))
        self.flagn41_label.setFont(font)
        self.flagn41_label.setFrameShape(QFrame.Shape.Box)
        self.flagn41_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn41_label.setWordWrap(True)

        self.LHS_Flag1_horizontalLayout.addWidget(self.flagn41_label)

        self.label_7 = QLabel(self.LHS_Frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.LHS_Flag1_horizontalLayout.addWidget(self.label_7)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag1_horizontalLayout)

        self.LHS_Flag2_horizontalLayout = QHBoxLayout()
        self.LHS_Flag2_horizontalLayout.setSpacing(0)
        self.LHS_Flag2_horizontalLayout.setObjectName(u"LHS_Flag2_horizontalLayout")
        self.flagn42_label = ColorChangingFrame(self.LHS_Frame)
        self.flagn42_label.setObjectName(u"flagn42_label")
        self.flagn42_label.setMinimumSize(QSize(0, 0))
        self.flagn42_label.setMaximumSize(QSize(16777215, 5000))
        self.flagn42_label.setFont(font)
        self.flagn42_label.setFrameShape(QFrame.Shape.Box)
        self.flagn42_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn42_label.setWordWrap(True)

        self.LHS_Flag2_horizontalLayout.addWidget(self.flagn42_label)

        self.flagn42_lineEdit = QLineEdit(self.LHS_Frame)
        self.flagn42_lineEdit.setObjectName(u"flagn42_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.flagn42_lineEdit.sizePolicy().hasHeightForWidth())
        self.flagn42_lineEdit.setSizePolicy(sizePolicy1)
        self.flagn42_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flagn42_lineEdit.setFont(font)
        self.flagn42_lineEdit.setFrame(True)
        self.flagn42_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LHS_Flag2_horizontalLayout.addWidget(self.flagn42_lineEdit)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag2_horizontalLayout)

        self.LHS_Flag3_horizontalLayout = QHBoxLayout()
        self.LHS_Flag3_horizontalLayout.setSpacing(0)
        self.LHS_Flag3_horizontalLayout.setObjectName(u"LHS_Flag3_horizontalLayout")
        self.flagn43_label = ColorChangingFrame(self.LHS_Frame)
        self.flagn43_label.setObjectName(u"flagn43_label")
        self.flagn43_label.setMinimumSize(QSize(0, 0))
        self.flagn43_label.setMaximumSize(QSize(16777215, 5000))
        self.flagn43_label.setFont(font)
        self.flagn43_label.setFrameShape(QFrame.Shape.Box)
        self.flagn43_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn43_label.setWordWrap(True)

        self.LHS_Flag3_horizontalLayout.addWidget(self.flagn43_label)

        self.flagn44_label = ColorChangingFrame(self.LHS_Frame)
        self.flagn44_label.setObjectName(u"flagn44_label")
        self.flagn44_label.setMinimumSize(QSize(0, 0))
        self.flagn44_label.setMaximumSize(QSize(16777215, 5000))
        self.flagn44_label.setFont(font)
        self.flagn44_label.setFrameShape(QFrame.Shape.Box)
        self.flagn44_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn44_label.setWordWrap(True)

        self.LHS_Flag3_horizontalLayout.addWidget(self.flagn44_label)

        self.label_8 = QLabel(self.LHS_Frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QFrame.Shape.Box)
        self.label_8.setFrameShadow(QFrame.Shadow.Plain)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LHS_Flag3_horizontalLayout.addWidget(self.label_8)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag3_horizontalLayout)


        self.LHS_verticalLayout.addLayout(self.LHS_SubverticalLayout)


        self.horizontalLayout_28.addLayout(self.LHS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LHS_Frame)

        self.RHO2MF_Frame = QFrame(self.frame)
        self.RHO2MF_Frame.setObjectName(u"RHO2MF_Frame")
        self.RHO2MF_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.RHO2MF_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.RHO2MF_Frame.setLineWidth(0)
        self.horizontalLayout_33 = QHBoxLayout(self.RHO2MF_Frame)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.RHO2MF_verticalLayout = QVBoxLayout()
        self.RHO2MF_verticalLayout.setSpacing(0)
        self.RHO2MF_verticalLayout.setObjectName(u"RHO2MF_verticalLayout")
        self.flagn12_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.flagn12_label.setObjectName(u"flagn12_label")
        self.flagn12_label.setMinimumSize(QSize(0, 18))
        self.flagn12_label.setMaximumSize(QSize(16777215, 18))
        self.flagn12_label.setFont(font)
        self.flagn12_label.setFrameShape(QFrame.Shape.Box)
        self.flagn12_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RHO2MF_verticalLayout.addWidget(self.flagn12_label)

        self.stateNumber10_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.stateNumber10_label.setObjectName(u"stateNumber10_label")
        self.stateNumber10_label.setMinimumSize(QSize(0, 18))
        self.stateNumber10_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber10_label.setFont(font)
        self.stateNumber10_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber10_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RHO2MF_verticalLayout.addWidget(self.stateNumber10_label)

        self.RHO2MF_Flag1_horizontalLayout = QHBoxLayout()
        self.RHO2MF_Flag1_horizontalLayout.setSpacing(0)
        self.RHO2MF_Flag1_horizontalLayout.setObjectName(u"RHO2MF_Flag1_horizontalLayout")
        self.flagn45_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.flagn45_label.setObjectName(u"flagn45_label")
        self.flagn45_label.setMinimumSize(QSize(0, 0))
        self.flagn45_label.setMaximumSize(QSize(16777215, 1000))
        self.flagn45_label.setFont(font)
        self.flagn45_label.setFrameShape(QFrame.Shape.Box)
        self.flagn45_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn45_label.setWordWrap(True)

        self.RHO2MF_Flag1_horizontalLayout.addWidget(self.flagn45_label)

        self.flagn45_lineEdit = QLineEdit(self.RHO2MF_Frame)
        self.flagn45_lineEdit.setObjectName(u"flagn45_lineEdit")
        sizePolicy.setHeightForWidth(self.flagn45_lineEdit.sizePolicy().hasHeightForWidth())
        self.flagn45_lineEdit.setSizePolicy(sizePolicy)
        self.flagn45_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn45_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flagn45_lineEdit.setFont(font)
        self.flagn45_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RHO2MF_Flag1_horizontalLayout.addWidget(self.flagn45_lineEdit)


        self.RHO2MF_verticalLayout.addLayout(self.RHO2MF_Flag1_horizontalLayout)


        self.horizontalLayout_33.addLayout(self.RHO2MF_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RHO2MF_Frame)

        self.RF2ET_Frame = QFrame(self.frame)
        self.RF2ET_Frame.setObjectName(u"RF2ET_Frame")
        self.RF2ET_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.RF2ET_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_35 = QHBoxLayout(self.RF2ET_Frame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.RF2ET_verticalLayout = QVBoxLayout()
        self.RF2ET_verticalLayout.setSpacing(0)
        self.RF2ET_verticalLayout.setObjectName(u"RF2ET_verticalLayout")
        self.flagn13_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flagn13_label.setObjectName(u"flagn13_label")
        self.flagn13_label.setMinimumSize(QSize(0, 18))
        self.flagn13_label.setMaximumSize(QSize(16777215, 18))
        self.flagn13_label.setFont(font)
        self.flagn13_label.setFrameShape(QFrame.Shape.Box)
        self.flagn13_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RF2ET_verticalLayout.addWidget(self.flagn13_label)

        self.stateNumber11_label = ColorChangingFrame(self.RF2ET_Frame)
        self.stateNumber11_label.setObjectName(u"stateNumber11_label")
        self.stateNumber11_label.setMinimumSize(QSize(0, 18))
        self.stateNumber11_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber11_label.setFont(font)
        self.stateNumber11_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber11_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RF2ET_verticalLayout.addWidget(self.stateNumber11_label)

        self.RF2ET_Flag12_verticalLayout = QVBoxLayout()
        self.RF2ET_Flag12_verticalLayout.setSpacing(0)
        self.RF2ET_Flag12_verticalLayout.setObjectName(u"RF2ET_Flag12_verticalLayout")
        self.RF2ET_Flag1_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag1_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag1_horizontalLayout.setObjectName(u"RF2ET_Flag1_horizontalLayout")
        self.flagn46_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flagn46_label.setObjectName(u"flagn46_label")
        self.flagn46_label.setFont(font)
        self.flagn46_label.setFrameShape(QFrame.Shape.Box)
        self.flagn46_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn46_label.setWordWrap(True)

        self.RF2ET_Flag1_horizontalLayout.addWidget(self.flagn46_label)

        self.label_9 = QLabel(self.RF2ET_Frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.Box)

        self.RF2ET_Flag1_horizontalLayout.addWidget(self.label_9)


        self.RF2ET_Flag12_verticalLayout.addLayout(self.RF2ET_Flag1_horizontalLayout)

        self.StandingStill_label_35 = ColorChangingFrame(self.RF2ET_Frame)
        self.StandingStill_label_35.setObjectName(u"StandingStill_label_35")
        self.StandingStill_label_35.setFont(font)
        self.StandingStill_label_35.setFrameShape(QFrame.Shape.Box)
        self.StandingStill_label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RF2ET_Flag12_verticalLayout.addWidget(self.StandingStill_label_35)

        self.RF2ET_Flag2_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag2_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag2_horizontalLayout.setObjectName(u"RF2ET_Flag2_horizontalLayout")
        self.flagn47_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flagn47_label.setObjectName(u"flagn47_label")
        self.flagn47_label.setFont(font)
        self.flagn47_label.setFrameShape(QFrame.Shape.Box)
        self.flagn47_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn47_label.setWordWrap(True)

        self.RF2ET_Flag2_horizontalLayout.addWidget(self.flagn47_label)

        self.label_10 = QLabel(self.RF2ET_Frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QFrame.Shape.Box)

        self.RF2ET_Flag2_horizontalLayout.addWidget(self.label_10)


        self.RF2ET_Flag12_verticalLayout.addLayout(self.RF2ET_Flag2_horizontalLayout)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag12_verticalLayout)

        self.RF2ET_Flag3_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag3_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag3_horizontalLayout.setObjectName(u"RF2ET_Flag3_horizontalLayout")
        self.flagn48_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flagn48_label.setObjectName(u"flagn48_label")
        self.flagn48_label.setFont(font)
        self.flagn48_label.setFrameShape(QFrame.Shape.Box)
        self.flagn48_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn48_label.setWordWrap(True)

        self.RF2ET_Flag3_horizontalLayout.addWidget(self.flagn48_label)

        self.label_11 = QLabel(self.RF2ET_Frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QFrame.Shape.Box)

        self.RF2ET_Flag3_horizontalLayout.addWidget(self.label_11)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag3_horizontalLayout)

        self.RF2ET_Flag4_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag4_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag4_horizontalLayout.setObjectName(u"RF2ET_Flag4_horizontalLayout")
        self.flagn49_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flagn49_label.setObjectName(u"flagn49_label")
        self.flagn49_label.setFont(font)
        self.flagn49_label.setFrameShape(QFrame.Shape.Box)
        self.flagn49_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn49_label.setWordWrap(True)

        self.RF2ET_Flag4_horizontalLayout.addWidget(self.flagn49_label)

        self.flagn49_lineEdit = QLineEdit(self.RF2ET_Frame)
        self.flagn49_lineEdit.setObjectName(u"flagn49_lineEdit")
        self.flagn49_lineEdit.setMinimumSize(QSize(30, 0))
        self.flagn49_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flagn49_lineEdit.setFont(font)
        self.flagn49_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn49_lineEdit.textChanged.connect(
            lambda txt:self.label_12.setText(txt)
        )

        self.RF2ET_Flag4_horizontalLayout.addWidget(self.flagn49_lineEdit)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag4_horizontalLayout)


        self.horizontalLayout_35.addLayout(self.RF2ET_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RF2ET_Frame)

        self.Rextension_Frame = QFrame(self.frame)
        self.Rextension_Frame.setObjectName(u"Rextension_Frame")
        self.Rextension_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Rextension_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_40 = QHBoxLayout(self.Rextension_Frame)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Rextension_verticalLayout = QVBoxLayout()
        self.Rextension_verticalLayout.setSpacing(0)
        self.Rextension_verticalLayout.setObjectName(u"Rextension_verticalLayout")
        self.flagn14_label = ColorChangingFrame(self.Rextension_Frame)
        self.flagn14_label.setObjectName(u"flagn14_label")
        self.flagn14_label.setMinimumSize(QSize(0, 18))
        self.flagn14_label.setMaximumSize(QSize(16777215, 18))
        self.flagn14_label.setFont(font)
        self.flagn14_label.setFrameShape(QFrame.Shape.Box)
        self.flagn14_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Rextension_verticalLayout.addWidget(self.flagn14_label)

        self.stateNumber12_label = ColorChangingFrame(self.Rextension_Frame)
        self.stateNumber12_label.setObjectName(u"stateNumber12_label")
        self.stateNumber12_label.setMinimumSize(QSize(0, 18))
        self.stateNumber12_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber12_label.setFont(font)
        self.stateNumber12_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber12_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Rextension_verticalLayout.addWidget(self.stateNumber12_label)

        self.Rextension_horizontalLayout = QHBoxLayout()
        self.Rextension_horizontalLayout.setSpacing(0)
        self.Rextension_horizontalLayout.setObjectName(u"Rextension_horizontalLayout")
        self.flagn50_label = ColorChangingFrame(self.Rextension_Frame)
        self.flagn50_label.setObjectName(u"flagn50_label")
        self.flagn50_label.setMinimumSize(QSize(0, 0))
        self.flagn50_label.setMaximumSize(QSize(16777215, 1000))
        self.flagn50_label.setFont(font)
        self.flagn50_label.setFrameShape(QFrame.Shape.Box)
        self.flagn50_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn50_label.setWordWrap(True)

        self.Rextension_horizontalLayout.addWidget(self.flagn50_label)

        self.label_12 = QLabel(self.Rextension_Frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QFrame.Shape.Box)

        self.Rextension_horizontalLayout.addWidget(self.label_12)


        self.Rextension_verticalLayout.addLayout(self.Rextension_horizontalLayout)


        self.horizontalLayout_40.addLayout(self.Rextension_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Rextension_Frame)

        self.Rextended_Frame = QFrame(self.frame)
        self.Rextended_Frame.setObjectName(u"Rextended_Frame")
        self.Rextended_Frame.setFrameShape(QFrame.Shape.Box)
        self.Rextended_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.Rextended_Frame.setLineWidth(0)
        self.horizontalLayout_42 = QHBoxLayout(self.Rextended_Frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Rextended_verticalLayout = QVBoxLayout()
        self.Rextended_verticalLayout.setSpacing(0)
        self.Rextended_verticalLayout.setObjectName(u"Rextended_verticalLayout")
        self.flagn15_label = ColorChangingFrame(self.Rextended_Frame)
        self.flagn15_label.setObjectName(u"flagn15_label")
        self.flagn15_label.setMinimumSize(QSize(0, 18))
        self.flagn15_label.setMaximumSize(QSize(16777215, 18))
        self.flagn15_label.setFont(font)
        self.flagn15_label.setFrameShape(QFrame.Shape.Box)
        self.flagn15_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Rextended_verticalLayout.addWidget(self.flagn15_label)

        self.stateNumber13_label = ColorChangingFrame(self.Rextended_Frame)
        self.stateNumber13_label.setObjectName(u"stateNumber13_label")
        self.stateNumber13_label.setMinimumSize(QSize(0, 18))
        self.stateNumber13_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber13_label.setFont(font)
        self.stateNumber13_label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber13_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Rextended_verticalLayout.addWidget(self.stateNumber13_label)

        self.Rextended_Flag1_horizontalLayout = QHBoxLayout()
        self.Rextended_Flag1_horizontalLayout.setSpacing(0)
        self.Rextended_Flag1_horizontalLayout.setObjectName(u"Rextended_Flag1_horizontalLayout")
        self.flagn51_label = ColorChangingFrame(self.Rextended_Frame)
        self.flagn51_label.setObjectName(u"flagn51_label")
        self.flagn51_label.setMinimumSize(QSize(0, 0))
        self.flagn51_label.setMaximumSize(QSize(16777215, 1000))
        self.flagn51_label.setFont(font)
        self.flagn51_label.setFrameShape(QFrame.Shape.Box)
        self.flagn51_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn51_label.setWordWrap(True)

        self.Rextended_Flag1_horizontalLayout.addWidget(self.flagn51_label)

        self.label_13 = QLabel(self.Rextended_Frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QFrame.Shape.Box)

        self.Rextended_Flag1_horizontalLayout.addWidget(self.label_13)


        self.Rextended_verticalLayout.addLayout(self.Rextended_Flag1_horizontalLayout)


        self.horizontalLayout_42.addLayout(self.Rextended_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Rextended_Frame)


        self.walking_verticalLayout.addLayout(self.walikng_horizontalLayout)


        self.horizontalLayout.addLayout(self.walking_verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_17.addWidget(self.frame)

        self.Stand2SitandSit2StandandSquatTasks_frame = QFrame(self.Main_widget)
        self.Stand2SitandSit2StandandSquatTasks_frame.setObjectName(u"Stand2SitandSit2StandandSquatTasks_frame")
        self.Stand2SitandSit2StandandSquatTasks_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Stand2SitandSit2StandandSquatTasks_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.flagn52_label = ColorChangingFrame(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.flagn52_label.setObjectName(u"flagn52_label")
        self.flagn52_label.setMaximumSize(QSize(16777215, 18))
        self.flagn52_label.setFont(font)
        self.flagn52_label.setFrameShape(QFrame.Shape.Box)
        self.flagn52_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn52_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.flagn52_label)

        self.Stand2SitandSit2StandandSquatTasks_subframe = QFrame(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.Stand2SitandSit2StandandSquatTasks_subframe.setObjectName(u"Stand2SitandSit2StandandSquatTasks_subframe")
        self.Stand2SitandSit2StandandSquatTasks_subframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.Stand2SitandSit2StandandSquatTasks_subframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Stopsd_or_Stopsq_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.Stopsd_or_Stopsq_Frame.setObjectName(u"Stopsd_or_Stopsq_Frame")
        self.Stopsd_or_Stopsq_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Stopsd_or_Stopsq_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Stopsd_or_Stopsq_Frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Stopsd_or_Stopsq_Label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.Stopsd_or_Stopsq_Label.setObjectName(u"Stopsd_or_Stopsq_Label")
        self.Stopsd_or_Stopsq_Label.setMaximumSize(QSize(16777215, 18))
        self.Stopsd_or_Stopsq_Label.setFont(font)
        self.Stopsd_or_Stopsq_Label.setFrameShape(QFrame.Shape.Box)
        self.Stopsd_or_Stopsq_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Stopsd_or_Stopsq_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.Stopsd_or_Stopsq_Label)

        self.flagn53_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn53_label.setObjectName(u"flagn53_label")
        self.flagn53_label.setMaximumSize(QSize(16777215, 18))
        self.flagn53_label.setFont(font)
        self.flagn53_label.setFrameShape(QFrame.Shape.Box)
        self.flagn53_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn53_label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.flagn53_label)

        self.sd_stateNumber0_Label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.sd_stateNumber0_Label.setObjectName(u"sd_stateNumber0_Label")
        self.sd_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.sd_stateNumber0_Label.setFont(font)
        self.sd_stateNumber0_Label.setFrameShape(QFrame.Shape.Box)
        self.sd_stateNumber0_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sd_stateNumber0_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.sd_stateNumber0_Label)

        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag1and2_horizontalLayout")
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag1and2_verticalLayout")
        self.flagn61_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn61_label.setObjectName(u"flagn61_label")
        self.flagn61_label.setFont(font)
        self.flagn61_label.setFrameShape(QFrame.Shape.Box)
        self.flagn61_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn61_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.addWidget(self.flagn61_label)

        self.flagn62_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn62_label.setObjectName(u"flagn62_label")
        self.flagn62_label.setFont(font)
        self.flagn62_label.setFrameShape(QFrame.Shape.Box)
        self.flagn62_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn62_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.addWidget(self.flagn62_label)


        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.addLayout(self.Stopsd_or_Stopsq_Flag1and2_verticalLayout)

        self.flagn61_and_flagn62_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flagn61_and_flagn62_lineEdit.setObjectName(u"flagn61_and_flagn62_lineEdit")
        self.flagn61_and_flagn62_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn61_and_flagn62_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn61_and_flagn62_lineEdit.setFont(font)
        self.flagn61_and_flagn62_lineEdit.setFrame(True)
        self.flagn61_and_flagn62_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn61_and_flagn62_lineEdit.textChanged.connect(
            lambda txt:self.label_16.setText(txt)
        )

        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.addWidget(self.flagn61_and_flagn62_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag31_horizontalLayout")
        self.flagn63_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn63_label.setObjectName(u"flagn63_label")
        self.flagn63_label.setFont(font)
        self.flagn63_label.setFrameShape(QFrame.Shape.Box)
        self.flagn63_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn63_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.addWidget(self.flagn63_label)

        self.flagn63_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flagn63_lineEdit.setObjectName(u"flagn63_lineEdit")
        self.flagn63_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn63_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn63_lineEdit.setFont(font)
        self.flagn63_lineEdit.setFrame(True)
        self.flagn63_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn63_lineEdit.textChanged.connect(
            lambda txt:self.label_17.setText(txt)
        )

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.addWidget(self.flagn63_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag31_horizontalLayout)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag32and33_horizontalLayout")
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.setObjectName(u"Stopsd_or_Stopsq_Flage32and33_verticalLayout")
        self.flagn64_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn64_label.setObjectName(u"flagn64_label")
        self.flagn64_label.setFont(font)
        self.flagn64_label.setFrameShape(QFrame.Shape.Box)
        self.flagn64_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn64_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.addWidget(self.flagn64_label)

        self.flagn65_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flagn65_label.setObjectName(u"flagn65_label")
        self.flagn65_label.setFont(font)
        self.flagn65_label.setFrameShape(QFrame.Shape.Box)
        self.flagn65_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn65_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.addWidget(self.flagn65_label)


        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.addLayout(self.Stopsd_or_Stopsq_Flage32and33_verticalLayout)

        self.flagn64_and_flagn65_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flagn64_and_flagn65_lineEdit.setObjectName(u"flagn64_and_flagn65_lineEdit")
        self.flagn64_and_flagn65_lineEdit.setMinimumSize(QSize(30, 25))
        self.flagn64_and_flagn65_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn64_and_flagn65_lineEdit.setFont(font)
        self.flagn64_and_flagn65_lineEdit.setFrame(True)
        self.flagn64_and_flagn65_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn64_and_flagn65_lineEdit.textChanged.connect(
            lambda txt:self.label_18.setText(txt)
        )

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.addWidget(self.flagn64_and_flagn65_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.Stopsd_or_Stopsq_Frame)

        self.ss2sd_or_ss2sq_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.ss2sd_or_ss2sq_Frame.setObjectName(u"ss2sd_or_ss2sq_Frame")
        self.ss2sd_or_ss2sq_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ss2sd_or_ss2sq_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.ss2sd_or_ss2sq_Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ss2sd_Label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.ss2sd_Label.setObjectName(u"ss2sd_Label")
        self.ss2sd_Label.setMaximumSize(QSize(16777215, 18))
        self.ss2sd_Label.setFont(font)
        self.ss2sd_Label.setFrameShape(QFrame.Shape.Box)
        self.ss2sd_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ss2sd_Label.setWordWrap(True)

        self.verticalLayout.addWidget(self.ss2sd_Label)

        self.flagn54_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn54_label.setObjectName(u"flagn54_label")
        self.flagn54_label.setMaximumSize(QSize(16777215, 18))
        self.flagn54_label.setFont(font)
        self.flagn54_label.setFrameShape(QFrame.Shape.Box)
        self.flagn54_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn54_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flagn54_label)

        self.stateNumber4_or_10_Label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.stateNumber4_or_10_Label.setObjectName(u"stateNumber4_or_10_Label")
        self.stateNumber4_or_10_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber4_or_10_Label.setFont(font)
        self.stateNumber4_or_10_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber4_or_10_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber4_or_10_Label.setWordWrap(True)

        self.verticalLayout.addWidget(self.stateNumber4_or_10_Label)

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag1_horizontalLayout")
        self.flagn66_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn66_label.setObjectName(u"flagn66_label")
        self.flagn66_label.setFont(font)
        self.flagn66_label.setFrameShape(QFrame.Shape.Box)
        self.flagn66_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn66_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.addWidget(self.flagn66_label)

        self.flagn66_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn66_lineEdit.setObjectName(u"flagn66_lineEdit")
        self.flagn66_lineEdit.setMinimumSize(QSize(20, 30))
        self.flagn66_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn66_lineEdit.setFont(font)
        self.flagn66_lineEdit.setFrame(True)
        self.flagn66_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn66_lineEdit.textChanged.connect(
            lambda txt:self.label_19.setText(txt)
        )

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.addWidget(self.flagn66_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag1_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag2and3_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag2and3_verticalLayout")
        self.flagn67_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn67_label.setObjectName(u"flagn67_label")
        self.flagn67_label.setFont(font)
        self.flagn67_label.setFrameShape(QFrame.Shape.Box)
        self.flagn67_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn67_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.addWidget(self.flagn67_label)

        self.flagn68_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn68_label.setObjectName(u"flagn68_label")
        self.flagn68_label.setFont(font)
        self.flagn68_label.setFrameShape(QFrame.Shape.Box)
        self.flagn68_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn68_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.addWidget(self.flagn68_label)


        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag2and3_verticalLayout)

        self.flagn67_and_flagn68_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn67_and_flagn68_lineEdit.setObjectName(u"flagn67_and_flagn68_lineEdit")
        self.flagn67_and_flagn68_lineEdit.setMinimumSize(QSize(30, 30))
        self.flagn67_and_flagn68_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn67_and_flagn68_lineEdit.setFont(font)
        self.flagn67_and_flagn68_lineEdit.setFrame(True)
        self.flagn67_and_flagn68_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn67_and_flagn68_lineEdit.textChanged.connect(
            lambda txt:self.label_20.setText(txt)
        )

        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.addWidget(self.flagn67_and_flagn68_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag4and5_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag4and5_verticalLayout")
        self.flagn69_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn69_label.setObjectName(u"flagn69_label")
        self.flagn69_label.setFont(font)
        self.flagn69_label.setFrameShape(QFrame.Shape.Box)
        self.flagn69_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn69_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.addWidget(self.flagn69_label)

        self.flagn70_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn70_label.setObjectName(u"flagn70_label")
        self.flagn70_label.setFont(font)
        self.flagn70_label.setFrameShape(QFrame.Shape.Box)
        self.flagn70_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn70_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.addWidget(self.flagn70_label)


        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag4and5_verticalLayout)

        self.flagn69_and_flagn70_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn69_and_flagn70_lineEdit.setObjectName(u"flagn69_and_flagn70_lineEdit")
        self.flagn69_and_flagn70_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn69_and_flagn70_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flagn69_and_flagn70_lineEdit.setFont(font)
        self.flagn69_and_flagn70_lineEdit.setFrame(True)
        self.flagn69_and_flagn70_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn69_and_flagn70_lineEdit.textChanged.connect(
            lambda txt:self.label_21.setText(txt)
        )

        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.addWidget(self.flagn69_and_flagn70_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag6and7_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag6and7_verticalLayout")
        self.flagn71_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn71_label.setObjectName(u"flagn71_label")
        self.flagn71_label.setFont(font)
        self.flagn71_label.setFrameShape(QFrame.Shape.Box)
        self.flagn71_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn71_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.addWidget(self.flagn71_label)

        self.flagn72_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn72_label.setObjectName(u"flagn72_label")
        self.flagn72_label.setFont(font)
        self.flagn72_label.setFrameShape(QFrame.Shape.Box)
        self.flagn72_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn72_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.addWidget(self.flagn72_label)


        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag6and7_verticalLayout)

        self.flagn71_and_flagn72_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn71_and_flagn72_lineEdit.setObjectName(u"flagn71_and_flagn72_lineEdit")
        self.flagn71_and_flagn72_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn71_and_flagn72_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flagn71_and_flagn72_lineEdit.setFont(font)
        self.flagn71_and_flagn72_lineEdit.setFrame(True)
        self.flagn71_and_flagn72_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn71_and_flagn72_lineEdit.textChanged.connect(
            lambda txt:self.label_22.setText(txt)
        )

        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.addWidget(self.flagn71_and_flagn72_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout)

        self.flagn73_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn73_label.setObjectName(u"flagn73_label")
        self.flagn73_label.setMaximumSize(QSize(16777215, 18))
        self.flagn73_label.setFont(font)
        self.flagn73_label.setFrameShape(QFrame.Shape.Box)
        self.flagn73_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn73_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flagn73_label)

        self.flagn74_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn74_label.setObjectName(u"flagn74_label")
        self.flagn74_label.setMaximumSize(QSize(16777215, 18))
        self.flagn74_label.setFont(font)
        self.flagn74_label.setFrameShape(QFrame.Shape.Box)
        self.flagn74_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn74_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flagn74_label)

        self.flagn75_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn75_label.setObjectName(u"flagn75_label")
        self.flagn75_label.setMaximumSize(QSize(16777215, 18))
        self.flagn75_label.setFont(font)
        self.flagn75_label.setFrameShape(QFrame.Shape.Box)
        self.flagn75_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn75_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flagn75_label)

        self.flagn76_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn76_label.setObjectName(u"flagn76_label")
        self.flagn76_label.setMaximumSize(QSize(16777215, 18))
        self.flagn76_label.setFont(font)
        self.flagn76_label.setFrameShape(QFrame.Shape.Box)
        self.flagn76_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn76_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flagn76_label)

        self.ss2sd_or_ss2sq_flagn75_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_flagn75_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_flagn75_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_flagn75_horizontalLayout")
        self.flagn77_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn77_label.setObjectName(u"flagn77_label")
        self.flagn77_label.setFont(font)
        self.flagn77_label.setFrameShape(QFrame.Shape.Box)
        self.flagn77_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn77_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_flagn75_horizontalLayout.addWidget(self.flagn77_label)

        self.flagn77_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn77_lineEdit.setObjectName(u"flagn77_lineEdit")
        self.flagn77_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn77_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn77_lineEdit.setFont(font)
        self.flagn77_lineEdit.setFrame(True)
        self.flagn77_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn77_lineEdit.textChanged.connect(
            lambda txt:(
                self.label_14.setText(txt),
                self.label_23.setText(txt),
                self.label_25.setText(txt)
        ))

        self.ss2sd_or_ss2sq_flagn75_horizontalLayout.addWidget(self.flagn77_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_flagn75_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag82_horizontalLayout")
        self.flagn78_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flagn78_label.setObjectName(u"flagn78_label")
        self.flagn78_label.setFont(font)
        self.flagn78_label.setFrameShape(QFrame.Shape.Box)
        self.flagn78_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn78_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.addWidget(self.flagn78_label)

        self.flagn78_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flagn78_lineEdit.setObjectName(u"flagn78_lineEdit")
        self.flagn78_lineEdit.setMinimumSize(QSize(30, 28))
        self.flagn78_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn78_lineEdit.setFont(font)
        self.flagn78_lineEdit.setFrame(True)
        self.flagn78_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn78_lineEdit.textChanged.connect(
            lambda txt:self.label_24.setText(txt)
        )

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.addWidget(self.flagn78_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag82_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.ss2sd_or_ss2sq_Frame)

        self.SittingDown_or_Squat_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.SittingDown_or_Squat_Frame.setObjectName(u"SittingDown_or_Squat_Frame")
        self.SittingDown_or_Squat_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SittingDown_or_Squat_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.SittingDown_or_Squat_Frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.SittingDown_or_Squat_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.SittingDown_or_Squat_Label.setObjectName(u"SittingDown_or_Squat_Label")
        self.SittingDown_or_Squat_Label.setMaximumSize(QSize(16777215, 18))
        self.SittingDown_or_Squat_Label.setFont(font)
        self.SittingDown_or_Squat_Label.setFrameShape(QFrame.Shape.Box)
        self.SittingDown_or_Squat_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.SittingDown_or_Squat_Label)

        self.SittingDown_or_Squat_horizontalLayout = QHBoxLayout()
        self.SittingDown_or_Squat_horizontalLayout.setSpacing(0)
        self.SittingDown_or_Squat_horizontalLayout.setObjectName(u"SittingDown_or_Squat_horizontalLayout")
        self.sdMiddle_or_sqMiddle_verticalLayout = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_verticalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_verticalLayout.setObjectName(u"sdMiddle_or_sqMiddle_verticalLayout")
        self.flagn55_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn55_label.setObjectName(u"flagn55_label")
        self.flagn55_label.setMaximumSize(QSize(16777215, 18))
        self.flagn55_label.setFont(font)
        self.flagn55_label.setFrameShape(QFrame.Shape.Box)
        self.flagn55_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn55_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout.addWidget(self.flagn55_label)

        self.stateNumber_minus5_or_minus11_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.stateNumber_minus5_or_minus11_Label.setObjectName(u"stateNumber_minus5_or_minus11_Label")
        self.stateNumber_minus5_or_minus11_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus5_or_minus11_Label.setFont(font)
        self.stateNumber_minus5_or_minus11_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus5_or_minus11_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber_minus5_or_minus11_Label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout.addWidget(self.stateNumber_minus5_or_minus11_Label)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag11_horizontalLayout")
        self.flagn79_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn79_label.setObjectName(u"flagn79_label")
        self.flagn79_label.setFont(font)
        self.flagn79_label.setFrameShape(QFrame.Shape.Box)
        self.flagn79_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn79_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.addWidget(self.flagn79_label)

        self.label_14 = QLabel(self.SittingDown_or_Squat_Frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_14.setFrameShape(QFrame.Shape.Box)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.addWidget(self.label_14)


        self.sdMiddle_or_sqMiddle_verticalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout")
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_verticalLayout")
        self.flagn80_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn80_label.setObjectName(u"flagn80_label")
        self.flagn80_label.setFont(font)
        self.flagn80_label.setFrameShape(QFrame.Shape.Box)
        self.flagn80_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn80_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.addWidget(self.flagn80_label)

        self.flagn81_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn81_label.setObjectName(u"flagn81_label")
        self.flagn81_label.setFont(font)
        self.flagn81_label.setFrameShape(QFrame.Shape.Box)
        self.flagn81_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn81_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.addWidget(self.flagn81_label)


        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout)

        self.flagn80_and_flagn81_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame)
        self.flagn80_and_flagn81_lineEdit.setObjectName(u"flagn80_and_flagn81_lineEdit")
        self.flagn80_and_flagn81_lineEdit.setMinimumSize(QSize(28, 20))
        self.flagn80_and_flagn81_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flagn80_and_flagn81_lineEdit.setFont(font)
        self.flagn80_and_flagn81_lineEdit.setFrame(True)
        self.flagn80_and_flagn81_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn80_and_flagn81_lineEdit.textChanged.connect(
            lambda txt:self.label_26.setText(txt)
        )

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.addWidget(self.flagn80_and_flagn81_lineEdit)


        self.sdMiddle_or_sqMiddle_verticalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout)


        self.SittingDown_or_Squat_horizontalLayout.addLayout(self.sdMiddle_or_sqMiddle_verticalLayout)

        self.sdFinal_or_sqDeep_verticalLayout = QVBoxLayout()
        self.sdFinal_or_sqDeep_verticalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_verticalLayout.setObjectName(u"sdFinal_or_sqDeep_verticalLayout")
        self.flagn56_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn56_label.setObjectName(u"flagn56_label")
        self.flagn56_label.setMaximumSize(QSize(16777215, 18))
        self.flagn56_label.setFont(font)
        self.flagn56_label.setFrameShape(QFrame.Shape.Box)
        self.flagn56_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn56_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout.addWidget(self.flagn56_label)

        self.stateNumber_minus6_or_minus12_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.stateNumber_minus6_or_minus12_Label.setObjectName(u"stateNumber_minus6_or_minus12_Label")
        self.stateNumber_minus6_or_minus12_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus6_or_minus12_Label.setFont(font)
        self.stateNumber_minus6_or_minus12_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus6_or_minus12_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber_minus6_or_minus12_Label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout.addWidget(self.stateNumber_minus6_or_minus12_Label)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout = QHBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_horizontalLayout")
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout = QVBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_verticalLayout")
        self.flagn82_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn82_label.setObjectName(u"flagn82_label")
        self.flagn82_label.setFont(font)
        self.flagn82_label.setFrameShape(QFrame.Shape.Box)
        self.flagn82_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn82_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.addWidget(self.flagn82_label)

        self.flagn83_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flagn83_label.setObjectName(u"flagn83_label")
        self.flagn83_label.setFont(font)
        self.flagn83_label.setFrameShape(QFrame.Shape.Box)
        self.flagn83_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn83_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.addWidget(self.flagn83_label)


        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.addLayout(self.sdFinal_or_sqDeep_Flag1and2_verticalLayout)

        self.flagn82_and_flagn83_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame)
        self.flagn82_and_flagn83_lineEdit.setObjectName(u"flagn82_and_flagn83_lineEdit")
        self.flagn82_and_flagn83_lineEdit.setMinimumSize(QSize(28, 20))
        self.flagn82_and_flagn83_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flagn82_and_flagn83_lineEdit.setFont(font)
        self.flagn82_and_flagn83_lineEdit.setFrame(True)
        self.flagn82_and_flagn83_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn82_and_flagn83_lineEdit.textChanged.connect(
            lambda txt:self.label_27.setText(txt)
        )

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.addWidget(self.flagn82_and_flagn83_lineEdit)


        self.sdFinal_or_sqDeep_verticalLayout.addLayout(self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout)


        self.SittingDown_or_Squat_horizontalLayout.addLayout(self.sdFinal_or_sqDeep_verticalLayout)


        self.verticalLayout_13.addLayout(self.SittingDown_or_Squat_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.SittingDown_or_Squat_Frame)

        self.seated_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.seated_Frame.setObjectName(u"seated_Frame")
        self.seated_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.seated_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.seated_Frame)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.flagn57_label = ColorChangingFrame(self.seated_Frame)
        self.flagn57_label.setObjectName(u"flagn57_label")
        self.flagn57_label.setMaximumSize(QSize(16777215, 36))
        self.flagn57_label.setFont(font)
        self.flagn57_label.setFrameShape(QFrame.Shape.Box)
        self.flagn57_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.flagn57_label)

        self.stateNumber_minus7_Label = ColorChangingFrame(self.seated_Frame)
        self.stateNumber_minus7_Label.setObjectName(u"stateNumber_minus7_Label")
        self.stateNumber_minus7_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus7_Label.setFont(font)
        self.stateNumber_minus7_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus7_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.stateNumber_minus7_Label)

        self.seated_Flag11_horizontalLayout = QHBoxLayout()
        self.seated_Flag11_horizontalLayout.setSpacing(0)
        self.seated_Flag11_horizontalLayout.setObjectName(u"seated_Flag11_horizontalLayout")
        self.flagn84_label = ColorChangingFrame(self.seated_Frame)
        self.flagn84_label.setObjectName(u"flagn84_label")
        self.flagn84_label.setMaximumSize(QSize(16777215, 800))
        self.flagn84_label.setFont(font)
        self.flagn84_label.setFrameShape(QFrame.Shape.Box)
        self.flagn84_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn84_label.setWordWrap(True)

        self.seated_Flag11_horizontalLayout.addWidget(self.flagn84_label)

        self.flagn84_lineEdit = QLineEdit(self.seated_Frame)
        self.flagn84_lineEdit.setObjectName(u"flagn84_lineEdit")
        self.flagn84_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn84_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn84_lineEdit.setFont(font)
        self.flagn84_lineEdit.setFrame(True)
        self.flagn84_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.seated_Flag11_horizontalLayout.addWidget(self.flagn84_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag11_horizontalLayout)

        self.seated_Flag12and13_horizontalLayout = QHBoxLayout()
        self.seated_Flag12and13_horizontalLayout.setSpacing(0)
        self.seated_Flag12and13_horizontalLayout.setObjectName(u"seated_Flag12and13_horizontalLayout")
        self.seated_Flag12and13_verticalLayout = QVBoxLayout()
        self.seated_Flag12and13_verticalLayout.setSpacing(0)
        self.seated_Flag12and13_verticalLayout.setObjectName(u"seated_Flag12and13_verticalLayout")
        self.flagn85_label = ColorChangingFrame(self.seated_Frame)
        self.flagn85_label.setObjectName(u"flagn85_label")
        self.flagn85_label.setFont(font)
        self.flagn85_label.setFrameShape(QFrame.Shape.Box)
        self.flagn85_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn85_label.setWordWrap(True)

        self.seated_Flag12and13_verticalLayout.addWidget(self.flagn85_label)

        self.flagn86_label = ColorChangingFrame(self.seated_Frame)
        self.flagn86_label.setObjectName(u"flagn86_label")
        self.flagn86_label.setFont(font)
        self.flagn86_label.setFrameShape(QFrame.Shape.Box)
        self.flagn86_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn86_label.setWordWrap(True)

        self.seated_Flag12and13_verticalLayout.addWidget(self.flagn86_label)


        self.seated_Flag12and13_horizontalLayout.addLayout(self.seated_Flag12and13_verticalLayout)

        self.flagn85_and_flagn86_lineEdit = QLineEdit(self.seated_Frame)
        self.flagn85_and_flagn86_lineEdit.setObjectName(u"flagn85_and_flagn86_lineEdit")
        self.flagn85_and_flagn86_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn85_and_flagn86_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn85_and_flagn86_lineEdit.setFont(font)
        self.flagn85_and_flagn86_lineEdit.setFrame(True)
        self.flagn85_and_flagn86_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn85_and_flagn86_lineEdit.setReadOnly(False)

        self.seated_Flag12and13_horizontalLayout.addWidget(self.flagn85_and_flagn86_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag12and13_horizontalLayout)

        self.or_seated_Label = ColorChangingFrame(self.seated_Frame)
        self.or_seated_Label.setObjectName(u"or_seated_Label")
        self.or_seated_Label.setMaximumSize(QSize(16777215, 18))
        self.or_seated_Label.setFont(font)
        self.or_seated_Label.setFrameShape(QFrame.Shape.Box)
        self.or_seated_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.or_seated_Label.setWordWrap(True)

        self.verticalLayout_41.addWidget(self.or_seated_Label)

        self.seated_Flag2and3_horizontalLayout = QHBoxLayout()
        self.seated_Flag2and3_horizontalLayout.setSpacing(0)
        self.seated_Flag2and3_horizontalLayout.setObjectName(u"seated_Flag2and3_horizontalLayout")
        self.seated_Flag2and3_Label_verticalLayout = QVBoxLayout()
        self.seated_Flag2and3_Label_verticalLayout.setSpacing(0)
        self.seated_Flag2and3_Label_verticalLayout.setObjectName(u"seated_Flag2and3_Label_verticalLayout")
        self.flagn87_label = ColorChangingFrame(self.seated_Frame)
        self.flagn87_label.setObjectName(u"flagn87_label")
        self.flagn87_label.setFont(font)
        self.flagn87_label.setFrameShape(QFrame.Shape.Box)
        self.flagn87_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn87_label.setWordWrap(True)

        self.seated_Flag2and3_Label_verticalLayout.addWidget(self.flagn87_label)

        self.flagn88_label = ColorChangingFrame(self.seated_Frame)
        self.flagn88_label.setObjectName(u"flagn88_label")
        self.flagn88_label.setFont(font)
        self.flagn88_label.setFrameShape(QFrame.Shape.Box)
        self.flagn88_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn88_label.setWordWrap(True)

        self.seated_Flag2and3_Label_verticalLayout.addWidget(self.flagn88_label)


        self.seated_Flag2and3_horizontalLayout.addLayout(self.seated_Flag2and3_Label_verticalLayout)

        self.flagn87_and_flagn88_lineEdit = QLineEdit(self.seated_Frame)
        self.flagn87_and_flagn88_lineEdit.setObjectName(u"flagn87_and_flagn88_lineEdit")
        self.flagn87_and_flagn88_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn87_and_flagn88_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn87_and_flagn88_lineEdit.setFont(font)
        self.flagn87_and_flagn88_lineEdit.setFrame(True)
        self.flagn87_and_flagn88_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.seated_Flag2and3_horizontalLayout.addWidget(self.flagn87_and_flagn88_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag2and3_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.seated_Frame)

        self.standingUp_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.standingUp_Frame.setObjectName(u"standingUp_Frame")
        self.standingUp_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.standingUp_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.standingUp_Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.StandingUp_horizontalLayout = QHBoxLayout()
        self.StandingUp_horizontalLayout.setSpacing(0)
        self.StandingUp_horizontalLayout.setObjectName(u"StandingUp_horizontalLayout")
        self.seated2su_Frame = QFrame(self.standingUp_Frame)
        self.seated2su_Frame.setObjectName(u"seated2su_Frame")
        self.seated2su_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.seated2su_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.seated2su_Frame)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.flagn58_label = ColorChangingFrame(self.seated2su_Frame)
        self.flagn58_label.setObjectName(u"flagn58_label")
        self.flagn58_label.setMaximumSize(QSize(16777215, 36))
        self.flagn58_label.setFont(font)
        self.flagn58_label.setFrameShape(QFrame.Shape.Box)
        self.flagn58_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.flagn58_label)

        self.stateNumber_minus8_Label = ColorChangingFrame(self.seated2su_Frame)
        self.stateNumber_minus8_Label.setObjectName(u"stateNumber_minus8_Label")
        self.stateNumber_minus8_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus8_Label.setFont(font)
        self.stateNumber_minus8_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus8_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.stateNumber_minus8_Label)

        self.seated2su_Flag1and2_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag1and2_horizontalLayout.setSpacing(0)
        self.seated2su_Flag1and2_horizontalLayout.setObjectName(u"seated2su_Flag1and2_horizontalLayout")
        self.seated2su_Flag1and2_verticalLayout = QVBoxLayout()
        self.seated2su_Flag1and2_verticalLayout.setSpacing(0)
        self.seated2su_Flag1and2_verticalLayout.setObjectName(u"seated2su_Flag1and2_verticalLayout")
        self.flagn89_label = ColorChangingFrame(self.seated2su_Frame)
        self.flagn89_label.setObjectName(u"flagn89_label")
        self.flagn89_label.setFont(font)
        self.flagn89_label.setFrameShape(QFrame.Shape.Box)
        self.flagn89_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn89_label.setWordWrap(True)

        self.seated2su_Flag1and2_verticalLayout.addWidget(self.flagn89_label)

        self.flagn90_label = ColorChangingFrame(self.seated2su_Frame)
        self.flagn90_label.setObjectName(u"flagn90_label")
        self.flagn90_label.setFont(font)
        self.flagn90_label.setFrameShape(QFrame.Shape.Box)
        self.flagn90_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn90_label.setWordWrap(True)

        self.seated2su_Flag1and2_verticalLayout.addWidget(self.flagn90_label)


        self.seated2su_Flag1and2_horizontalLayout.addLayout(self.seated2su_Flag1and2_verticalLayout)

        self.flagn89_and_flagn90_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flagn89_and_flagn90_lineEdit.setObjectName(u"flagn89_and_flagn90_lineEdit")
        self.flagn89_and_flagn90_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn89_and_flagn90_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn89_and_flagn90_lineEdit.setFont(font)
        self.flagn89_and_flagn90_lineEdit.setFrame(True)
        self.flagn89_and_flagn90_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.seated2su_Flag1and2_horizontalLayout.addWidget(self.flagn89_and_flagn90_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag1and2_horizontalLayout)

        self.seated2su_Flag31_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag31_horizontalLayout.setSpacing(0)
        self.seated2su_Flag31_horizontalLayout.setObjectName(u"seated2su_Flag31_horizontalLayout")
        self.flagn91_label = ColorChangingFrame(self.seated2su_Frame)
        self.flagn91_label.setObjectName(u"flagn91_label")
        self.flagn91_label.setFont(font)
        self.flagn91_label.setFrameShape(QFrame.Shape.Box)
        self.flagn91_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn91_label.setWordWrap(True)

        self.seated2su_Flag31_horizontalLayout.addWidget(self.flagn91_label)

        self.flagn91_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flagn91_lineEdit.setObjectName(u"flagn91_lineEdit")
        self.flagn91_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn91_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn91_lineEdit.setFont(font)
        self.flagn91_lineEdit.setFrame(True)
        self.flagn91_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.seated2su_Flag31_horizontalLayout.addWidget(self.flagn91_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag31_horizontalLayout)

        self.seated2su_Flag32_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag32_horizontalLayout.setSpacing(0)
        self.seated2su_Flag32_horizontalLayout.setObjectName(u"seated2su_Flag32_horizontalLayout")
        self.flagn92_label = ColorChangingFrame(self.seated2su_Frame)
        self.flagn92_label.setObjectName(u"flagn92_label")
        self.flagn92_label.setFont(font)
        self.flagn92_label.setFrameShape(QFrame.Shape.Box)
        self.flagn92_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn92_label.setWordWrap(True)

        self.seated2su_Flag32_horizontalLayout.addWidget(self.flagn92_label)

        self.flagn92_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flagn92_lineEdit.setObjectName(u"flagn92_lineEdit")
        self.flagn92_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn92_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn92_lineEdit.setFont(font)
        self.flagn92_lineEdit.setFrame(True)
        self.flagn92_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.seated2su_Flag32_horizontalLayout.addWidget(self.flagn92_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag32_horizontalLayout)


        self.StandingUp_horizontalLayout.addWidget(self.seated2su_Frame)

        self.sub_standingUp_Frame = QFrame(self.standingUp_Frame)
        self.sub_standingUp_Frame.setObjectName(u"sub_standingUp_Frame")
        self.sub_standingUp_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sub_standingUp_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.sub_standingUp_Frame)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.flagn59_label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.flagn59_label.setObjectName(u"flagn59_label")
        self.flagn59_label.setMaximumSize(QSize(16777215, 36))
        self.flagn59_label.setFont(font)
        self.flagn59_label.setFrameShape(QFrame.Shape.Box)
        self.flagn59_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_44.addWidget(self.flagn59_label)

        self.stateNumber_minus9_Label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.stateNumber_minus9_Label.setObjectName(u"stateNumber_minus9_Label")
        self.stateNumber_minus9_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus9_Label.setFont(font)
        self.stateNumber_minus9_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus9_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_44.addWidget(self.stateNumber_minus9_Label)

        self.standingUp_Flag1_horizontalLayout = QHBoxLayout()
        self.standingUp_Flag1_horizontalLayout.setSpacing(0)
        self.standingUp_Flag1_horizontalLayout.setObjectName(u"standingUp_Flag1_horizontalLayout")
        self.flagn93_label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.flagn93_label.setObjectName(u"flagn93_label")
        self.flagn93_label.setFont(font)
        self.flagn93_label.setFrameShape(QFrame.Shape.Box)
        self.flagn93_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn93_label.setWordWrap(True)

        self.standingUp_Flag1_horizontalLayout.addWidget(self.flagn93_label)

        self.flagn93_lineEdit = QLineEdit(self.sub_standingUp_Frame)
        self.flagn93_lineEdit.setObjectName(u"flagn93_lineEdit")
        self.flagn93_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn93_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn93_lineEdit.setFont(font)
        self.flagn93_lineEdit.setFrame(True)
        self.flagn93_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.standingUp_Flag1_horizontalLayout.addWidget(self.flagn93_lineEdit)


        self.verticalLayout_44.addLayout(self.standingUp_Flag1_horizontalLayout)


        self.StandingUp_horizontalLayout.addWidget(self.sub_standingUp_Frame)


        self.verticalLayout_2.addLayout(self.StandingUp_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.standingUp_Frame)

        self.su2ss_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.su2ss_Frame.setObjectName(u"su2ss_Frame")
        self.su2ss_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.su2ss_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.su2ss_Frame)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.su2ss_Label = ColorChangingFrame(self.su2ss_Frame)
        self.su2ss_Label.setObjectName(u"su2ss_Label")
        self.su2ss_Label.setMaximumSize(QSize(16777215, 18))
        self.su2ss_Label.setFont(font)
        self.su2ss_Label.setFrameShape(QFrame.Shape.Box)
        self.su2ss_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_47.addWidget(self.su2ss_Label)

        self.flagn60_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn60_label.setObjectName(u"flagn60_label")
        self.flagn60_label.setMaximumSize(QSize(16777215, 18))
        self.flagn60_label.setFont(font)
        self.flagn60_label.setFrameShape(QFrame.Shape.Box)
        self.flagn60_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_47.addWidget(self.flagn60_label)

        self.su2ss_stateNumber0_Label = ColorChangingFrame(self.su2ss_Frame)
        self.su2ss_stateNumber0_Label.setObjectName(u"su2ss_stateNumber0_Label")
        self.su2ss_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.su2ss_stateNumber0_Label.setFont(font)
        self.su2ss_stateNumber0_Label.setFrameShape(QFrame.Shape.Box)
        self.su2ss_stateNumber0_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_47.addWidget(self.su2ss_stateNumber0_Label)

        self.standingStill_Flag1and2_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag1and2_horizontalLayout.setSpacing(0)
        self.standingStill_Flag1and2_horizontalLayout.setObjectName(u"standingStill_Flag1and2_horizontalLayout")
        self.standingStill_Flag1and2_verticalLayout = QVBoxLayout()
        self.standingStill_Flag1and2_verticalLayout.setSpacing(0)
        self.standingStill_Flag1and2_verticalLayout.setObjectName(u"standingStill_Flag1and2_verticalLayout")
        self.flagn94_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn94_label.setObjectName(u"flagn94_label")
        self.flagn94_label.setFont(font)
        self.flagn94_label.setFrameShape(QFrame.Shape.Box)
        self.flagn94_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn94_label.setWordWrap(True)

        self.standingStill_Flag1and2_verticalLayout.addWidget(self.flagn94_label)

        self.flagn95_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn95_label.setObjectName(u"flagn95_label")
        self.flagn95_label.setFont(font)
        self.flagn95_label.setFrameShape(QFrame.Shape.Box)
        self.flagn95_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn95_label.setWordWrap(True)

        self.standingStill_Flag1and2_verticalLayout.addWidget(self.flagn95_label)


        self.standingStill_Flag1and2_horizontalLayout.addLayout(self.standingStill_Flag1and2_verticalLayout)

        self.flagn94_and_flagn95_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flagn94_and_flagn95_lineEdit.setObjectName(u"flagn94_and_flagn95_lineEdit")
        self.flagn94_and_flagn95_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn94_and_flagn95_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn94_and_flagn95_lineEdit.setFont(font)
        self.flagn94_and_flagn95_lineEdit.setFrame(True)
        self.flagn94_and_flagn95_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.standingStill_Flag1and2_horizontalLayout.addWidget(self.flagn94_and_flagn95_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag1and2_horizontalLayout)

        self.standingStill_Flag31_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag31_horizontalLayout.setSpacing(0)
        self.standingStill_Flag31_horizontalLayout.setObjectName(u"standingStill_Flag31_horizontalLayout")
        self.flagn96_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn96_label.setObjectName(u"flagn96_label")
        self.flagn96_label.setFont(font)
        self.flagn96_label.setFrameShape(QFrame.Shape.Box)
        self.flagn96_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn96_label.setWordWrap(True)

        self.standingStill_Flag31_horizontalLayout.addWidget(self.flagn96_label)

        self.flagn96_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flagn96_lineEdit.setObjectName(u"flagn96_lineEdit")
        self.flagn96_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn96_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn96_lineEdit.setFont(font)
        self.flagn96_lineEdit.setFrame(True)
        self.flagn96_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.standingStill_Flag31_horizontalLayout.addWidget(self.flagn96_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag31_horizontalLayout)

        self.standingStill_Flag31and32_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag31and32_horizontalLayout.setSpacing(0)
        self.standingStill_Flag31and32_horizontalLayout.setObjectName(u"standingStill_Flag31and32_horizontalLayout")
        self.standingStill_Flag31and32_verticalLayout = QVBoxLayout()
        self.standingStill_Flag31and32_verticalLayout.setSpacing(0)
        self.standingStill_Flag31and32_verticalLayout.setObjectName(u"standingStill_Flag31and32_verticalLayout")
        self.flagn97_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn97_label.setObjectName(u"flagn97_label")
        self.flagn97_label.setFont(font)
        self.flagn97_label.setFrameShape(QFrame.Shape.Box)
        self.flagn97_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn97_label.setWordWrap(True)

        self.standingStill_Flag31and32_verticalLayout.addWidget(self.flagn97_label)

        self.flagn98_label = ColorChangingFrame(self.su2ss_Frame)
        self.flagn98_label.setObjectName(u"flagn98_label")
        self.flagn98_label.setFont(font)
        self.flagn98_label.setFrameShape(QFrame.Shape.Box)
        self.flagn98_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn98_label.setWordWrap(True)

        self.standingStill_Flag31and32_verticalLayout.addWidget(self.flagn98_label)


        self.standingStill_Flag31and32_horizontalLayout.addLayout(self.standingStill_Flag31and32_verticalLayout)

        self.flagn97_and_flagn98_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flagn97_and_flagn98_lineEdit.setObjectName(u"flagn97_and_flagn98_lineEdit")
        self.flagn97_and_flagn98_lineEdit.setMinimumSize(QSize(30, 20))
        self.flagn97_and_flagn98_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn97_and_flagn98_lineEdit.setFont(font)
        self.flagn97_and_flagn98_lineEdit.setFrame(True)
        self.flagn97_and_flagn98_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.standingStill_Flag31and32_horizontalLayout.addWidget(self.flagn97_and_flagn98_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag31and32_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.su2ss_Frame)


        self.verticalLayout_3.addWidget(self.Stand2SitandSit2StandandSquatTasks_subframe)


        self.verticalLayout_17.addWidget(self.Stand2SitandSit2StandandSquatTasks_frame)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.turningTask_Frame = QFrame(self.Main_widget)
        self.turningTask_Frame.setObjectName(u"turningTask_Frame")
        self.turningTask_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.turningTask_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.turningTask_Frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.flagn99_label = ColorChangingFrame(self.turningTask_Frame)
        self.flagn99_label.setObjectName(u"flagn99_label")
        self.flagn99_label.setMaximumSize(QSize(16777215, 18))
        self.flagn99_label.setFont(font)
        self.flagn99_label.setFrameShape(QFrame.Shape.Box)
        self.flagn99_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.flagn99_label)

        self.turningTask_sub_Frame = QFrame(self.turningTask_Frame)
        self.turningTask_sub_Frame.setObjectName(u"turningTask_sub_Frame")
        self.turningTask_sub_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.turningTask_sub_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.turningTask_sub_Frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.ss2t_Frame = QFrame(self.turningTask_sub_Frame)
        self.ss2t_Frame.setObjectName(u"ss2t_Frame")
        self.ss2t_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.ss2t_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ss2t_Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ss2t_Label = ColorChangingFrame(self.ss2t_Frame)
        self.ss2t_Label.setObjectName(u"ss2t_Label")
        self.ss2t_Label.setMaximumSize(QSize(16777215, 18))
        self.ss2t_Label.setFont(font)
        self.ss2t_Label.setFrameShape(QFrame.Shape.Box)
        self.ss2t_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.ss2t_Label)

        self.flagn100_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn100_label.setObjectName(u"flagn100_label")
        self.flagn100_label.setMaximumSize(QSize(16777215, 18))
        self.flagn100_label.setFont(font)
        self.flagn100_label.setFrameShape(QFrame.Shape.Box)
        self.flagn100_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.flagn100_label)

        self.stateNumber_minus1_Label = ColorChangingFrame(self.ss2t_Frame)
        self.stateNumber_minus1_Label.setObjectName(u"stateNumber_minus1_Label")
        self.stateNumber_minus1_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus1_Label.setFont(font)
        self.stateNumber_minus1_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus1_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.stateNumber_minus1_Label)

        self.turningStart_Flag1_horizontalLayout = QHBoxLayout()
        self.turningStart_Flag1_horizontalLayout.setSpacing(0)
        self.turningStart_Flag1_horizontalLayout.setObjectName(u"turningStart_Flag1_horizontalLayout")
        self.flagn104_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn104_label.setObjectName(u"flagn104_label")
        self.flagn104_label.setFont(font)
        self.flagn104_label.setFrameShape(QFrame.Shape.Box)
        self.flagn104_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn104_label.setWordWrap(True)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flagn104_label)

        self.flagn105_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn105_label.setObjectName(u"flagn105_label")
        self.flagn105_label.setFont(font)
        self.flagn105_label.setFrameShape(QFrame.Shape.Box)
        self.flagn105_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn105_label.setWordWrap(True)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flagn105_label)

        self.flagn104_and_flagn105_lineEdit = QLineEdit(self.ss2t_Frame)
        self.flagn104_and_flagn105_lineEdit.setObjectName(u"flagn104_and_flagn105_lineEdit")
        self.flagn104_and_flagn105_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn104_and_flagn105_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn104_and_flagn105_lineEdit.setFont(font)
        self.flagn104_and_flagn105_lineEdit.setFrame(True)
        self.flagn104_and_flagn105_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flagn104_and_flagn105_lineEdit)


        self.verticalLayout_6.addLayout(self.turningStart_Flag1_horizontalLayout)

        self.turningStart_Flag2_horizontalLayout = QHBoxLayout()
        self.turningStart_Flag2_horizontalLayout.setSpacing(0)
        self.turningStart_Flag2_horizontalLayout.setObjectName(u"turningStart_Flag2_horizontalLayout")
        self.flagn106_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn106_label.setObjectName(u"flagn106_label")
        self.flagn106_label.setFont(font)
        self.flagn106_label.setFrameShape(QFrame.Shape.Box)
        self.flagn106_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningStart_Flag2_horizontalLayout.addWidget(self.flagn106_label)

        self.flagn106_lineEdit = QLineEdit(self.ss2t_Frame)
        self.flagn106_lineEdit.setObjectName(u"flagn106_lineEdit")
        self.flagn106_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn106_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn106_lineEdit.setFont(font)
        self.flagn106_lineEdit.setFrame(True)
        self.flagn106_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningStart_Flag2_horizontalLayout.addWidget(self.flagn106_lineEdit)


        self.verticalLayout_6.addLayout(self.turningStart_Flag2_horizontalLayout)

        self.flagn107_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn107_label.setObjectName(u"flagn107_label")
        self.flagn107_label.setMaximumSize(QSize(16777215, 18))
        self.flagn107_label.setFont(font)
        self.flagn107_label.setFrameShape(QFrame.Shape.Box)
        self.flagn107_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.flagn107_label)

        self.flagn108_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn108_label.setObjectName(u"flagn108_label")
        self.flagn108_label.setMaximumSize(QSize(16777215, 18))
        self.flagn108_label.setFont(font)
        self.flagn108_label.setFrameShape(QFrame.Shape.Box)
        self.flagn108_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.flagn108_label)

        self.flagn109_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn109_label.setObjectName(u"flagn109_label")
        self.flagn109_label.setMaximumSize(QSize(16777215, 18))
        self.flagn109_label.setFont(font)
        self.flagn109_label.setFrameShape(QFrame.Shape.Box)
        self.flagn109_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.flagn109_label)

        self.flagn110_label = ColorChangingFrame(self.ss2t_Frame)
        self.flagn110_label.setObjectName(u"flagn110_label")
        self.flagn110_label.setMaximumSize(QSize(16777215, 18))
        self.flagn110_label.setFont(font)
        self.flagn110_label.setFrameShape(QFrame.Shape.Box)
        self.flagn110_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.flagn110_label)


        self.horizontalLayout_53.addWidget(self.ss2t_Frame)

        self.turning_Frame = QFrame(self.turningTask_sub_Frame)
        self.turning_Frame.setObjectName(u"turning_Frame")
        self.turning_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.turning_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.turning_Frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.turning_Label = ColorChangingFrame(self.turning_Frame)
        self.turning_Label.setObjectName(u"turning_Label")
        self.turning_Label.setMaximumSize(QSize(16777215, 18))
        self.turning_Label.setFont(font)
        self.turning_Label.setFrameShape(QFrame.Shape.Box)
        self.turning_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.turning_Label)

        self.turning_horizontalLayout = QHBoxLayout()
        self.turning_horizontalLayout.setSpacing(0)
        self.turning_horizontalLayout.setObjectName(u"turning_horizontalLayout")
        self.turningMiddle_verticalLayout = QVBoxLayout()
        self.turningMiddle_verticalLayout.setSpacing(0)
        self.turningMiddle_verticalLayout.setObjectName(u"turningMiddle_verticalLayout")
        self.flagn101_label = ColorChangingFrame(self.turning_Frame)
        self.flagn101_label.setObjectName(u"flagn101_label")
        self.flagn101_label.setMaximumSize(QSize(16777215, 18))
        self.flagn101_label.setFont(font)
        self.flagn101_label.setFrameShape(QFrame.Shape.Box)
        self.flagn101_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningMiddle_verticalLayout.addWidget(self.flagn101_label)

        self.stateNumber_minus2_Label = ColorChangingFrame(self.turning_Frame)
        self.stateNumber_minus2_Label.setObjectName(u"stateNumber_minus2_Label")
        self.stateNumber_minus2_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus2_Label.setFont(font)
        self.stateNumber_minus2_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus2_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningMiddle_verticalLayout.addWidget(self.stateNumber_minus2_Label)

        self.turningMiddle_Flag1_horizontalLayout = QHBoxLayout()
        self.turningMiddle_Flag1_horizontalLayout.setSpacing(0)
        self.turningMiddle_Flag1_horizontalLayout.setObjectName(u"turningMiddle_Flag1_horizontalLayout")
        self.flagn111_label = ColorChangingFrame(self.turning_Frame)
        self.flagn111_label.setObjectName(u"flagn111_label")
        self.flagn111_label.setFont(font)
        self.flagn111_label.setFrameShape(QFrame.Shape.Box)
        self.flagn111_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn111_label.setWordWrap(True)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flagn111_label)

        self.flagn112_label = ColorChangingFrame(self.turning_Frame)
        self.flagn112_label.setObjectName(u"flagn112_label")
        self.flagn112_label.setFont(font)
        self.flagn112_label.setFrameShape(QFrame.Shape.Box)
        self.flagn112_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn112_label.setWordWrap(True)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flagn112_label)

        self.flagn111_and_flagn112_lineEdit = QLineEdit(self.turning_Frame)
        self.flagn111_and_flagn112_lineEdit.setObjectName(u"flagn111_and_flagn112_lineEdit")
        self.flagn111_and_flagn112_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn111_and_flagn112_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn111_and_flagn112_lineEdit.setFont(font)
        self.flagn111_and_flagn112_lineEdit.setFrame(True)
        self.flagn111_and_flagn112_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flagn111_and_flagn112_lineEdit)


        self.turningMiddle_verticalLayout.addLayout(self.turningMiddle_Flag1_horizontalLayout)

        self.turningMiddle_Flag2_horizontalLayout = QHBoxLayout()
        self.turningMiddle_Flag2_horizontalLayout.setSpacing(0)
        self.turningMiddle_Flag2_horizontalLayout.setObjectName(u"turningMiddle_Flag2_horizontalLayout")
        self.flagn113_label = ColorChangingFrame(self.turning_Frame)
        self.flagn113_label.setObjectName(u"flagn113_label")
        self.flagn113_label.setFont(font)
        self.flagn113_label.setFrameShape(QFrame.Shape.Box)
        self.flagn113_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn113_label.setWordWrap(True)

        self.turningMiddle_Flag2_horizontalLayout.addWidget(self.flagn113_label)

        self.flagn113_lineEdit = QLineEdit(self.turning_Frame)
        self.flagn113_lineEdit.setObjectName(u"flagn113_lineEdit")
        self.flagn113_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn113_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn113_lineEdit.setFont(font)
        self.flagn113_lineEdit.setFrame(True)
        self.flagn113_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningMiddle_Flag2_horizontalLayout.addWidget(self.flagn113_lineEdit)


        self.turningMiddle_verticalLayout.addLayout(self.turningMiddle_Flag2_horizontalLayout)


        self.turning_horizontalLayout.addLayout(self.turningMiddle_verticalLayout)

        self.turningFinal_verticalLayout = QVBoxLayout()
        self.turningFinal_verticalLayout.setSpacing(0)
        self.turningFinal_verticalLayout.setObjectName(u"turningFinal_verticalLayout")
        self.flagn102_label = ColorChangingFrame(self.turning_Frame)
        self.flagn102_label.setObjectName(u"flagn102_label")
        self.flagn102_label.setMaximumSize(QSize(16777215, 18))
        self.flagn102_label.setFont(font)
        self.flagn102_label.setFrameShape(QFrame.Shape.Box)
        self.flagn102_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningFinal_verticalLayout.addWidget(self.flagn102_label)

        self.stateNumber_minus3_Label = ColorChangingFrame(self.turning_Frame)
        self.stateNumber_minus3_Label.setObjectName(u"stateNumber_minus3_Label")
        self.stateNumber_minus3_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus3_Label.setFont(font)
        self.stateNumber_minus3_Label.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus3_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningFinal_verticalLayout.addWidget(self.stateNumber_minus3_Label)

        self.turningFinal_Flag1_horizontalLayout = QHBoxLayout()
        self.turningFinal_Flag1_horizontalLayout.setSpacing(0)
        self.turningFinal_Flag1_horizontalLayout.setObjectName(u"turningFinal_Flag1_horizontalLayout")
        self.flagn114_label = ColorChangingFrame(self.turning_Frame)
        self.flagn114_label.setObjectName(u"flagn114_label")
        self.flagn114_label.setFont(font)
        self.flagn114_label.setFrameShape(QFrame.Shape.Box)
        self.flagn114_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn114_label.setWordWrap(True)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flagn114_label)

        self.flagn115_label = ColorChangingFrame(self.turning_Frame)
        self.flagn115_label.setObjectName(u"flagn115_label")
        self.flagn115_label.setFont(font)
        self.flagn115_label.setFrameShape(QFrame.Shape.Box)
        self.flagn115_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn115_label.setWordWrap(True)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flagn115_label)

        self.flagn114_and_flagn115_lineEdit = QLineEdit(self.turning_Frame)
        self.flagn114_and_flagn115_lineEdit.setObjectName(u"flagn114_and_flagn115_lineEdit")
        self.flagn114_and_flagn115_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn114_and_flagn115_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn114_and_flagn115_lineEdit.setFont(font)
        self.flagn114_and_flagn115_lineEdit.setFrame(True)
        self.flagn114_and_flagn115_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flagn114_and_flagn115_lineEdit)


        self.turningFinal_verticalLayout.addLayout(self.turningFinal_Flag1_horizontalLayout)


        self.turning_horizontalLayout.addLayout(self.turningFinal_verticalLayout)


        self.verticalLayout_21.addLayout(self.turning_horizontalLayout)


        self.horizontalLayout_53.addWidget(self.turning_Frame)

        self.t2ss_Frame = QFrame(self.turningTask_sub_Frame)
        self.t2ss_Frame.setObjectName(u"t2ss_Frame")
        self.t2ss_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.t2ss_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.t2ss_Frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stopTurning_Label = ColorChangingFrame(self.t2ss_Frame)
        self.stopTurning_Label.setObjectName(u"stopTurning_Label")
        self.stopTurning_Label.setMaximumSize(QSize(16777215, 18))
        self.stopTurning_Label.setFont(font)
        self.stopTurning_Label.setFrameShape(QFrame.Shape.Box)
        self.stopTurning_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.stopTurning_Label)

        self.stopTurning_verticalLayout = QVBoxLayout()
        self.stopTurning_verticalLayout.setSpacing(0)
        self.stopTurning_verticalLayout.setObjectName(u"stopTurning_verticalLayout")
        self.flagn103_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn103_label.setObjectName(u"flagn103_label")
        self.flagn103_label.setMaximumSize(QSize(16777215, 18))
        self.flagn103_label.setFont(font)
        self.flagn103_label.setFrameShape(QFrame.Shape.Box)
        self.flagn103_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stopTurning_verticalLayout.addWidget(self.flagn103_label)

        self.stopTurning_StateNumber0_Label = ColorChangingFrame(self.t2ss_Frame)
        self.stopTurning_StateNumber0_Label.setObjectName(u"stopTurning_StateNumber0_Label")
        self.stopTurning_StateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.stopTurning_StateNumber0_Label.setFont(font)
        self.stopTurning_StateNumber0_Label.setFrameShape(QFrame.Shape.Box)
        self.stopTurning_StateNumber0_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stopTurning_verticalLayout.addWidget(self.stopTurning_StateNumber0_Label)

        self.stopTurning_Flag1_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag1_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag1_horizontalLayout.setObjectName(u"stopTurning_Flag1_horizontalLayout")
        self.flagn116_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn116_label.setObjectName(u"flagn116_label")
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(False)
        self.flagn116_label.setFont(font2)
        self.flagn116_label.setFrameShape(QFrame.Shape.Box)
        self.flagn116_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn116_label.setWordWrap(True)

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flagn116_label)

        self.flagn117_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn117_label.setObjectName(u"flagn117_label")
        self.flagn117_label.setFont(font2)
        self.flagn117_label.setFrameShape(QFrame.Shape.Box)
        self.flagn117_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn117_label.setWordWrap(True)

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flagn117_label)

        self.flagn116_and_flagn117_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flagn116_and_flagn117_lineEdit.setObjectName(u"flagn116_and_flagn117_lineEdit")
        self.flagn116_and_flagn117_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn116_and_flagn117_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn116_and_flagn117_lineEdit.setFont(font)
        self.flagn116_and_flagn117_lineEdit.setFrame(True)
        self.flagn116_and_flagn117_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn116_and_flagn117_lineEdit.textChanged.connect(
            lambda txt: self.label_15.setText(txt)
        )

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flagn116_and_flagn117_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag1_horizontalLayout)

        self.stopTurning_Flag2_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag2_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag2_horizontalLayout.setObjectName(u"stopTurning_Flag2_horizontalLayout")
        self.flagn118_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn118_label.setObjectName(u"flagn118_label")
        self.flagn118_label.setFont(font)
        self.flagn118_label.setFrameShape(QFrame.Shape.Box)
        self.flagn118_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn118_label.setWordWrap(True)

        self.stopTurning_Flag2_horizontalLayout.addWidget(self.flagn118_label)

        self.flagn118_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flagn118_lineEdit.setObjectName(u"flagn118_lineEdit")
        self.flagn118_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn118_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn118_lineEdit.setFont(font)
        self.flagn118_lineEdit.setFrame(True)
        self.flagn118_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stopTurning_Flag2_horizontalLayout.addWidget(self.flagn118_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag2_horizontalLayout)

        self.or_stopTurning_Label = ColorChangingFrame(self.t2ss_Frame)
        self.or_stopTurning_Label.setObjectName(u"or_stopTurning_Label")
        self.or_stopTurning_Label.setMaximumSize(QSize(16777215, 18))
        self.or_stopTurning_Label.setFont(font)
        self.or_stopTurning_Label.setFrameShape(QFrame.Shape.Box)
        self.or_stopTurning_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.or_stopTurning_Label.setWordWrap(True)

        self.stopTurning_verticalLayout.addWidget(self.or_stopTurning_Label)

        self.stopTurning_Flag31_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag31_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag31_horizontalLayout.setObjectName(u"stopTurning_Flag31_horizontalLayout")
        self.flagn119_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn119_label.setObjectName(u"flagn119_label")
        self.flagn119_label.setFont(font)
        self.flagn119_label.setFrameShape(QFrame.Shape.Box)
        self.flagn119_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn119_label.setWordWrap(True)

        self.stopTurning_Flag31_horizontalLayout.addWidget(self.flagn119_label)

        self.flagn119_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flagn119_lineEdit.setObjectName(u"flagn119_lineEdit")
        self.flagn119_lineEdit.setMinimumSize(QSize(30, 50))
        self.flagn119_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flagn119_lineEdit.setFont(font)
        self.flagn119_lineEdit.setFrame(True)
        self.flagn119_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stopTurning_Flag31_horizontalLayout.addWidget(self.flagn119_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag31_horizontalLayout)

        self.stopTurning_Flag32_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag32_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag32_horizontalLayout.setObjectName(u"stopTurning_Flag32_horizontalLayout")
        self.flagn120_label = ColorChangingFrame(self.t2ss_Frame)
        self.flagn120_label.setObjectName(u"flagn120_label")
        self.flagn120_label.setFont(font)
        self.flagn120_label.setFrameShape(QFrame.Shape.Box)
        self.flagn120_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn120_label.setWordWrap(True)

        self.stopTurning_Flag32_horizontalLayout.addWidget(self.flagn120_label)

        self.label_15 = QLabel(self.t2ss_Frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_15.setFrameShape(QFrame.Shape.Box)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stopTurning_Flag32_horizontalLayout.addWidget(self.label_15)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag32_horizontalLayout)


        self.verticalLayout_22.addLayout(self.stopTurning_verticalLayout)


        self.horizontalLayout_53.addWidget(self.t2ss_Frame)


        self.verticalLayout_28.addWidget(self.turningTask_sub_Frame)


        self.horizontalLayout_7.addWidget(self.turningTask_Frame)

        self.frame_2 = QFrame(self.Main_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.flagn121_label = ColorChangingFrame(self.frame_2)
        self.flagn121_label.setObjectName(u"flagn121_label")
        self.flagn121_label.setMaximumSize(QSize(16777215, 18))
        self.flagn121_label.setFont(font)
        self.flagn121_label.setFrameShape(QFrame.Shape.Box)
        self.flagn121_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn121_label.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.flagn121_label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Stopsd_or_Stopsq_Frame_2 = QFrame(self.frame_2)
        self.Stopsd_or_Stopsq_Frame_2.setObjectName(u"Stopsd_or_Stopsq_Frame_2")
        self.Stopsd_or_Stopsq_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Stopsd_or_Stopsq_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Stopsd_or_Stopsq_Frame_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Stopsq_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.Stopsq_label.setObjectName(u"Stopsq_label")
        self.Stopsq_label.setMaximumSize(QSize(16777215, 18))
        self.Stopsq_label.setFont(font)
        self.Stopsq_label.setFrameShape(QFrame.Shape.Box)
        self.Stopsq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Stopsq_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.Stopsq_label)

        self.flagn122_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn122_label.setObjectName(u"flagn122_label")
        self.flagn122_label.setMaximumSize(QSize(16777215, 18))
        self.flagn122_label.setFont(font)
        self.flagn122_label.setFrameShape(QFrame.Shape.Box)
        self.flagn122_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn122_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.flagn122_label)

        self.sd_stateNumber0_Label_3 = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.sd_stateNumber0_Label_3.setObjectName(u"sd_stateNumber0_Label_3")
        self.sd_stateNumber0_Label_3.setMaximumSize(QSize(16777215, 18))
        self.sd_stateNumber0_Label_3.setFont(font)
        self.sd_stateNumber0_Label_3.setFrameShape(QFrame.Shape.Box)
        self.sd_stateNumber0_Label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sd_stateNumber0_Label_3.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.sd_stateNumber0_Label_3)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.flagn126_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn126_label.setObjectName(u"flagn126_label")
        self.flagn126_label.setFont(font)
        self.flagn126_label.setFrameShape(QFrame.Shape.Box)
        self.flagn126_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn126_label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.flagn126_label)

        self.flagn127_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn127_label.setObjectName(u"flagn127_label")
        self.flagn127_label.setFont(font)
        self.flagn127_label.setFrameShape(QFrame.Shape.Box)
        self.flagn127_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn127_label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.flagn127_label)


        self.horizontalLayout_15.addLayout(self.verticalLayout_8)

        self.label_16 = QLabel(self.Stopsd_or_Stopsq_Frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_16.setFrameShape(QFrame.Shape.Box)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_16)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3 = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flag31_horizontalLayout_3")
        self.flagn128_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn128_label.setObjectName(u"flagn128_label")
        self.flagn128_label.setFont(font)
        self.flagn128_label.setFrameShape(QFrame.Shape.Box)
        self.flagn128_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn128_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.addWidget(self.flagn128_label)

        self.label_17 = QLabel(self.Stopsd_or_Stopsq_Frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_17.setFrameShape(QFrame.Shape.Box)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.addWidget(self.label_17)


        self.verticalLayout_11.addLayout(self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3 = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3")
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3 = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flage32and33_verticalLayout_3")
        self.flagn129_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn129_label.setObjectName(u"flagn129_label")
        self.flagn129_label.setFont(font)
        self.flagn129_label.setFrameShape(QFrame.Shape.Box)
        self.flagn129_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn129_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.addWidget(self.flagn129_label)

        self.flagn130_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flagn130_label.setObjectName(u"flagn130_label")
        self.flagn130_label.setFont(font)
        self.flagn130_label.setFrameShape(QFrame.Shape.Box)
        self.flagn130_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn130_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.addWidget(self.flagn130_label)


        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.addLayout(self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3)

        self.label_18 = QLabel(self.Stopsd_or_Stopsq_Frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_18.setFrameShape(QFrame.Shape.Box)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.addWidget(self.label_18)


        self.verticalLayout_11.addLayout(self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3)


        self.horizontalLayout_13.addWidget(self.Stopsd_or_Stopsq_Frame_2)

        self.ss2sd_or_ss2sq_Frame_2 = QFrame(self.frame_2)
        self.ss2sd_or_ss2sq_Frame_2.setObjectName(u"ss2sd_or_ss2sq_Frame_2")
        self.ss2sd_or_ss2sq_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.ss2sd_or_ss2sq_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ss2sd_or_ss2sq_Frame_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ss2sd_or_ss2sq_Label_2 = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.ss2sd_or_ss2sq_Label_2.setObjectName(u"ss2sd_or_ss2sq_Label_2")
        self.ss2sd_or_ss2sq_Label_2.setMaximumSize(QSize(16777215, 18))
        self.ss2sd_or_ss2sq_Label_2.setFont(font)
        self.ss2sd_or_ss2sq_Label_2.setFrameShape(QFrame.Shape.Box)
        self.ss2sd_or_ss2sq_Label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ss2sd_or_ss2sq_Label_2.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.ss2sd_or_ss2sq_Label_2)

        self.flagn123_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn123_label.setObjectName(u"flagn123_label")
        self.flagn123_label.setMaximumSize(QSize(16777215, 18))
        self.flagn123_label.setFont(font)
        self.flagn123_label.setFrameShape(QFrame.Shape.Box)
        self.flagn123_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn123_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flagn123_label)

        self.stateNumber4_or_10_Label_2 = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.stateNumber4_or_10_Label_2.setObjectName(u"stateNumber4_or_10_Label_2")
        self.stateNumber4_or_10_Label_2.setMaximumSize(QSize(16777215, 18))
        self.stateNumber4_or_10_Label_2.setFont(font)
        self.stateNumber4_or_10_Label_2.setFrameShape(QFrame.Shape.Box)
        self.stateNumber4_or_10_Label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber4_or_10_Label_2.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.stateNumber4_or_10_Label_2)

        self.flagn131_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn131_label.setObjectName(u"flagn131_label")
        self.flagn131_label.setMaximumSize(QSize(16777215, 18))
        self.flagn131_label.setFont(font)
        self.flagn131_label.setFrameShape(QFrame.Shape.Box)
        self.flagn131_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn131_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flagn131_label)

        self.flagn132_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn132_label.setObjectName(u"flagn132_label")
        self.flagn132_label.setMaximumSize(QSize(16777215, 18))
        self.flagn132_label.setFont(font)
        self.flagn132_label.setFrameShape(QFrame.Shape.Box)
        self.flagn132_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn132_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flagn132_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.flagn133_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn133_label.setObjectName(u"flagn133_label")
        self.flagn133_label.setFont(font)
        self.flagn133_label.setFrameShape(QFrame.Shape.Box)
        self.flagn133_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn133_label.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.flagn133_label)

        self.label_19 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_19.setFrameShape(QFrame.Shape.Box)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_19)


        self.verticalLayout_19.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.flagn134_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn134_label.setObjectName(u"flagn134_label")
        self.flagn134_label.setFont(font)
        self.flagn134_label.setFrameShape(QFrame.Shape.Box)
        self.flagn134_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn134_label.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.flagn134_label)

        self.flagn135_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn135_label.setObjectName(u"flagn135_label")
        self.flagn135_label.setFont(font)
        self.flagn135_label.setFrameShape(QFrame.Shape.Box)
        self.flagn135_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn135_label.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.flagn135_label)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.label_20 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_20.setFrameShape(QFrame.Shape.Box)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_20)


        self.verticalLayout_19.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.flagn136_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn136_label.setObjectName(u"flagn136_label")
        self.flagn136_label.setFont(font)
        self.flagn136_label.setFrameShape(QFrame.Shape.Box)
        self.flagn136_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn136_label.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.flagn136_label)

        self.flagn137_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn137_label.setObjectName(u"flagn137_label")
        self.flagn137_label.setFont(font)
        self.flagn137_label.setFrameShape(QFrame.Shape.Box)
        self.flagn137_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn137_label.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.flagn137_label)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.label_21 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_21.setFrameShape(QFrame.Shape.Box)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_21)


        self.verticalLayout_19.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.flagn138_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn138_label.setObjectName(u"flagn138_label")
        self.flagn138_label.setMaximumSize(QSize(16777215, 103))
        self.flagn138_label.setFont(font)
        self.flagn138_label.setFrameShape(QFrame.Shape.Box)
        self.flagn138_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn138_label.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.flagn138_label)

        self.flagn139_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn139_label.setObjectName(u"flagn139_label")
        self.flagn139_label.setMaximumSize(QSize(16777215, 103))
        self.flagn139_label.setFont(font)
        self.flagn139_label.setFrameShape(QFrame.Shape.Box)
        self.flagn139_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn139_label.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.flagn139_label)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)

        self.label_22 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_22.setFrameShape(QFrame.Shape.Box)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.flagn140_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn140_label.setObjectName(u"flagn140_label")
        self.flagn140_label.setFont(font)
        self.flagn140_label.setFrameShape(QFrame.Shape.Box)
        self.flagn140_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn140_label.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.flagn140_label)

        self.label_23 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_23.setFrameShape(QFrame.Shape.Box)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_23)


        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.flagn141_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flagn141_label.setObjectName(u"flagn141_label")
        self.flagn141_label.setFont(font)
        self.flagn141_label.setFrameShape(QFrame.Shape.Box)
        self.flagn141_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn141_label.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.flagn141_label)

        self.label_24 = QLabel(self.ss2sd_or_ss2sq_Frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(20, 20))
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_24.setFrameShape(QFrame.Shape.Box)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_13.addWidget(self.ss2sd_or_ss2sq_Frame_2)

        self.SittingDown_or_Squat_Frame_2 = QFrame(self.frame_2)
        self.SittingDown_or_Squat_Frame_2.setObjectName(u"SittingDown_or_Squat_Frame_2")
        self.SittingDown_or_Squat_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.SittingDown_or_Squat_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.SittingDown_or_Squat_Frame_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.SittingDown_or_Squat_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.SittingDown_or_Squat_Label_3.setObjectName(u"SittingDown_or_Squat_Label_3")
        self.SittingDown_or_Squat_Label_3.setMaximumSize(QSize(16777215, 18))
        self.SittingDown_or_Squat_Label_3.setFont(font)
        self.SittingDown_or_Squat_Label_3.setFrameShape(QFrame.Shape.Box)
        self.SittingDown_or_Squat_Label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.SittingDown_or_Squat_Label_3)

        self.SittingDown_or_Squat_horizontalLayout_3 = QHBoxLayout()
        self.SittingDown_or_Squat_horizontalLayout_3.setSpacing(0)
        self.SittingDown_or_Squat_horizontalLayout_3.setObjectName(u"SittingDown_or_Squat_horizontalLayout_3")
        self.sdMiddle_or_sqMiddle_verticalLayout_3 = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_verticalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_verticalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_verticalLayout_3")
        self.flagn124_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn124_label.setObjectName(u"flagn124_label")
        self.flagn124_label.setMaximumSize(QSize(16777215, 18))
        self.flagn124_label.setFont(font)
        self.flagn124_label.setFrameShape(QFrame.Shape.Box)
        self.flagn124_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn124_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout_3.addWidget(self.flagn124_label)

        self.stateNumber_minus5_or_minus11_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.stateNumber_minus5_or_minus11_Label_3.setObjectName(u"stateNumber_minus5_or_minus11_Label_3")
        self.stateNumber_minus5_or_minus11_Label_3.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus5_or_minus11_Label_3.setFont(font)
        self.stateNumber_minus5_or_minus11_Label_3.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus5_or_minus11_Label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber_minus5_or_minus11_Label_3.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout_3.addWidget(self.stateNumber_minus5_or_minus11_Label_3)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3 = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3")
        self.flagn142_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn142_label.setObjectName(u"flagn142_label")
        self.flagn142_label.setFont(font)
        self.flagn142_label.setFrameShape(QFrame.Shape.Box)
        self.flagn142_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn142_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.addWidget(self.flagn142_label)

        self.label_25 = QLabel(self.SittingDown_or_Squat_Frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_25.setFrameShape(QFrame.Shape.Box)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.addWidget(self.label_25)


        self.sdMiddle_or_sqMiddle_verticalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3 = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3")
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3 = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3")
        self.flagn143_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn143_label.setObjectName(u"flagn143_label")
        self.flagn143_label.setFont(font)
        self.flagn143_label.setFrameShape(QFrame.Shape.Box)
        self.flagn143_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn143_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.addWidget(self.flagn143_label)

        self.flagn144_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn144_label.setObjectName(u"flagn144_label")
        self.flagn144_label.setFont(font)
        self.flagn144_label.setFrameShape(QFrame.Shape.Box)
        self.flagn144_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn144_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.addWidget(self.flagn144_label)


        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3)

        self.label_26 = QLabel(self.SittingDown_or_Squat_Frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_26.setFrameShape(QFrame.Shape.Box)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.addWidget(self.label_26)


        self.sdMiddle_or_sqMiddle_verticalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3)


        self.SittingDown_or_Squat_horizontalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_verticalLayout_3)

        self.sdFinal_or_sqDeep_verticalLayout_3 = QVBoxLayout()
        self.sdFinal_or_sqDeep_verticalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_verticalLayout_3.setObjectName(u"sdFinal_or_sqDeep_verticalLayout_3")
        self.flagn125_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn125_label.setObjectName(u"flagn125_label")
        self.flagn125_label.setMaximumSize(QSize(16777215, 18))
        self.flagn125_label.setFont(font)
        self.flagn125_label.setFrameShape(QFrame.Shape.Box)
        self.flagn125_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn125_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout_3.addWidget(self.flagn125_label)

        self.stateNumber_minus6_or_minus12_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.stateNumber_minus6_or_minus12_Label_3.setObjectName(u"stateNumber_minus6_or_minus12_Label_3")
        self.stateNumber_minus6_or_minus12_Label_3.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus6_or_minus12_Label_3.setFont(font)
        self.stateNumber_minus6_or_minus12_Label_3.setFrameShape(QFrame.Shape.Box)
        self.stateNumber_minus6_or_minus12_Label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stateNumber_minus6_or_minus12_Label_3.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout_3.addWidget(self.stateNumber_minus6_or_minus12_Label_3)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3 = QHBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3")
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3 = QVBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_verticalLayout_3")
        self.flagn145_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn145_label.setObjectName(u"flagn145_label")
        self.flagn145_label.setFont(font)
        self.flagn145_label.setFrameShape(QFrame.Shape.Box)
        self.flagn145_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn145_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.addWidget(self.flagn145_label)

        self.flagn146_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flagn146_label.setObjectName(u"flagn146_label")
        self.flagn146_label.setFont(font)
        self.flagn146_label.setFrameShape(QFrame.Shape.Box)
        self.flagn146_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flagn146_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.addWidget(self.flagn146_label)


        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.addLayout(self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3)

        self.label_27 = QLabel(self.SittingDown_or_Squat_Frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_27.setFrameShape(QFrame.Shape.Box)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.addWidget(self.label_27)


        self.sdFinal_or_sqDeep_verticalLayout_3.addLayout(self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3)


        self.SittingDown_or_Squat_horizontalLayout_3.addLayout(self.sdFinal_or_sqDeep_verticalLayout_3)


        self.verticalLayout_15.addLayout(self.SittingDown_or_Squat_horizontalLayout_3)


        self.horizontalLayout_13.addWidget(self.SittingDown_or_Squat_Frame_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_7)

        self.Buttons_Frame = QFrame(self.Main_widget)
        self.Buttons_Frame.setObjectName(u"Buttons_Frame")
        self.Buttons_Frame.setMaximumSize(QSize(16777215, 5000))
        self.Buttons_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Buttons_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Buttons_Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.record_Button = QPushButton(self.Buttons_Frame)
        self.record_Button.setObjectName(u"record_Button")
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

        self.horizontalLayout_4.addWidget(self.record_Button)

        self.Apply_Button = QPushButton(self.Buttons_Frame)
        self.Apply_Button.setObjectName(u"Apply_Button")
        self.Apply_Button.setMinimumSize(QSize(121, 40))
        self.Apply_Button.setStyleSheet(u"#Apply_Button { \n"
"color: white;\n"
"background-color: rgba(81, 145, 207, 1);\n"
"border-radius: 8px;\n"
"padding: 8px;\n"
"}\n"
"\n"
"#Apply_Button:hover {\n"
"\n"
"color: white;\n"
"background-color: rgba(81, 145, 207, 1);\n"
"padding: 8px;\n"
"}\n"
"\n"
"#Apply_Button:pressed {\n"
"border: solid ;\n"
"background-color:rgbargba(241, 196, 15, 1);\n"
"}\n"
"")
        self.Apply_Button.setCheckable(False)
        self.Apply_Button.setChecked(False)
        self.Apply_Button.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.Apply_Button)

        self.Save_All_Parameters_Button = QPushButton(self.Buttons_Frame)
        self.Save_All_Parameters_Button.setObjectName(u"Save_All_Parameters_Button")
        self.Save_All_Parameters_Button.setMinimumSize(QSize(120, 40))
        self.Save_All_Parameters_Button.setStyleSheet(u"#Save_All_Parameters_Button { \n"
"color: white;\n"
"background-color: rgba(138, 38, 140, 1);\n"
"border-radius: 8px;\n"
"padding: 8px;\n"
"\n"
"}\n"
"\n"
"#Save_All_Parameters_Button:hover {\n"
"\n"
"color: white;\n"
"background-color: rgba(138, 38, 140, 1);\n"
"padding: 8px;\n"
"}\n"
"\n"
"#Save_All_Parameters_Button:pressed {\n"
"border: solid ;\n"
"background-color: rgba(241, 196, 15, 1);\n"
"padding: 8px;\n"
"}\n"
"")
        self.Save_All_Parameters_Button.setCheckable(False)
        self.Save_All_Parameters_Button.setChecked(False)
        self.Save_All_Parameters_Button.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.Save_All_Parameters_Button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.Sit2Stand_and_Stand2Sit_Mode_label = ColorChangingFrame(self.Buttons_Frame)
        self.Sit2Stand_and_Stand2Sit_Mode_label.setObjectName(u"Sit2Stand_and_Stand2Sit_Mode_label")
        self.Sit2Stand_and_Stand2Sit_Mode_label.setMinimumSize(QSize(200, 0))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setMaximumSize(QSize(16777215, 88000))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setStyleSheet(u"#Sit2Stand_and_Stand2Sit_Mode_label {\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"font-weight: bold; \n"
"}")
        self.Sit2Stand_and_Stand2Sit_Mode_label.setFrameShape(QFrame.Shape.Box)
        self.Sit2Stand_and_Stand2Sit_Mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Sit2Stand_and_Stand2Sit_Mode_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Reset_Button = QPushButton(self.Buttons_Frame)
        self.Reset_Button.setObjectName(u"Reset_Button")
        self.Reset_Button.setMinimumSize(QSize(60, 40))
        self.Reset_Button.setStyleSheet(u"#Reset_Button { \n"
"color: white;\n"
"background: rgba(255, 56, 74, 1);\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"font-weight: bold; \n"
"}\n"
"\n"
"#Reset_Button:hover {\n"
"\n"
"color: white;\n"
"background-color: rgba(220, 38, 54, 1);\n"
"\n"
"}\n"
"\n"
"#Reset_Button:pressed {\n"
"\n"
"background-color:rgba(255, 119, 131, 1);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.Reset_Button)


        self.verticalLayout_17.addWidget(self.Buttons_Frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.flagn1_label.setText(QCoreApplication.translate("Form", u"Walking Task", None))
        self.StopWalking_label.setText(QCoreApplication.translate("Form", u"Stop Walking", None))
        self.flagn2_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.stopWalking_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn16_label.setText(QCoreApplication.translate("Form", u"|RH-LH| <= wStopHipTh", None))
        self.flagn19_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn19_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flagn17_label.setText(QCoreApplication.translate("Form", u"|RKA| < wStopKneeAngTh", None))
        self.flagn16_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn16_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flagn18_label.setText(QCoreApplication.translate("Form", u"|LKA| < wStopKneeAngTh", None))
        self.flagn19_label.setText(QCoreApplication.translate("Form", u"wStopCounterLim", None))
        self.flagn17_and_flagn18_lineEdit.setText(QCoreApplication.translate("Form", u"200", None))
        self.flagn17_and_flagn18_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"200", None))
        self.ss2w_label.setText(QCoreApplication.translate("Form", u"ss2w", None))
        self.flagn3_label.setText(QCoreApplication.translate("Form", u"Walking Start", None))
        self.stateNumber1_Label.setText(QCoreApplication.translate("Form", u"1", None))
        self.flagn20_label.setText(QCoreApplication.translate("Form", u"RH > wStartHipTh", None))
        self.flagn21_label.setText(QCoreApplication.translate("Form", u"|RH-LH| > wStart HipTh", None))
        self.flagn20_and_flagn21_lineEdit.setText(QCoreApplication.translate("Form", u"7.5", None))
        self.flagn20_and_flagn21_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"7.5", None))
        self.flagn22_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ >= wStartTimuXTh", None))
        self.flagn22_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn22_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flagn23_label.setText(QCoreApplication.translate("Form", u"walkingFlag == False", None))
        self.flagn24_label.setText(QCoreApplication.translate("Form", u"turning Flag == False", None))
        self.flagn25_label.setText(QCoreApplication.translate("Form", u"sitStandFlag == False", None))
        self.flagn26_label.setText(QCoreApplication.translate("Form", u" state == StandingStill", None))
        self.walking_w_label.setText(QCoreApplication.translate("Form", u"Walking (w)", None))
        self.flagn4_label.setText(QCoreApplication.translate("Form", u"RLS", None))
        self.stateNumber2_label.setText(QCoreApplication.translate("Form", u"2", None))
        self.flagn27_label.setText(QCoreApplication.translate("Form", u"RH <= wStartHipTh", None))
        self.label.setText(QCoreApplication.translate("Form", self.flagn20_and_flagn21_lineEdit.text(), None))
        self.flagn28_label.setText(QCoreApplication.translate("Form", u"RWZ <= rlsTimuTh", None))
        self.flagn28_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn28_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn5_label.setText(QCoreApplication.translate("Form", u"RHS", None))
        self.stateNumber3_label.setText(QCoreApplication.translate("Form", u"3", None))
        self.flagn29_label.setText(QCoreApplication.translate("Form", u"RWZ <= rlsTimuTh", None))
        self.flagn29_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn30_label.setText(QCoreApplication.translate("Form", u"RH > rhsHipTh", None))
        self.flagn30_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn30_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn31_label.setText(QCoreApplication.translate("Form", u"hsWS",None))
        self.flagn32_label.setText(QCoreApplication.translate("Form", u"RK LM", None))
        self.flagn31_and_flagn32_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn31_and_flagn32_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flagn6_label.setText(QCoreApplication.translate("Form", u"LHO2MF", None))
        self.stateNumber4_label.setText(QCoreApplication.translate("Form", u"4", None))
        self.flagn33_label.setText(QCoreApplication.translate("Form", u"LWZ <= lhoTimuTh", None))
        self.flagn33_lineEdit.setText(QCoreApplication.translate("Form", self.flagn29_lineEdit.text(), None))
        self.flagn7_label.setText(QCoreApplication.translate("Form", u"LF2ET", None))
        self.stateNumber5_label.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn34_label.setText(QCoreApplication.translate("Form", u"LKA <= lfAngLim", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"-60", None))
        self.StandingStill_label_23.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flagn35_label.setText(QCoreApplication.translate("Form", u"LKA > lfAngLim", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"-60", None))
        self.flagn36_label.setText(QCoreApplication.translate("Form", u"LKA <= LHOKA + lfMin AllowAng", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn37_label.setText(QCoreApplication.translate("Form", u"LKV >= lf2etKnee VelTh", None))
        self.flagn37_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn37_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn8_label.setText(QCoreApplication.translate("Form", u"Lextension", None))
        self.stateNumber6_label.setText(QCoreApplication.translate("Form", u"6", None))
        self.flagn38_label.setText(QCoreApplication.translate("Form", u"LKV > lf2etKnee VelTh", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn9_label.setText(QCoreApplication.translate("Form", u"Lextended", None))
        self.stateNumber7_label.setText(QCoreApplication.translate("Form", u"7", None))
        self.flagn39_label.setText(QCoreApplication.translate("Form", u"LKA >= leAngLim", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn10_label.setText(QCoreApplication.translate("Form", u"LLS", None))
        self.stateNumber8_label.setText(QCoreApplication.translate("Form", u"8", None))
        self.flagn40_label.setText(QCoreApplication.translate("Form", u"LWZ >= llsTimuTh", None))
        self.flagn40_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn40_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn11_label.setText(QCoreApplication.translate("Form", u"LHS", None))
        self.stateNumber9_label.setText(QCoreApplication.translate("Form", u"9", None))
        self.flagn41_label.setText(QCoreApplication.translate("Form", u"LWZ >= llsTimuTh", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn42_label.setText(QCoreApplication.translate("Form", u"LH > lhsHipTh", None))
        self.flagn42_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn42_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn43_label.setText(QCoreApplication.translate("Form", u"hsWS", None))
        self.flagn44_label.setText(QCoreApplication.translate("Form", u"LK LM", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn12_label.setText(QCoreApplication.translate("Form", u"RHO2MF", None))
        self.stateNumber10_label.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn45_label.setText(QCoreApplication.translate("Form", u"RWZ >= rhoTimuTh", None))
        self.flagn45_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn13_label.setText(QCoreApplication.translate("Form", u"RF2ET", None))
        self.stateNumber11_label.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn46_label.setText(QCoreApplication.translate("Form", u"RKA >= rfAngLim", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"60", None))
        self.StandingStill_label_35.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flagn47_label.setText(QCoreApplication.translate("Form", u"RKA < rfAngLim", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"60", None))
        self.flagn48_label.setText(QCoreApplication.translate("Form", u"RKA >= RHOKA + rfMin AllowAng", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn49_label.setText(QCoreApplication.translate("Form", u"RKV <= rf2etKnee VelTh", None))
        self.flagn49_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn49_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn14_label.setText(QCoreApplication.translate("Form", u"Rextension", None))
        self.stateNumber12_label.setText(QCoreApplication.translate("Form", u"12", None))
        self.flagn50_label.setText(QCoreApplication.translate("Form", u"RKV < rf2etKnee VelTh", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn15_label.setText(QCoreApplication.translate("Form", u"Rextended", None))
        self.stateNumber13_label.setText(QCoreApplication.translate("Form", u"13", None))
        self.flagn51_label.setText(QCoreApplication.translate("Form", u"RKA <= reAngLim", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn52_label.setText(QCoreApplication.translate("Form", u"Stand2Sit, Sit2Stand Task", None))
        self.Stopsd_or_Stopsq_Label.setText(QCoreApplication.translate("Form", u"Stop sd", None))
        self.flagn53_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.sd_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn61_label.setText(QCoreApplication.translate("Form", u"RH < sdStopHTh", None))
        self.flagn62_label.setText(QCoreApplication.translate("Form", u"LH < sdStopHTh", None))
        self.flagn61_and_flagn62_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn61_and_flagn62_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flagn63_label.setText(QCoreApplication.translate("Form", u"sdStopWS", None))
        self.flagn63_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.flagn63_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.flagn64_label.setText(QCoreApplication.translate("Form", u"RKA < sdStopKneeAngTh", None))
        self.flagn65_label.setText(QCoreApplication.translate("Form", u"|LKA| < sdStopKneeAngTh", None))
        self.flagn64_and_flagn65_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn64_and_flagn65_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.ss2sd_Label.setText(QCoreApplication.translate("Form", u"ss2sd", None))
        self.flagn54_label.setText(QCoreApplication.translate("Form", u"sd Start", None))
        self.stateNumber4_or_10_Label.setText(QCoreApplication.translate("Form", u"-4 ", None))
        self.flagn66_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ <= sdStartTimuXTh", None))
        self.flagn66_lineEdit.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn66_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn67_label.setText(QCoreApplication.translate("Form", u"RKA >= sdStartKneeAngTh", None))
        self.flagn68_label.setText(QCoreApplication.translate("Form", u"|LKA| >= sdStartKneeAngTh", None))
        self.flagn67_and_flagn68_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn67_and_flagn68_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flagn69_label.setText(QCoreApplication.translate("Form", u"RKV > sdStartKneeVelTh", None))
        self.flagn70_label.setText(QCoreApplication.translate("Form", u"LKV < sdStartKneeVelTh", None))
        self.flagn69_and_flagn70_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn69_and_flagn70_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flagn71_label.setText(QCoreApplication.translate("Form", u"RH >= sdStartHipTh", None))
        self.flagn72_label.setText(QCoreApplication.translate("Form", u"LH >= sdStartHipTh", None))
        self.flagn71_and_flagn72_lineEdit.setText(QCoreApplication.translate("Form", u"22", None))
        self.flagn71_and_flagn72_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"22", None))
        self.flagn73_label.setText(QCoreApplication.translate("Form", u"walkingFlag == False", None))
        self.flagn74_label.setText(QCoreApplication.translate("Form", u"turningFlag == False", None))
        self.flagn75_label.setText(QCoreApplication.translate("Form", u"sitStandFlag == False", None))
        self.flagn76_label.setText(QCoreApplication.translate("Form", u"state == StandingStill", None))
        self.flagn77_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.flagn77_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn77_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flagn78_label.setText(QCoreApplication.translate("Form", u"BWX < sdStartBimuTh", None))
        self.flagn78_lineEdit.setText(QCoreApplication.translate("Form", u"-5", None))
        self.flagn78_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-5", None))
        self.SittingDown_or_Squat_Label.setText(QCoreApplication.translate("Form", u"Sitting Down (sd)", None))
        self.flagn55_label.setText(QCoreApplication.translate("Form", u"sd Middle", None))
        self.stateNumber_minus5_or_minus11_Label.setText(QCoreApplication.translate("Form", u"-5", None))
        self.flagn79_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn80_label.setText(QCoreApplication.translate("Form", u"RKA >= sd Middle Knee Ang Th", None))
        self.flagn81_label.setText(QCoreApplication.translate("Form", u"|LKA| >= sd Middle Knee Ang Th", None))
        self.flagn80_and_flagn81_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn80_and_flagn81_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flagn56_label.setText(QCoreApplication.translate("Form", u"sd Final", None))
        self.stateNumber_minus6_or_minus12_Label.setText(QCoreApplication.translate("Form", u"-6", None))
        self.flagn82_label.setText(QCoreApplication.translate("Form", u"RKA > sd Final Knee Ang Th", None))
        self.flagn83_label.setText(QCoreApplication.translate("Form", u"|LKA| > sd Final Knee Ang Th", None))
        self.flagn82_and_flagn83_lineEdit.setText(QCoreApplication.translate("Form", u"65", None))
        self.flagn82_and_flagn83_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"65", None))
        self.flagn57_label.setText(QCoreApplication.translate("Form", u"Seated", None))
        self.stateNumber_minus7_Label.setText(QCoreApplication.translate("Form", u"-7", None))
        self.flagn84_label.setText(QCoreApplication.translate("Form", u"seatedWS", None))
        self.flagn84_lineEdit.setText(QCoreApplication.translate("Form", u"50", None))
        self.flagn84_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"50", None))
        self.flagn85_label.setText(QCoreApplication.translate("Form", u"|RWZ| < seatedTimuTh", None))
        self.flagn86_label.setText(QCoreApplication.translate("Form", u"|LWZ| < seatedTimuTh", None))
        self.flagn85_and_flagn86_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn85_and_flagn86_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.or_seated_Label.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flagn87_label.setText(QCoreApplication.translate("Form", u"RKA >=  sdFinalKneeAngTh + seatedAddedKneeAng", None))
        self.flagn88_label.setText(QCoreApplication.translate("Form", u"|LKA| >= sdFinalKneeAngTh + seatedAddedKneeAng", None))
        self.flagn87_and_flagn88_lineEdit.setText(QCoreApplication.translate("Form", u"15", None))
        self.flagn87_and_flagn88_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.flagn58_label.setText(QCoreApplication.translate("Form", u"Seated2su", None))
        self.stateNumber_minus8_Label.setText(QCoreApplication.translate("Form", u"-8", None))
        self.flagn89_label.setText(QCoreApplication.translate("Form", u"RKA > seated2suMinAllowKneeAng", None))
        self.flagn90_label.setText(QCoreApplication.translate("Form", u"|LKA| > seated2suMinAllowKneeAng", None))
        self.flagn89_and_flagn90_lineEdit.setText(QCoreApplication.translate("Form", u"65", None))
        self.flagn89_and_flagn90_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"65", None))
        self.flagn91_label.setText(QCoreApplication.translate("Form", u"seated2suWS", None))
        self.flagn91_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn91_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flagn92_label.setText(QCoreApplication.translate("Form", u"|BWX| < seated2suBimuTh", None))
        self.flagn92_lineEdit.setText(QCoreApplication.translate("Form", u"-30", None))
        self.flagn92_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-30", None))
        self.flagn59_label.setText(QCoreApplication.translate("Form", u"StandingUp (su)", None))
        self.stateNumber_minus9_Label.setText(QCoreApplication.translate("Form", u"-9", None))
        self.flagn93_label.setText(QCoreApplication.translate("Form", u"elapsedTime > timeRisePeak", None))
        self.flagn93_lineEdit.setText(QCoreApplication.translate("Form", u"0.15", None))
        self.flagn93_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.15", None))
        self.su2ss_Label.setText(QCoreApplication.translate("Form", u"su2ss", None))
        self.flagn60_label.setText(QCoreApplication.translate("Form", u"StandingStill", None))
        self.su2ss_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn94_label.setText(QCoreApplication.translate("Form", u"RKA < su2ssKneeAngTh", None))
        self.flagn95_label.setText(QCoreApplication.translate("Form", u"|LKA| < su2ssKneeAngTh", None))
        self.flagn94_and_flagn95_lineEdit.setText(QCoreApplication.translate("Form", u"15", None))
        self.flagn94_and_flagn95_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.flagn96_label.setText(QCoreApplication.translate("Form", u"su2ssWS", None))
        self.flagn96_lineEdit.setText(QCoreApplication.translate("Form", u"20", None))
        self.flagn96_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"20", None))
        self.flagn97_label.setText(QCoreApplication.translate("Form", u"|RKV| < su2ssKneeVelTh", None))
        self.flagn98_label.setText(QCoreApplication.translate("Form", u"|LKV| < su2ssKneeVelTh", None))
        self.flagn97_and_flagn98_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn97_and_flagn98_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flagn99_label.setText(QCoreApplication.translate("Form", u"Turning Task", None))
        self.ss2t_Label.setText(QCoreApplication.translate("Form", u"ss2t", None))
        self.flagn100_label.setText(QCoreApplication.translate("Form", u"Turning Start", None))
        self.stateNumber_minus1_Label.setText(QCoreApplication.translate("Form", u"-1", None))
        self.flagn104_label.setText(QCoreApplication.translate("Form", u"|RWY| > tStartTimuTh", None))
        self.flagn105_label.setText(QCoreApplication.translate("Form", u"|LWY| > tStartTimuTh", None))
        self.flagn104_and_flagn105_lineEdit.setText(QCoreApplication.translate("Form", u"80", None))
        self.flagn104_and_flagn105_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"80", None))
        self.flagn106_label.setText(QCoreApplication.translate("Form", u"|BWY| > tStartBimuTh", None))
        self.flagn106_lineEdit.setText(QCoreApplication.translate("Form", u"40", None))
        self.flagn106_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"40", None))
        self.flagn107_label.setText(QCoreApplication.translate("Form", u"walkingFlag == False", None))
        self.flagn108_label.setText(QCoreApplication.translate("Form", u"turningFlag == False", None))
        self.flagn109_label.setText(QCoreApplication.translate("Form", u"sitStandFlag == False", None))
        self.flagn110_label.setText(QCoreApplication.translate("Form", u"state == StandingStill", None))
        self.turning_Label.setText(QCoreApplication.translate("Form", u"Turning (t)", None))
        self.flagn101_label.setText(QCoreApplication.translate("Form", u"Turning Middle", None))
        self.stateNumber_minus2_Label.setText(QCoreApplication.translate("Form", u"-2", None))
        self.flagn111_label.setText(QCoreApplication.translate("Form", u"|RWY| > tMiddleTimuTh", None))
        self.flagn112_label.setText(QCoreApplication.translate("Form", u"|LWY| > tMiddleTimuTh", None))
        self.flagn111_and_flagn112_lineEdit.setText(QCoreApplication.translate("Form", u"135", None))
        self.flagn111_and_flagn112_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"135", None))
        self.flagn113_label.setText(QCoreApplication.translate("Form", u"|BWY| > tMiddleBimuTh", None))
        self.flagn113_lineEdit.setText(QCoreApplication.translate("Form", u"70", None))
        self.flagn113_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"70", None))
        self.flagn102_label.setText(QCoreApplication.translate("Form", u"Turning Final", None))
        self.stateNumber_minus3_Label.setText(QCoreApplication.translate("Form", u"-3", None))
        self.flagn114_label.setText(QCoreApplication.translate("Form", u"|RWY| > tFinalTimuTh", None))
        self.flagn115_label.setText(QCoreApplication.translate("Form", u"|LWY| > tFinalTimuTh", None))
        self.flagn114_and_flagn115_lineEdit.setText(QCoreApplication.translate("Form", u"120", None))
        self.flagn114_and_flagn115_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"120", None))
        self.stopTurning_Label.setText(QCoreApplication.translate("Form", u"Stop Turning", None))
        self.flagn103_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.stopTurning_StateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn116_label.setText(QCoreApplication.translate("Form", u"|RWY| < tStopTimuTh", None))
        self.flagn117_label.setText(QCoreApplication.translate("Form", u"|LWY| < tStopTimuTh", None))
        self.flagn116_and_flagn117_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn116_and_flagn117_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flagn118_label.setText(QCoreApplication.translate("Form", u"|BWY| < tStopBimuTh", None))
        self.flagn118_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn118_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.or_stopTurning_Label.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flagn119_label.setText(QCoreApplication.translate("Form", u"tWS", None))
        self.flagn119_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.flagn119_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.flagn120_label.setText(QCoreApplication.translate("Form", u"|LWY| < tStopTimuTh", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"10", None))
        self.flagn121_label.setText(QCoreApplication.translate("Form", u"Squat Task", None))
        self.Stopsq_label.setText(QCoreApplication.translate("Form", u"Stop sq", None))
        self.flagn122_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.sd_stateNumber0_Label_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn126_label.setText(QCoreApplication.translate("Form", u"RH < sdStopHTh", None))
        self.flagn127_label.setText(QCoreApplication.translate("Form", u"LH < sdStopHTh", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn128_label.setText(QCoreApplication.translate("Form", u"sdStopWS", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"100", None))
        self.flagn129_label.setText(QCoreApplication.translate("Form", u"RKA < sdStopKneeAngTh", None))
        self.flagn130_label.setText(QCoreApplication.translate("Form", u"|LKA| < sdStopKneeAngTh", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"5", None))
        self.ss2sd_or_ss2sq_Label_2.setText(QCoreApplication.translate("Form", u"ss2sq", None))
        self.flagn123_label.setText(QCoreApplication.translate("Form", u"Squat Start", None))
        self.stateNumber4_or_10_Label_2.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn131_label.setText(QCoreApplication.translate("Form", u"Squat Flag", None))
        self.flagn132_label.setText(QCoreApplication.translate("Form", u"state == standing still", None))
        self.flagn133_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ <= sdStartTimuXTh", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flagn134_label.setText(QCoreApplication.translate("Form", u"RKA >= sdStartKneeAngTh", None))
        self.flagn135_label.setText(QCoreApplication.translate("Form", u"|LKA| >= sdStartKneeAngTh", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn136_label.setText(QCoreApplication.translate("Form", u"RKV > sdStartKneeVelTh", None))
        self.flagn137_label.setText(QCoreApplication.translate("Form", u"LKV < sdStartKneeVelTh", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"0", None))
        self.flagn138_label.setText(QCoreApplication.translate("Form", u"RH >= sdStartHipTh", None))
        self.flagn139_label.setText(QCoreApplication.translate("Form", u"LH >= sdStartHipTh", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"22", None))
        self.flagn140_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn141_label.setText(QCoreApplication.translate("Form", u"BWX < sdStartBimuTh", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"-5", None))
        self.SittingDown_or_Squat_Label_3.setText(QCoreApplication.translate("Form", u"Squat (sq)", None))
        self.flagn124_label.setText(QCoreApplication.translate("Form", u"sq Middle", None))
        self.stateNumber_minus5_or_minus11_Label_3.setText(QCoreApplication.translate("Form", u"-11", None))
        self.flagn142_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"11", None))
        self.flagn143_label.setText(QCoreApplication.translate("Form", u"RKA >= sd Middle Knee Ang Th", None))
        self.flagn144_label.setText(QCoreApplication.translate("Form", u"|LKA|>= sd Middle Knee Ang Th", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"5", None))
        self.flagn125_label.setText(QCoreApplication.translate("Form", u"sq Deep", None))
        self.stateNumber_minus6_or_minus12_Label_3.setText(QCoreApplication.translate("Form", u"-12", None))
        self.flagn145_label.setText(QCoreApplication.translate("Form", u"RKA > sd Final Knee Ang Th", None))
        self.flagn146_label.setText(QCoreApplication.translate("Form", u"|LKA| > sd Final Knee Ang Th", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"65", None))
        self.record_Button.setText("")
        self.Apply_Button.setText(QCoreApplication.translate("Form", u"Apply Advanced Parameters", None))
        self.Save_All_Parameters_Button.setText(QCoreApplication.translate("Form", u"Save All Parameters", None))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setText(QCoreApplication.translate("Form", u"Sti2Stand and Stand2Sit", None))
        self.Reset_Button.setText(QCoreApplication.translate("Form", u"Reset Advanced Parameters", None))
    # retranslateUi

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QSize # Import QSize for fixed size if needed
 # Import QSize for fixed size if needed

class ColorChangingFrame(QLabel): # Inherit directly from ColorChangingFrame
    def __init__(self, *args, **kwargs):
        # Call the ColorChangingFrame constructor with all arguments passed
        super().__init__(*args, **kwargs)

        self.flag = False
        self.update_color()
        # self.setTextFormat(Qt.PlainText)
        # self.setWordWrap(True)
        # self.setStyleSheet("color: black;")

    def update_color(self):

        if self.flag:
            self.setStyleSheet("background-color: lightgreen;color: black;font-weight:bold;")
        else:
            self.setStyleSheet("background-color: lightcoral;color: black;font-weight:bold;")