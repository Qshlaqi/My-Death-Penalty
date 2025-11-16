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
import resources_rc


class DebugPage(QWidget):
    def __init__(self):
        super().__init__()

        self.Main_widget = QWidget(self)
        self.Main_widget.setObjectName(u"Main_widget")
        self.Main_widget.setGeometry(QRect(0, 10, 1310, 780))
        self.verticalLayout_17 = QVBoxLayout(self.Main_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.Main_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.flag110_label = ColorChangingFrame(self.frame)
        self.flag110_label.setObjectName(u"flag110_label")
        font = QFont()
        font.setPointSize(6)
        self.flag110_label.setFont(font)
        self.flag110_label.setFrameShape(QFrame.Box)
        self.flag110_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.flag110_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stopWalking_Frame = QFrame(self.frame)
        self.stopWalking_Frame.setObjectName(u"stopWalking_Frame")
        self.stopWalking_Frame.setFrameShape(QFrame.Box)
        self.stopWalking_Frame.setFrameShadow(QFrame.Plain)
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
        self.StopWalking_label.setFrameShape(QFrame.Box)
        self.StopWalking_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.StopWalking_label)

        self.flag126_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flag126_label.setObjectName(u"flag126_label")
        self.flag126_label.setMinimumSize(QSize(120, 0))
        self.flag126_label.setMaximumSize(QSize(16777215, 18))
        self.flag126_label.setFont(font)
        self.flag126_label.setFrameShape(QFrame.Box)
        self.flag126_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.flag126_label)

        self.stopWalking_stateNumber0_Label = ColorChangingFrame(self.stopWalking_Frame)
        self.stopWalking_stateNumber0_Label.setObjectName(u"stopWalking_stateNumber0_Label")
        self.stopWalking_stateNumber0_Label.setMinimumSize(QSize(120, 0))
        self.stopWalking_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.stopWalking_stateNumber0_Label.setFont(font)
        self.stopWalking_stateNumber0_Label.setFrameShape(QFrame.Box)
        self.stopWalking_stateNumber0_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.stopWalking_stateNumber0_Label)

        self.stoWalking_Flag1_horizontalLayout = QHBoxLayout()
        self.stoWalking_Flag1_horizontalLayout.setSpacing(0)
        self.stoWalking_Flag1_horizontalLayout.setObjectName(u"stoWalking_Flag1_horizontalLayout")
        self.flag68_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flag68_label.setObjectName(u"flag68_label")
        self.flag68_label.setFont(font)
        self.flag68_label.setFrameShape(QFrame.Box)
        self.flag68_label.setAlignment(Qt.AlignCenter)
        self.flag68_label.setWordWrap(True)
        self.stoWalking_Flag1_horizontalLayout.addWidget(self.flag68_label)

        self.flag68_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flag68_lineEdit.setObjectName(u"flag68_lineEdit")
        self.flag68_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag68_lineEdit.setMaximumSize(QSize(30, 1560000))
        self.flag68_lineEdit.setFont(font)
        self.flag68_lineEdit.setFrame(True)
        self.flag68_lineEdit.setAlignment(Qt.AlignCenter)

     

        self.stoWalking_Flag1_horizontalLayout.addWidget(self.flag68_lineEdit)


        self.verticalLayout_4.addLayout(self.stoWalking_Flag1_horizontalLayout)

        self.stoWalking_Flag2_horizontalLayout = QHBoxLayout()
        self.stoWalking_Flag2_horizontalLayout.setSpacing(0)
        self.stoWalking_Flag2_horizontalLayout.setObjectName(u"stoWalking_Flag2_horizontalLayout")
        self.flag69_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flag69_label.setObjectName(u"flag69_label")
        self.flag69_label.setFont(font)
        self.flag69_label.setFrameShape(QFrame.Box)
        self.flag69_label.setAlignment(Qt.AlignCenter)
        self.flag69_label.setWordWrap(True)

        self.stoWalking_Flag2_horizontalLayout.addWidget(self.flag69_label)

        self.flag69_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flag69_lineEdit.setObjectName(u"flag69_lineEdit")
        self.flag69_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag69_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag69_lineEdit.setFont(font)
        self.flag69_lineEdit.setFrame(True)
        self.flag69_lineEdit.setAlignment(Qt.AlignCenter)

        self.stoWalking_Flag2_horizontalLayout.addWidget(self.flag69_lineEdit)

        self.StopWalking_Flag1and14_horizontalLayout = QHBoxLayout()
        self.StopWalking_Flag1and14_horizontalLayout.setSpacing(0)
        self.StopWalking_Flag1and14_horizontalLayout.setObjectName(u"StopWalking_Flag1and14_horizontalLayout")
        self.StopWalking_Flag1and14_verticalLayout = QVBoxLayout()
        self.StopWalking_Flag1and14_verticalLayout.setSpacing(0)
        self.StopWalking_Flag1and14_verticalLayout.setObjectName(u"StopWalking_Flag1and14_verticalLayout")
        self.flag70_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flag70_label.setObjectName(u"flag70_label")
        self.flag70_label.setFont(font)
        self.flag70_label.setFrameShape(QFrame.Box)
        self.flag70_label.setAlignment(Qt.AlignCenter)
        self.flag70_label.setWordWrap(True)

        self.StopWalking_Flag1and14_verticalLayout.addWidget(self.flag70_label)

        self.verticalLayout_4.addLayout(self.stoWalking_Flag2_horizontalLayout)


        self.flag71_label = ColorChangingFrame(self.stopWalking_Frame)
        self.flag71_label.setObjectName(u"flag71_label")
        self.flag71_label.setFont(font)
        self.flag71_label.setFrameShape(QFrame.Box)
        self.flag71_label.setAlignment(Qt.AlignCenter)
        self.flag71_label.setWordWrap(True)

        self.StopWalking_Flag1and14_verticalLayout.addWidget(self.flag71_label)


        self.StopWalking_Flag1and14_horizontalLayout.addLayout(self.StopWalking_Flag1and14_verticalLayout)

        self.flag70_and_flag71_lineEdit = QLineEdit(self.stopWalking_Frame)
        self.flag70_and_flag71_lineEdit.setObjectName(u"flag70_and_flag71_lineEdit")
        self.flag70_and_flag71_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag70_and_flag71_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag70_and_flag71_lineEdit.setFont(font)
        self.flag70_and_flag71_lineEdit.setFrame(True)
        self.flag70_and_flag71_lineEdit.setAlignment(Qt.AlignCenter)

        self.StopWalking_Flag1and14_horizontalLayout.addWidget(self.flag70_and_flag71_lineEdit)


        self.verticalLayout_4.addLayout(self.StopWalking_Flag1and14_horizontalLayout)


        self.horizontalLayout.addWidget(self.stopWalking_Frame)

        self.ss2w_Frame = QFrame(self.frame)
        self.ss2w_Frame.setObjectName(u"ss2w_Frame")
        self.ss2w_Frame.setFrameShape(QFrame.NoFrame)
        self.ss2w_Frame.setFrameShadow(QFrame.Raised)
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
        self.ss2w_label.setFrameShape(QFrame.Box)
        self.ss2w_label.setFrameShadow(QFrame.Plain)
        self.ss2w_label.setAlignment(Qt.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.ss2w_label)

        self.flag130_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag130_label.setObjectName(u"flag130_label")
        self.flag130_label.setMaximumSize(QSize(900, 18))
        self.flag130_label.setFont(font)
        self.flag130_label.setFrameShape(QFrame.Box)
        self.flag130_label.setAlignment(Qt.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.flag130_label)

        self.stateNumber1_Label = ColorChangingFrame(self.ss2w_Frame)
        self.stateNumber1_Label.setObjectName(u"stateNumber1_Label")
        self.stateNumber1_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber1_Label.setFont(font)
        self.stateNumber1_Label.setFrameShape(QFrame.Box)
        self.stateNumber1_Label.setAlignment(Qt.AlignCenter)

        self.ss2w_verticalLayout.addWidget(self.stateNumber1_Label)

        self.wstartHipTh_horizontalLayout = QHBoxLayout()
        self.wstartHipTh_horizontalLayout.setSpacing(0)
        self.wstartHipTh_horizontalLayout.setObjectName(u"wstartHipTh_horizontalLayout")
        self.walkingStart_Flag12_verticalLayout = QVBoxLayout()
        self.walkingStart_Flag12_verticalLayout.setSpacing(0)
        self.walkingStart_Flag12_verticalLayout.setObjectName(u"walkingStart_Flag12_verticalLayout")
        self.flag36_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag36_label.setObjectName(u"flag36_label")
        self.flag36_label.setFont(font)
        self.flag36_label.setFrameShape(QFrame.Box)
        self.flag36_label.setAlignment(Qt.AlignCenter)
        self.flag36_label.setWordWrap(True)

        self.walkingStart_Flag12_verticalLayout.addWidget(self.flag36_label)

        self.flag37_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag37_label.setObjectName(u"flag37_label")
        self.flag37_label.setFont(font)
        self.flag37_label.setFrameShape(QFrame.Box)
        self.flag37_label.setAlignment(Qt.AlignCenter)
        self.flag37_label.setWordWrap(True)

        self.walkingStart_Flag12_verticalLayout.addWidget(self.flag37_label)


        self.wstartHipTh_horizontalLayout.addLayout(self.walkingStart_Flag12_verticalLayout)

        self.flag36_and_flag37_lineEdit = QLineEdit(self.ss2w_Frame)
        self.flag36_and_flag37_lineEdit.setObjectName(u"flag36_and_flag37_lineEdit")
        self.flag36_and_flag37_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag36_and_flag37_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag36_and_flag37_lineEdit.setFont(font)
        self.flag36_and_flag37_lineEdit.setFrame(True)
        self.flag36_and_flag37_lineEdit.setAlignment(Qt.AlignCenter)

        self.wstartHipTh_horizontalLayout.addWidget(self.flag36_and_flag37_lineEdit)


        self.ss2w_verticalLayout.addLayout(self.wstartHipTh_horizontalLayout)

        self.walkingStart_Flag3_horizontalLayout = QHBoxLayout()
        self.walkingStart_Flag3_horizontalLayout.setSpacing(0)
        self.walkingStart_Flag3_horizontalLayout.setObjectName(u"walkingStart_Flag3_horizontalLayout")
        self.flag38_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag38_label.setObjectName(u"flag38_label")
        self.flag38_label.setMinimumSize(QSize(80, 0))
        self.flag38_label.setFont(font)
        self.flag38_label.setFrameShape(QFrame.Box)
        self.flag38_label.setTextFormat(Qt.AutoText)
        self.flag38_label.setAlignment(Qt.AlignCenter)
        self.flag38_label.setWordWrap(True)

        self.walkingStart_Flag3_horizontalLayout.addWidget(self.flag38_label)

        self.flag38_lineEdit = QLineEdit(self.ss2w_Frame)
        self.flag38_lineEdit.setObjectName(u"flag38_lineEdit")
        self.flag38_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag38_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag38_lineEdit.setFont(font)
        self.flag38_lineEdit.setFrame(True)
        self.flag38_lineEdit.setAlignment(Qt.AlignCenter)

        self.walkingStart_Flag3_horizontalLayout.addWidget(self.flag38_lineEdit)


        self.ss2w_verticalLayout.addLayout(self.walkingStart_Flag3_horizontalLayout)

        self.flag39_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag39_label.setObjectName(u"flag39_label")
        self.flag39_label.setMaximumSize(QSize(16777215, 18))
        self.flag39_label.setFont(font)
        self.flag39_label.setFrameShape(QFrame.Box)
        self.flag39_label.setAlignment(Qt.AlignCenter)
        self.flag39_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flag39_label)

        self.flag40_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag40_label.setObjectName(u"flag40_label")
        self.flag40_label.setMaximumSize(QSize(16777215, 18))
        self.flag40_label.setFont(font)
        self.flag40_label.setFrameShape(QFrame.Box)
        self.flag40_label.setAlignment(Qt.AlignCenter)
        self.flag40_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flag40_label)

        self.flag41_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag41_label.setObjectName(u"flag41_label")
        self.flag41_label.setMaximumSize(QSize(16777215, 18))
        self.flag41_label.setFont(font)
        self.flag41_label.setFrameShape(QFrame.Box)
        self.flag41_label.setAlignment(Qt.AlignCenter)
        self.flag41_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flag41_label)

        self.flag42_label = ColorChangingFrame(self.ss2w_Frame)
        self.flag42_label.setObjectName(u"flag42_label")
        self.flag42_label.setMaximumSize(QSize(16777215, 18))
        self.flag42_label.setFont(font)
        self.flag42_label.setFrameShape(QFrame.Box)
        self.flag42_label.setAlignment(Qt.AlignCenter)
        self.flag42_label.setWordWrap(True)

        self.ss2w_verticalLayout.addWidget(self.flag42_label)


        self.horizontalLayout_3.addLayout(self.ss2w_verticalLayout)


        self.horizontalLayout.addWidget(self.ss2w_Frame)

        self.walking_verticalLayout = QVBoxLayout()
        self.walking_verticalLayout.setSpacing(0)
        self.walking_verticalLayout.setObjectName(u"walking_verticalLayout")
        self.walking_w_label = ColorChangingFrame(self.frame)
        self.walking_w_label.setObjectName(u"walking_w_label")
        self.walking_w_label.setFont(font)
        self.walking_w_label.setFrameShape(QFrame.Box)
        self.walking_w_label.setAlignment(Qt.AlignCenter)

        self.walking_verticalLayout.addWidget(self.walking_w_label)

        self.walikng_horizontalLayout = QHBoxLayout()
        self.walikng_horizontalLayout.setSpacing(0)
        self.walikng_horizontalLayout.setObjectName(u"walikng_horizontalLayout")
        self.RLS_Frame = QFrame(self.frame)
        self.RLS_Frame.setObjectName(u"RLS_Frame")
        self.RLS_Frame.setFrameShape(QFrame.Box)
        self.RLS_Frame.setFrameShadow(QFrame.Plain)
        self.RLS_Frame.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.RLS_Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.RLS_verticalLayout = QVBoxLayout()
        self.RLS_verticalLayout.setSpacing(0)
        self.RLS_verticalLayout.setObjectName(u"RLS_verticalLayout")
        self.flag131_label = ColorChangingFrame(self.RLS_Frame)
        self.flag131_label.setObjectName(u"flag131_label")
        self.flag131_label.setMinimumSize(QSize(0, 18))
        self.flag131_label.setMaximumSize(QSize(16777215, 18))
        self.flag131_label.setFont(font)
        self.flag131_label.setFrameShape(QFrame.Box)
        self.flag131_label.setAlignment(Qt.AlignCenter)

        self.RLS_verticalLayout.addWidget(self.flag131_label)

        self.stateNumber2_label = ColorChangingFrame(self.RLS_Frame)
        self.stateNumber2_label.setObjectName(u"stateNumber2_label")
        self.stateNumber2_label.setMinimumSize(QSize(0, 18))
        self.stateNumber2_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber2_label.setFont(font)
        self.stateNumber2_label.setFrameShape(QFrame.Box)
        self.stateNumber2_label.setAlignment(Qt.AlignCenter)

        self.RLS_verticalLayout.addWidget(self.stateNumber2_label)

        self.RLS_Flag1_horizontallLayout = QHBoxLayout()
        self.RLS_Flag1_horizontallLayout.setSpacing(0)
        self.RLS_Flag1_horizontallLayout.setObjectName(u"RLS_Flag1_horizontallLayout")
        self.flag43_label = ColorChangingFrame(self.RLS_Frame)
        self.flag43_label.setObjectName(u"flag43_label")
        self.flag43_label.setMinimumSize(QSize(0, 0))
        self.flag43_label.setMaximumSize(QSize(8000, 900))
        self.flag43_label.setFont(font)
        self.flag43_label.setFrameShape(QFrame.Box)
        self.flag43_label.setAlignment(Qt.AlignCenter)
        self.flag43_label.setWordWrap(True)

        self.RLS_Flag1_horizontallLayout.addWidget(self.flag43_label)

        self.flag43_ineEdit = QLineEdit(self.RLS_Frame)
        self.flag43_ineEdit.setObjectName(u"flag43_ineEdit")
        self.flag43_ineEdit.setMinimumSize(QSize(30, 0))
        self.flag43_ineEdit.setMaximumSize(QSize(30, 900))
        self.flag43_ineEdit.setFont(font)
        self.flag43_ineEdit.setFrame(True)
        self.flag43_ineEdit.setAlignment(Qt.AlignCenter)

        self.RLS_Flag1_horizontallLayout.addWidget(self.flag43_ineEdit)


        self.RLS_verticalLayout.addLayout(self.RLS_Flag1_horizontallLayout)

        self.RLS_Flag1_horizontallLayout_3 = QHBoxLayout()
        self.RLS_Flag1_horizontallLayout_3.setSpacing(0)
        self.RLS_Flag1_horizontallLayout_3.setObjectName(u"RLS_Flag1_horizontallLayout_3")
        self.flag44_label = ColorChangingFrame(self.RLS_Frame)
        self.flag44_label.setObjectName(u"flag44_label")
        self.flag44_label.setMinimumSize(QSize(0, 0))
        self.flag44_label.setMaximumSize(QSize(8000, 900))
        self.flag44_label.setFont(font)
        self.flag44_label.setFrameShape(QFrame.Box)
        self.flag44_label.setAlignment(Qt.AlignCenter)
        self.flag44_label.setWordWrap(True)

        self.RLS_Flag1_horizontallLayout_3.addWidget(self.flag44_label)

        self.flag44_lineEdit = QLineEdit(self.RLS_Frame)
        self.flag44_lineEdit.setObjectName(u"flag44_lineEdit")
        self.flag44_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag44_lineEdit.setMaximumSize(QSize(30, 900))
        self.flag44_lineEdit.setFont(font)
        self.flag44_lineEdit.setFrame(True)
        self.flag44_lineEdit.setAlignment(Qt.AlignCenter)

        self.RLS_Flag1_horizontallLayout_3.addWidget(self.flag44_lineEdit)


        self.RLS_verticalLayout.addLayout(self.RLS_Flag1_horizontallLayout_3)


        self.horizontalLayout_6.addLayout(self.RLS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RLS_Frame)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.flag132_label = ColorChangingFrame(self.frame_6)
        self.flag132_label.setObjectName(u"flag132_label")
        self.flag132_label.setEnabled(True)
        self.flag132_label.setMinimumSize(QSize(120, 18))
        self.flag132_label.setMaximumSize(QSize(1550, 18))
        self.flag132_label.setFont(font)
        self.flag132_label.setFrameShape(QFrame.Box)
        self.flag132_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.flag132_label)

        self.stateNumber3_label = ColorChangingFrame(self.frame_6)
        self.stateNumber3_label.setObjectName(u"stateNumber3_label")
        self.stateNumber3_label.setMinimumSize(QSize(120, 18))
        self.stateNumber3_label.setMaximumSize(QSize(1550, 18))
        self.stateNumber3_label.setFont(font)
        self.stateNumber3_label.setFrameShape(QFrame.Box)
        self.stateNumber3_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.stateNumber3_label)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.RHS_Flag1_horizontalLayout = QHBoxLayout()
        self.RHS_Flag1_horizontalLayout.setSpacing(0)
        self.RHS_Flag1_horizontalLayout.setObjectName(u"RHS_Flag1_horizontalLayout")
        self.flag45_label = ColorChangingFrame(self.frame_6)
        self.flag45_label.setObjectName(u"flag45_label")
        self.flag45_label.setFont(font)
        self.flag45_label.setFrameShape(QFrame.Box)
        self.flag45_label.setAlignment(Qt.AlignCenter)
        self.flag45_label.setWordWrap(True)

        self.RHS_Flag1_horizontalLayout.addWidget(self.flag45_label)

        self.flag45_lineEdit = QLineEdit(self.frame_6)
        self.flag45_lineEdit.setObjectName(u"flag45_lineEdit")
        self.flag45_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag45_lineEdit.setMaximumSize(QSize(30, 500))
        self.flag45_lineEdit.setFont(font)
        self.flag45_lineEdit.setAlignment(Qt.AlignCenter)

        self.RHS_Flag1_horizontalLayout.addWidget(self.flag45_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag1_horizontalLayout)

        self.RHS_Flag2_horizontalLayout = QHBoxLayout()
        self.RHS_Flag2_horizontalLayout.setSpacing(0)
        self.RHS_Flag2_horizontalLayout.setObjectName(u"RHS_Flag2_horizontalLayout")
        self.flag46_label = ColorChangingFrame(self.frame_6)
        self.flag46_label.setObjectName(u"flag46_label")
        self.flag46_label.setFont(font)
        self.flag46_label.setFrameShape(QFrame.Box)
        self.flag46_label.setAlignment(Qt.AlignCenter)
        self.flag46_label.setWordWrap(True)

        self.RHS_Flag2_horizontalLayout.addWidget(self.flag46_label)

        self.flag46_lineEdit = QLineEdit(self.frame_6)
        self.flag46_lineEdit.setObjectName(u"flag46_lineEdit")
        self.flag46_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag46_lineEdit.setMaximumSize(QSize(30, 500))
        self.flag46_lineEdit.setFont(font)
        self.flag46_lineEdit.setAlignment(Qt.AlignCenter)

        self.RHS_Flag2_horizontalLayout.addWidget(self.flag46_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag2_horizontalLayout)

        self.RHS_Flag3_horizontalLayout = QHBoxLayout()
        self.RHS_Flag3_horizontalLayout.setSpacing(0)
        self.RHS_Flag3_horizontalLayout.setObjectName(u"RHS_Flag3_horizontalLayout")
        self.flag47_label = ColorChangingFrame(self.frame_6)
        self.flag47_label.setObjectName(u"flag47_label")
        self.flag47_label.setFont(font)
        self.flag47_label.setFrameShape(QFrame.Box)
        self.flag47_label.setAlignment(Qt.AlignCenter)
        self.flag47_label.setWordWrap(True)

        self.RHS_Flag3_horizontalLayout.addWidget(self.flag47_label)

        self.flag48_label = ColorChangingFrame(self.frame_6)
        self.flag48_label.setObjectName(u"flag48_label")
        self.flag48_label.setFont(font)
        self.flag48_label.setFrameShape(QFrame.Box)
        self.flag48_label.setAlignment(Qt.AlignCenter)
        self.flag48_label.setWordWrap(True)

        self.RHS_Flag3_horizontalLayout.addWidget(self.flag48_label)

        self.flag47_and_flag48_lineEdit = QLineEdit(self.frame_6)
        self.flag47_and_flag48_lineEdit.setObjectName(u"flag47_and_flag48_lineEdit")
        self.flag47_and_flag48_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag47_and_flag48_lineEdit.setMaximumSize(QSize(30, 500))
        self.flag47_and_flag48_lineEdit.setFont(font)
        self.flag47_and_flag48_lineEdit.setAlignment(Qt.AlignCenter)

        self.RHS_Flag3_horizontalLayout.addWidget(self.flag47_and_flag48_lineEdit)


        self.verticalLayout_9.addLayout(self.RHS_Flag3_horizontalLayout)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.walikng_horizontalLayout.addWidget(self.frame_6)

        self.LHO2MF_Frame = QFrame(self.frame)
        self.LHO2MF_Frame.setObjectName(u"LHO2MF_Frame")
        self.LHO2MF_Frame.setFrameShape(QFrame.Box)
        self.LHO2MF_Frame.setFrameShadow(QFrame.Plain)
        self.LHO2MF_Frame.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.LHO2MF_Frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.LHO2MF_Flag1_verticalLayout = QVBoxLayout()
        self.LHO2MF_Flag1_verticalLayout.setSpacing(0)
        self.LHO2MF_Flag1_verticalLayout.setObjectName(u"LHO2MF_Flag1_verticalLayout")
        self.flag133_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.flag133_label.setObjectName(u"flag133_label")
        self.flag133_label.setMinimumSize(QSize(120, 18))
        self.flag133_label.setMaximumSize(QSize(1550, 18))
        self.flag133_label.setFont(font)
        self.flag133_label.setFrameShape(QFrame.Box)
        self.flag133_label.setAlignment(Qt.AlignCenter)

        self.LHO2MF_Flag1_verticalLayout.addWidget(self.flag133_label)

        self.stateNumber4_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.stateNumber4_label.setObjectName(u"stateNumber4_label")
        self.stateNumber4_label.setMinimumSize(QSize(120, 18))
        self.stateNumber4_label.setMaximumSize(QSize(1550, 18))
        self.stateNumber4_label.setFont(font)
        self.stateNumber4_label.setFrameShape(QFrame.Box)
        self.stateNumber4_label.setAlignment(Qt.AlignCenter)

        self.LHO2MF_Flag1_verticalLayout.addWidget(self.stateNumber4_label)

        self.LHO2MF_Flag1_horizontalLayout = QHBoxLayout()
        self.LHO2MF_Flag1_horizontalLayout.setSpacing(0)
        self.LHO2MF_Flag1_horizontalLayout.setObjectName(u"LHO2MF_Flag1_horizontalLayout")
        self.flag49_label = ColorChangingFrame(self.LHO2MF_Frame)
        self.flag49_label.setObjectName(u"flag49_label")
        self.flag49_label.setMaximumSize(QSize(8000, 16777215))
        self.flag49_label.setFont(font)
        self.flag49_label.setFrameShape(QFrame.Box)
        self.flag49_label.setAlignment(Qt.AlignCenter)
        self.flag49_label.setWordWrap(True)
        self.flag49_label.setMargin(0)

        self.LHO2MF_Flag1_horizontalLayout.addWidget(self.flag49_label)

        self.flag49_lineEdit = QLineEdit(self.LHO2MF_Frame)
        self.flag49_lineEdit.setObjectName(u"flag49_lineEdit")
        self.flag49_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag49_lineEdit.setMaximumSize(QSize(30, 1500))
        self.flag49_lineEdit.setFont(font)
        self.flag49_lineEdit.setAlignment(Qt.AlignCenter)

        self.LHO2MF_Flag1_horizontalLayout.addWidget(self.flag49_lineEdit)


        self.LHO2MF_Flag1_verticalLayout.addLayout(self.LHO2MF_Flag1_horizontalLayout)


        self.horizontalLayout_17.addLayout(self.LHO2MF_Flag1_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LHO2MF_Frame)

        self.LF2ET_Frame = QFrame(self.frame)
        self.LF2ET_Frame.setObjectName(u"LF2ET_Frame")
        self.LF2ET_Frame.setFrameShape(QFrame.Box)
        self.LF2ET_Frame.setFrameShadow(QFrame.Plain)
        self.LF2ET_Frame.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.LF2ET_Frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.LF2ET_verticalLayout = QVBoxLayout()
        self.LF2ET_verticalLayout.setSpacing(0)
        self.LF2ET_verticalLayout.setObjectName(u"LF2ET_verticalLayout")
        self.flag134_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flag134_label.setObjectName(u"flag134_label")
        self.flag134_label.setMinimumSize(QSize(0, 18))
        self.flag134_label.setMaximumSize(QSize(16777215, 18))
        self.flag134_label.setFont(font)
        self.flag134_label.setFrameShape(QFrame.Box)
        self.flag134_label.setAlignment(Qt.AlignCenter)

        self.LF2ET_verticalLayout.addWidget(self.flag134_label)

        self.stateNumber5_label = ColorChangingFrame(self.LF2ET_Frame)
        self.stateNumber5_label.setObjectName(u"stateNumber5_label")
        self.stateNumber5_label.setMinimumSize(QSize(0, 18))
        self.stateNumber5_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber5_label.setFont(font)
        self.stateNumber5_label.setFrameShape(QFrame.Box)
        self.stateNumber5_label.setAlignment(Qt.AlignCenter)

        self.LF2ET_verticalLayout.addWidget(self.stateNumber5_label)

        self.LF2ET_Flag12_verticalLayout = QVBoxLayout()
        self.LF2ET_Flag12_verticalLayout.setSpacing(0)
        self.LF2ET_Flag12_verticalLayout.setObjectName(u"LF2ET_Flag12_verticalLayout")
        self.LF2ET_Flag1_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag1_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag1_horizontalLayout.setObjectName(u"LF2ET_Flag1_horizontalLayout")
        self.flag50_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flag50_label.setObjectName(u"flag50_label")
        self.flag50_label.setFont(font)
        self.flag50_label.setFrameShape(QFrame.Box)
        self.flag50_label.setAlignment(Qt.AlignCenter)
        self.flag50_label.setWordWrap(True)

        self.LF2ET_Flag1_horizontalLayout.addWidget(self.flag50_label)

        self.flag50_lineEdit = QLineEdit(self.LF2ET_Frame)
        self.flag50_lineEdit.setObjectName(u"flag50_lineEdit")
        self.flag50_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag50_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag50_lineEdit.setFont(font)
        self.flag50_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag50_lineEdit.setReadOnly(True)

        self.LF2ET_Flag1_horizontalLayout.addWidget(self.flag50_lineEdit)


        self.LF2ET_Flag12_verticalLayout.addLayout(self.LF2ET_Flag1_horizontalLayout)

        self.StandingStill_label_23 = ColorChangingFrame(self.LF2ET_Frame)
        self.StandingStill_label_23.setObjectName(u"StandingStill_label_23")
        self.StandingStill_label_23.setFont(font)
        self.StandingStill_label_23.setFrameShape(QFrame.Box)
        self.StandingStill_label_23.setAlignment(Qt.AlignCenter)

        self.LF2ET_Flag12_verticalLayout.addWidget(self.StandingStill_label_23)

        self.LF2ET_Flag2_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag2_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag2_horizontalLayout.setObjectName(u"LF2ET_Flag2_horizontalLayout")
        self.flag51_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flag51_label.setObjectName(u"flag51_label")
        self.flag51_label.setFont(font)
        self.flag51_label.setFrameShape(QFrame.Box)
        self.flag51_label.setAlignment(Qt.AlignCenter)
        self.flag51_label.setWordWrap(True)

        self.LF2ET_Flag2_horizontalLayout.addWidget(self.flag51_label)

        self.flag51_lineEdit = QLineEdit(self.LF2ET_Frame)
        self.flag51_lineEdit.setObjectName(u"flag51_lineEdit")
        self.flag51_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag51_lineEdit.setMaximumSize(QSize(30, 60000))
        self.flag51_lineEdit.setFont(font)
        self.flag51_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag51_lineEdit.setReadOnly(True)

        self.LF2ET_Flag2_horizontalLayout.addWidget(self.flag51_lineEdit)


        self.LF2ET_Flag12_verticalLayout.addLayout(self.LF2ET_Flag2_horizontalLayout)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag12_verticalLayout)

        self.LF2ET_Flag3_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag3_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag3_horizontalLayout.setObjectName(u"LF2ET_Flag3_horizontalLayout")
        self.flag52_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flag52_label.setObjectName(u"flag52_label")
        self.flag52_label.setFont(font)
        self.flag52_label.setFrameShape(QFrame.Box)
        self.flag52_label.setAlignment(Qt.AlignCenter)
        self.flag52_label.setWordWrap(True)

        self.LF2ET_Flag3_horizontalLayout.addWidget(self.flag52_label)

        self.flag52_lineEdit = QLineEdit(self.LF2ET_Frame)
        self.flag52_lineEdit.setObjectName(u"flag52_lineEdit")
        self.flag52_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag52_lineEdit.setMaximumSize(QSize(30, 66000))
        self.flag52_lineEdit.setFont(font)
        self.flag52_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag52_lineEdit.setReadOnly(True)

        self.LF2ET_Flag3_horizontalLayout.addWidget(self.flag52_lineEdit)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag3_horizontalLayout)

        self.LF2ET_Flag4_horizontalLayout = QHBoxLayout()
        self.LF2ET_Flag4_horizontalLayout.setSpacing(0)
        self.LF2ET_Flag4_horizontalLayout.setObjectName(u"LF2ET_Flag4_horizontalLayout")
        self.flag53_label = ColorChangingFrame(self.LF2ET_Frame)
        self.flag53_label.setObjectName(u"flag53_label")
        self.flag53_label.setFont(font)
        self.flag53_label.setFrameShape(QFrame.Box)
        self.flag53_label.setAlignment(Qt.AlignCenter)
        self.flag53_label.setWordWrap(True)

        self.LF2ET_Flag4_horizontalLayout.addWidget(self.flag53_label)

        self.flag53_lineEdit = QLineEdit(self.LF2ET_Frame)
        self.flag53_lineEdit.setObjectName(u"flag53_lineEdit")
        self.flag53_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag53_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag53_lineEdit.setFont(font)
        self.flag53_lineEdit.setAlignment(Qt.AlignCenter)

        self.LF2ET_Flag4_horizontalLayout.addWidget(self.flag53_lineEdit)


        self.LF2ET_verticalLayout.addLayout(self.LF2ET_Flag4_horizontalLayout)


        self.horizontalLayout_16.addLayout(self.LF2ET_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LF2ET_Frame)

        self.Lextension_Frame = QFrame(self.frame)
        self.Lextension_Frame.setObjectName(u"Lextension_Frame")
        self.Lextension_Frame.setFrameShape(QFrame.Box)
        self.Lextension_Frame.setFrameShadow(QFrame.Plain)
        self.Lextension_Frame.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.Lextension_Frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Lextension_verticalLayout = QVBoxLayout()
        self.Lextension_verticalLayout.setSpacing(0)
        self.Lextension_verticalLayout.setObjectName(u"Lextension_verticalLayout")
        self.flag135_label = ColorChangingFrame(self.Lextension_Frame)
        self.flag135_label.setObjectName(u"flag135_label")
        self.flag135_label.setMinimumSize(QSize(0, 18))
        self.flag135_label.setMaximumSize(QSize(16777215, 18))
        self.flag135_label.setFont(font)
        self.flag135_label.setFrameShape(QFrame.Box)
        self.flag135_label.setAlignment(Qt.AlignCenter)

        self.Lextension_verticalLayout.addWidget(self.flag135_label)

        self.stateNumber6_label = ColorChangingFrame(self.Lextension_Frame)
        self.stateNumber6_label.setObjectName(u"stateNumber6_label")
        self.stateNumber6_label.setMinimumSize(QSize(0, 18))
        self.stateNumber6_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber6_label.setFont(font)
        self.stateNumber6_label.setFrameShape(QFrame.Box)
        self.stateNumber6_label.setAlignment(Qt.AlignCenter)

        self.Lextension_verticalLayout.addWidget(self.stateNumber6_label)

        self.Lextension_Flag1_horizontalLayout = QHBoxLayout()
        self.Lextension_Flag1_horizontalLayout.setSpacing(0)
        self.Lextension_Flag1_horizontalLayout.setObjectName(u"Lextension_Flag1_horizontalLayout")
        self.flag54_label = ColorChangingFrame(self.Lextension_Frame)
        self.flag54_label.setObjectName(u"flag54_label")
        self.flag54_label.setMinimumSize(QSize(100, 0))
        self.flag54_label.setMaximumSize(QSize(16777215, 1000))
        self.flag54_label.setFont(font)
        self.flag54_label.setFrameShape(QFrame.Box)
        self.flag54_label.setAlignment(Qt.AlignCenter)
        self.flag54_label.setWordWrap(True)

        self.Lextension_Flag1_horizontalLayout.addWidget(self.flag54_label)

        self.flag54_lineEdit = QLineEdit(self.Lextension_Frame)
        self.flag54_lineEdit.setObjectName(u"flag54_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flag54_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag54_lineEdit.setSizePolicy(sizePolicy)
        self.flag54_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag54_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag54_lineEdit.setFont(font)
        self.flag54_lineEdit.setFrame(True)
        self.flag54_lineEdit.setAlignment(Qt.AlignCenter)

        self.Lextension_Flag1_horizontalLayout.addWidget(self.flag54_lineEdit)


        self.Lextension_verticalLayout.addLayout(self.Lextension_Flag1_horizontalLayout)


        self.horizontalLayout_19.addLayout(self.Lextension_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Lextension_Frame)

        self.Lextended_Frame = QFrame(self.frame)
        self.Lextended_Frame.setObjectName(u"Lextended_Frame")
        self.Lextended_Frame.setFrameShape(QFrame.Box)
        self.Lextended_Frame.setFrameShadow(QFrame.Plain)
        self.Lextended_Frame.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.Lextended_Frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Lextended_verticalLayout = QVBoxLayout()
        self.Lextended_verticalLayout.setSpacing(0)
        self.Lextended_verticalLayout.setObjectName(u"Lextended_verticalLayout")
        self.flag136_label = ColorChangingFrame(self.Lextended_Frame)
        self.flag136_label.setObjectName(u"flag136_label")
        self.flag136_label.setMinimumSize(QSize(0, 18))
        self.flag136_label.setMaximumSize(QSize(16777215, 18))
        self.flag136_label.setFont(font)
        self.flag136_label.setFrameShape(QFrame.Box)
        self.flag136_label.setAlignment(Qt.AlignCenter)

        self.Lextended_verticalLayout.addWidget(self.flag136_label)

        self.stateNumber7_label = ColorChangingFrame(self.Lextended_Frame)
        self.stateNumber7_label.setObjectName(u"stateNumber7_label")
        self.stateNumber7_label.setMinimumSize(QSize(0, 18))
        self.stateNumber7_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber7_label.setFont(font)
        self.stateNumber7_label.setFrameShape(QFrame.Box)
        self.stateNumber7_label.setAlignment(Qt.AlignCenter)

        self.Lextended_verticalLayout.addWidget(self.stateNumber7_label)

        self.Lextended_Flag1_horizontalLayout = QHBoxLayout()
        self.Lextended_Flag1_horizontalLayout.setSpacing(0)
        self.Lextended_Flag1_horizontalLayout.setObjectName(u"Lextended_Flag1_horizontalLayout")
        self.flag55_label = ColorChangingFrame(self.Lextended_Frame)
        self.flag55_label.setObjectName(u"flag55_label")
        self.flag55_label.setMinimumSize(QSize(70, 0))
        self.flag55_label.setMaximumSize(QSize(80, 1000))
        self.flag55_label.setFont(font)
        self.flag55_label.setFrameShape(QFrame.Box)
        self.flag55_label.setAlignment(Qt.AlignCenter)
        self.flag55_label.setWordWrap(True)

        self.Lextended_Flag1_horizontalLayout.addWidget(self.flag55_label)

        self.flag55_lineEdit = QLineEdit(self.Lextended_Frame)
        self.flag55_lineEdit.setObjectName(u"flag55_lineEdit")
        sizePolicy.setHeightForWidth(self.flag55_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag55_lineEdit.setSizePolicy(sizePolicy)
        self.flag55_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag55_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag55_lineEdit.setFont(font)
        self.flag55_lineEdit.setFrame(True)
        self.flag55_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag55_lineEdit.setReadOnly(True)

        self.Lextended_Flag1_horizontalLayout.addWidget(self.flag55_lineEdit)


        self.Lextended_verticalLayout.addLayout(self.Lextended_Flag1_horizontalLayout)


        self.horizontalLayout_21.addLayout(self.Lextended_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Lextended_Frame)

        self.LLS_Frame = QFrame(self.frame)
        self.LLS_Frame.setObjectName(u"LLS_Frame")
        self.LLS_Frame.setFrameShape(QFrame.NoFrame)
        self.LLS_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.LLS_Frame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LLS_verticalLayout = QVBoxLayout()
        self.LLS_verticalLayout.setSpacing(0)
        self.LLS_verticalLayout.setObjectName(u"LLS_verticalLayout")
        self.flag137_label = ColorChangingFrame(self.LLS_Frame)
        self.flag137_label.setObjectName(u"flag137_label")
        self.flag137_label.setMinimumSize(QSize(0, 18))
        self.flag137_label.setMaximumSize(QSize(16777215, 18))
        self.flag137_label.setFont(font)
        self.flag137_label.setFrameShape(QFrame.Box)
        self.flag137_label.setAlignment(Qt.AlignCenter)

        self.LLS_verticalLayout.addWidget(self.flag137_label)

        self.stateNumber8_label = ColorChangingFrame(self.LLS_Frame)
        self.stateNumber8_label.setObjectName(u"stateNumber8_label")
        self.stateNumber8_label.setMinimumSize(QSize(0, 18))
        self.stateNumber8_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber8_label.setFont(font)
        self.stateNumber8_label.setFrameShape(QFrame.Box)
        self.stateNumber8_label.setAlignment(Qt.AlignCenter)

        self.LLS_verticalLayout.addWidget(self.stateNumber8_label)

        self.LLS_Flag1_horizontalLayout = QHBoxLayout()
        self.LLS_Flag1_horizontalLayout.setSpacing(0)
        self.LLS_Flag1_horizontalLayout.setObjectName(u"LLS_Flag1_horizontalLayout")
        self.flag56_label = ColorChangingFrame(self.LLS_Frame)
        self.flag56_label.setObjectName(u"flag56_label")
        self.flag56_label.setMinimumSize(QSize(0, 0))
        self.flag56_label.setMaximumSize(QSize(16777215, 1000))
        self.flag56_label.setFont(font)
        self.flag56_label.setFrameShape(QFrame.Box)
        self.flag56_label.setAlignment(Qt.AlignCenter)
        self.flag56_label.setWordWrap(True)

        self.LLS_Flag1_horizontalLayout.addWidget(self.flag56_label)

        self.flag56_lineEdit = QLineEdit(self.LLS_Frame)
        self.flag56_lineEdit.setObjectName(u"flag56_lineEdit")
        sizePolicy.setHeightForWidth(self.flag56_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag56_lineEdit.setSizePolicy(sizePolicy)
        self.flag56_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag56_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag56_lineEdit.setFont(font)
        self.flag56_lineEdit.setFrame(True)
        self.flag56_lineEdit.setAlignment(Qt.AlignCenter)

        self.LLS_Flag1_horizontalLayout.addWidget(self.flag56_lineEdit)


        self.LLS_verticalLayout.addLayout(self.LLS_Flag1_horizontalLayout)


        self.horizontalLayout_23.addLayout(self.LLS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LLS_Frame)

        self.LHS_Frame = QFrame(self.frame)
        self.LHS_Frame.setObjectName(u"LHS_Frame")
        self.LHS_Frame.setFrameShape(QFrame.NoFrame)
        self.LHS_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_28 = QHBoxLayout(self.LHS_Frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.LHS_verticalLayout = QVBoxLayout()
        self.LHS_verticalLayout.setSpacing(0)
        self.LHS_verticalLayout.setObjectName(u"LHS_verticalLayout")
        self.flag138_label = ColorChangingFrame(self.LHS_Frame)
        self.flag138_label.setObjectName(u"flag138_label")
        self.flag138_label.setMinimumSize(QSize(0, 18))
        self.flag138_label.setMaximumSize(QSize(16777215, 18))
        self.flag138_label.setFont(font)
        self.flag138_label.setFrameShape(QFrame.Box)
        self.flag138_label.setAlignment(Qt.AlignCenter)
        self.flag138_label.setWordWrap(True)

        self.LHS_verticalLayout.addWidget(self.flag138_label)

        self.stateNumber9_label = ColorChangingFrame(self.LHS_Frame)
        self.stateNumber9_label.setObjectName(u"stateNumber9_label")
        self.stateNumber9_label.setMinimumSize(QSize(0, 18))
        self.stateNumber9_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber9_label.setFont(font)
        self.stateNumber9_label.setFrameShape(QFrame.Box)
        self.stateNumber9_label.setAlignment(Qt.AlignCenter)
        self.stateNumber9_label.setWordWrap(True)

        self.LHS_verticalLayout.addWidget(self.stateNumber9_label)

        self.LHS_SubverticalLayout = QVBoxLayout()
        self.LHS_SubverticalLayout.setSpacing(0)
        self.LHS_SubverticalLayout.setObjectName(u"LHS_SubverticalLayout")
        self.LHS_Flag1_horizontalLayout = QHBoxLayout()
        self.LHS_Flag1_horizontalLayout.setSpacing(0)
        self.LHS_Flag1_horizontalLayout.setObjectName(u"LHS_Flag1_horizontalLayout")
        self.flag57_label = ColorChangingFrame(self.LHS_Frame)
        self.flag57_label.setObjectName(u"flag57_label")
        self.flag57_label.setMinimumSize(QSize(0, 0))
        self.flag57_label.setMaximumSize(QSize(16777215, 5000))
        self.flag57_label.setFont(font)
        self.flag57_label.setFrameShape(QFrame.Box)
        self.flag57_label.setAlignment(Qt.AlignCenter)
        self.flag57_label.setWordWrap(True)

        self.LHS_Flag1_horizontalLayout.addWidget(self.flag57_label)

        self.flag57_lineEdit = QLineEdit(self.LHS_Frame)
        self.flag57_lineEdit.setObjectName(u"flag57_lineEdit")
        sizePolicy.setHeightForWidth(self.flag57_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag57_lineEdit.setSizePolicy(sizePolicy)
        self.flag57_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag57_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag57_lineEdit.setFont(font)
        self.flag57_lineEdit.setFrame(True)
        self.flag57_lineEdit.setAlignment(Qt.AlignCenter)

        self.LHS_Flag1_horizontalLayout.addWidget(self.flag57_lineEdit)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag1_horizontalLayout)

        self.LHS_Flag2_horizontalLayout = QHBoxLayout()
        self.LHS_Flag2_horizontalLayout.setSpacing(0)
        self.LHS_Flag2_horizontalLayout.setObjectName(u"LHS_Flag2_horizontalLayout")
        self.flag58_label = ColorChangingFrame(self.LHS_Frame)
        self.flag58_label.setObjectName(u"flag58_label")
        self.flag58_label.setMinimumSize(QSize(0, 0))
        self.flag58_label.setMaximumSize(QSize(16777215, 5000))
        self.flag58_label.setFont(font)
        self.flag58_label.setFrameShape(QFrame.Box)
        self.flag58_label.setAlignment(Qt.AlignCenter)
        self.flag58_label.setWordWrap(True)

        self.LHS_Flag2_horizontalLayout.addWidget(self.flag58_label)

        self.flag58_lineEdit = QLineEdit(self.LHS_Frame)
        self.flag58_lineEdit.setObjectName(u"flag58_lineEdit")
        sizePolicy.setHeightForWidth(self.flag58_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag58_lineEdit.setSizePolicy(sizePolicy)
        self.flag58_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag58_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag58_lineEdit.setFont(font)
        self.flag58_lineEdit.setFrame(True)
        self.flag58_lineEdit.setAlignment(Qt.AlignCenter)

        self.LHS_Flag2_horizontalLayout.addWidget(self.flag58_lineEdit)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag2_horizontalLayout)

        self.LHS_Flag3_horizontalLayout = QHBoxLayout()
        self.LHS_Flag3_horizontalLayout.setSpacing(0)
        self.LHS_Flag3_horizontalLayout.setObjectName(u"LHS_Flag3_horizontalLayout")
        self.flag59_label = ColorChangingFrame(self.LHS_Frame)
        self.flag59_label.setObjectName(u"flag59_label")
        self.flag59_label.setMinimumSize(QSize(0, 0))
        self.flag59_label.setMaximumSize(QSize(16777215, 5000))
        self.flag59_label.setFont(font)
        self.flag59_label.setFrameShape(QFrame.Box)
        self.flag59_label.setAlignment(Qt.AlignCenter)
        self.flag59_label.setWordWrap(True)

        self.LHS_Flag3_horizontalLayout.addWidget(self.flag59_label)

        self.flag60_label = ColorChangingFrame(self.LHS_Frame)
        self.flag60_label.setObjectName(u"flag60_label")
        self.flag60_label.setMinimumSize(QSize(0, 0))
        self.flag60_label.setMaximumSize(QSize(16777215, 5000))
        self.flag60_label.setFont(font)
        self.flag60_label.setFrameShape(QFrame.Box)
        self.flag60_label.setAlignment(Qt.AlignCenter)
        self.flag60_label.setWordWrap(True)

        self.LHS_Flag3_horizontalLayout.addWidget(self.flag60_label)

        self.flag59_and_flag60_lineEdit = QLineEdit(self.LHS_Frame)
        self.flag59_and_flag60_lineEdit.setObjectName(u"flag59_and_flag60_lineEdit")
        sizePolicy.setHeightForWidth(self.flag59_and_flag60_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag59_and_flag60_lineEdit.setSizePolicy(sizePolicy)
        self.flag59_and_flag60_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag59_and_flag60_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag59_and_flag60_lineEdit.setFont(font)
        self.flag59_and_flag60_lineEdit.setFrame(True)
        self.flag59_and_flag60_lineEdit.setAlignment(Qt.AlignCenter)

        self.LHS_Flag3_horizontalLayout.addWidget(self.flag59_and_flag60_lineEdit)


        self.LHS_SubverticalLayout.addLayout(self.LHS_Flag3_horizontalLayout)


        self.LHS_verticalLayout.addLayout(self.LHS_SubverticalLayout)


        self.horizontalLayout_28.addLayout(self.LHS_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.LHS_Frame)

        self.RHO2MF_Frame = QFrame(self.frame)
        self.RHO2MF_Frame.setObjectName(u"RHO2MF_Frame")
        self.RHO2MF_Frame.setFrameShape(QFrame.NoFrame)
        self.RHO2MF_Frame.setFrameShadow(QFrame.Plain)
        self.RHO2MF_Frame.setLineWidth(0)
        self.horizontalLayout_33 = QHBoxLayout(self.RHO2MF_Frame)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.RHO2MF_verticalLayout = QVBoxLayout()
        self.RHO2MF_verticalLayout.setSpacing(0)
        self.RHO2MF_verticalLayout.setObjectName(u"RHO2MF_verticalLayout")
        self.flag139_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.flag139_label.setObjectName(u"flag139_label")
        self.flag139_label.setMinimumSize(QSize(0, 18))
        self.flag139_label.setMaximumSize(QSize(16777215, 18))
        self.flag139_label.setFont(font)
        self.flag139_label.setFrameShape(QFrame.Box)
        self.flag139_label.setAlignment(Qt.AlignCenter)

        self.RHO2MF_verticalLayout.addWidget(self.flag139_label)

        self.stateNumber10_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.stateNumber10_label.setObjectName(u"stateNumber10_label")
        self.stateNumber10_label.setMinimumSize(QSize(0, 18))
        self.stateNumber10_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber10_label.setFont(font)
        self.stateNumber10_label.setFrameShape(QFrame.Box)
        self.stateNumber10_label.setAlignment(Qt.AlignCenter)

        self.RHO2MF_verticalLayout.addWidget(self.stateNumber10_label)

        self.RHO2MF_Flag1_horizontalLayout = QHBoxLayout()
        self.RHO2MF_Flag1_horizontalLayout.setSpacing(0)
        self.RHO2MF_Flag1_horizontalLayout.setObjectName(u"RHO2MF_Flag1_horizontalLayout")
        self.flag61_label = ColorChangingFrame(self.RHO2MF_Frame)
        self.flag61_label.setObjectName(u"flag61_label")
        self.flag61_label.setMinimumSize(QSize(0, 0))
        self.flag61_label.setMaximumSize(QSize(16777215, 1000))
        self.flag61_label.setFont(font)
        self.flag61_label.setFrameShape(QFrame.Box)
        self.flag61_label.setAlignment(Qt.AlignCenter)
        self.flag61_label.setWordWrap(True)

        self.RHO2MF_Flag1_horizontalLayout.addWidget(self.flag61_label)

        self.flag61_lineEdit = QLineEdit(self.RHO2MF_Frame)
        self.flag61_lineEdit.setObjectName(u"flag61_lineEdit")
        sizePolicy.setHeightForWidth(self.flag61_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag61_lineEdit.setSizePolicy(sizePolicy)
        self.flag61_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag61_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag61_lineEdit.setFont(font)
        self.flag61_lineEdit.setFrame(True)
        self.flag61_lineEdit.setAlignment(Qt.AlignCenter)

        self.RHO2MF_Flag1_horizontalLayout.addWidget(self.flag61_lineEdit)


        self.RHO2MF_verticalLayout.addLayout(self.RHO2MF_Flag1_horizontalLayout)


        self.horizontalLayout_33.addLayout(self.RHO2MF_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RHO2MF_Frame)

        self.RF2ET_Frame = QFrame(self.frame)
        self.RF2ET_Frame.setObjectName(u"RF2ET_Frame")
        self.RF2ET_Frame.setFrameShape(QFrame.NoFrame)
        self.RF2ET_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_35 = QHBoxLayout(self.RF2ET_Frame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.RF2ET_verticalLayout = QVBoxLayout()
        self.RF2ET_verticalLayout.setSpacing(0)
        self.RF2ET_verticalLayout.setObjectName(u"RF2ET_verticalLayout")
        self.flag140_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flag140_label.setObjectName(u"flag140_label")
        self.flag140_label.setMinimumSize(QSize(0, 18))
        self.flag140_label.setMaximumSize(QSize(16777215, 18))
        self.flag140_label.setFont(font)
        self.flag140_label.setFrameShape(QFrame.Box)
        self.flag140_label.setAlignment(Qt.AlignCenter)

        self.RF2ET_verticalLayout.addWidget(self.flag140_label)

        self.stateNumber11_label = ColorChangingFrame(self.RF2ET_Frame)
        self.stateNumber11_label.setObjectName(u"stateNumber11_label")
        self.stateNumber11_label.setMinimumSize(QSize(0, 18))
        self.stateNumber11_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber11_label.setFont(font)
        self.stateNumber11_label.setFrameShape(QFrame.Box)
        self.stateNumber11_label.setAlignment(Qt.AlignCenter)

        self.RF2ET_verticalLayout.addWidget(self.stateNumber11_label)

        self.RF2ET_Flag12_verticalLayout = QVBoxLayout()
        self.RF2ET_Flag12_verticalLayout.setSpacing(0)
        self.RF2ET_Flag12_verticalLayout.setObjectName(u"RF2ET_Flag12_verticalLayout")
        self.RF2ET_Flag1_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag1_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag1_horizontalLayout.setObjectName(u"RF2ET_Flag1_horizontalLayout")
        self.flag62_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flag62_label.setObjectName(u"flag62_label")
        self.flag62_label.setFont(font)
        self.flag62_label.setFrameShape(QFrame.Box)
        self.flag62_label.setAlignment(Qt.AlignCenter)
        self.flag62_label.setWordWrap(True)

        self.RF2ET_Flag1_horizontalLayout.addWidget(self.flag62_label)

        self.flag62_lineEdit = QLineEdit(self.RF2ET_Frame)
        self.flag62_lineEdit.setObjectName(u"flag62_lineEdit")
        self.flag62_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag62_lineEdit.setMaximumSize(QSize(30, 60000))
        self.flag62_lineEdit.setFont(font)
        self.flag62_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag62_lineEdit.setReadOnly(True)

        self.RF2ET_Flag1_horizontalLayout.addWidget(self.flag62_lineEdit)


        self.RF2ET_Flag12_verticalLayout.addLayout(self.RF2ET_Flag1_horizontalLayout)

        self.StandingStill_label_35 = ColorChangingFrame(self.RF2ET_Frame)
        self.StandingStill_label_35.setObjectName(u"StandingStill_label_35")
        self.StandingStill_label_35.setFont(font)
        self.StandingStill_label_35.setFrameShape(QFrame.Box)
        self.StandingStill_label_35.setAlignment(Qt.AlignCenter)

        self.RF2ET_Flag12_verticalLayout.addWidget(self.StandingStill_label_35)

        self.RF2ET_Flag2_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag2_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag2_horizontalLayout.setObjectName(u"RF2ET_Flag2_horizontalLayout")
        self.flag63_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flag63_label.setObjectName(u"flag63_label")
        self.flag63_label.setFont(font)
        self.flag63_label.setFrameShape(QFrame.Box)
        self.flag63_label.setAlignment(Qt.AlignCenter)
        self.flag63_label.setWordWrap(True)

        self.RF2ET_Flag2_horizontalLayout.addWidget(self.flag63_label)

        self.flag63_lineEdit = QLineEdit(self.RF2ET_Frame)
        self.flag63_lineEdit.setObjectName(u"flag63_lineEdit")
        self.flag63_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag63_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag63_lineEdit.setFont(font)
        self.flag63_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag63_lineEdit.setReadOnly(True)

        self.RF2ET_Flag2_horizontalLayout.addWidget(self.flag63_lineEdit)


        self.RF2ET_Flag12_verticalLayout.addLayout(self.RF2ET_Flag2_horizontalLayout)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag12_verticalLayout)

        self.RF2ET_Flag3_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag3_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag3_horizontalLayout.setObjectName(u"RF2ET_Flag3_horizontalLayout")
        self.flag64_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flag64_label.setObjectName(u"flag64_label")
        self.flag64_label.setFont(font)
        self.flag64_label.setFrameShape(QFrame.Box)
        self.flag64_label.setAlignment(Qt.AlignCenter)
        self.flag64_label.setWordWrap(True)

        self.RF2ET_Flag3_horizontalLayout.addWidget(self.flag64_label)

        self.flag64_lineEdit = QLineEdit(self.RF2ET_Frame)
        self.flag64_lineEdit.setObjectName(u"flag64_lineEdit")
        self.flag64_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag64_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag64_lineEdit.setFont(font)
        self.flag64_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag64_lineEdit.setReadOnly(True)

        self.RF2ET_Flag3_horizontalLayout.addWidget(self.flag64_lineEdit)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag3_horizontalLayout)

        self.RF2ET_Flag4_horizontalLayout = QHBoxLayout()
        self.RF2ET_Flag4_horizontalLayout.setSpacing(0)
        self.RF2ET_Flag4_horizontalLayout.setObjectName(u"RF2ET_Flag4_horizontalLayout")
        self.flag65_label = ColorChangingFrame(self.RF2ET_Frame)
        self.flag65_label.setObjectName(u"flag65_label")
        self.flag65_label.setFont(font)
        self.flag65_label.setFrameShape(QFrame.Box)
        self.flag65_label.setAlignment(Qt.AlignCenter)
        self.flag65_label.setWordWrap(True)

        self.RF2ET_Flag4_horizontalLayout.addWidget(self.flag65_label)

        self.flag65_lineEdit = QLineEdit(self.RF2ET_Frame)
        self.flag65_lineEdit.setObjectName(u"flag65_lineEdit")
        self.flag65_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag65_lineEdit.setMaximumSize(QSize(30, 6000))
        self.flag65_lineEdit.setFont(font)
        self.flag65_lineEdit.setAlignment(Qt.AlignCenter)

        self.RF2ET_Flag4_horizontalLayout.addWidget(self.flag65_lineEdit)


        self.RF2ET_verticalLayout.addLayout(self.RF2ET_Flag4_horizontalLayout)


        self.horizontalLayout_35.addLayout(self.RF2ET_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.RF2ET_Frame)

        self.Rextension_Frame = QFrame(self.frame)
        self.Rextension_Frame.setObjectName(u"Rextension_Frame")
        self.Rextension_Frame.setFrameShape(QFrame.NoFrame)
        self.Rextension_Frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_40 = QHBoxLayout(self.Rextension_Frame)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Rextension_verticalLayout = QVBoxLayout()
        self.Rextension_verticalLayout.setSpacing(0)
        self.Rextension_verticalLayout.setObjectName(u"Rextension_verticalLayout")
        self.flag141_label = ColorChangingFrame(self.Rextension_Frame)
        self.flag141_label.setObjectName(u"flag141_label")
        self.flag141_label.setMinimumSize(QSize(0, 18))
        self.flag141_label.setMaximumSize(QSize(16777215, 18))
        self.flag141_label.setFont(font)
        self.flag141_label.setFrameShape(QFrame.Box)
        self.flag141_label.setAlignment(Qt.AlignCenter)

        self.Rextension_verticalLayout.addWidget(self.flag141_label)

        self.stateNumber12_label = ColorChangingFrame(self.Rextension_Frame)
        self.stateNumber12_label.setObjectName(u"stateNumber12_label")
        self.stateNumber12_label.setMinimumSize(QSize(0, 18))
        self.stateNumber12_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber12_label.setFont(font)
        self.stateNumber12_label.setFrameShape(QFrame.Box)
        self.stateNumber12_label.setAlignment(Qt.AlignCenter)

        self.Rextension_verticalLayout.addWidget(self.stateNumber12_label)

        self.Rextension_horizontalLayout = QHBoxLayout()
        self.Rextension_horizontalLayout.setSpacing(0)
        self.Rextension_horizontalLayout.setObjectName(u"Rextension_horizontalLayout")
        self.flag66_label = ColorChangingFrame(self.Rextension_Frame)
        self.flag66_label.setObjectName(u"flag66_label")
        self.flag66_label.setMinimumSize(QSize(0, 0))
        self.flag66_label.setMaximumSize(QSize(16777215, 1000))
        self.flag66_label.setFont(font)
        self.flag66_label.setFrameShape(QFrame.Box)
        self.flag66_label.setAlignment(Qt.AlignCenter)
        self.flag66_label.setWordWrap(True)

        self.Rextension_horizontalLayout.addWidget(self.flag66_label)

        self.flag66_lineEdit = QLineEdit(self.Rextension_Frame)
        self.flag66_lineEdit.setObjectName(u"flag66_lineEdit")
        sizePolicy.setHeightForWidth(self.flag66_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag66_lineEdit.setSizePolicy(sizePolicy)
        self.flag66_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag66_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag66_lineEdit.setFont(font)
        self.flag66_lineEdit.setFrame(True)
        self.flag66_lineEdit.setAlignment(Qt.AlignCenter)

        self.Rextension_horizontalLayout.addWidget(self.flag66_lineEdit)


        self.Rextension_verticalLayout.addLayout(self.Rextension_horizontalLayout)


        self.horizontalLayout_40.addLayout(self.Rextension_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Rextension_Frame)

        self.Rextended_Frame = QFrame(self.frame)
        self.Rextended_Frame.setObjectName(u"Rextended_Frame")
        self.Rextended_Frame.setFrameShape(QFrame.Box)
        self.Rextended_Frame.setFrameShadow(QFrame.Plain)
        self.Rextended_Frame.setLineWidth(0)
        self.horizontalLayout_42 = QHBoxLayout(self.Rextended_Frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Rextended_verticalLayout = QVBoxLayout()
        self.Rextended_verticalLayout.setSpacing(0)
        self.Rextended_verticalLayout.setObjectName(u"Rextended_verticalLayout")
        self.flag142_label = ColorChangingFrame(self.Rextended_Frame)
        self.flag142_label.setObjectName(u"flag142_label")
        self.flag142_label.setMinimumSize(QSize(0, 18))
        self.flag142_label.setMaximumSize(QSize(16777215, 18))
        self.flag142_label.setFont(font)
        self.flag142_label.setFrameShape(QFrame.Box)
        self.flag142_label.setAlignment(Qt.AlignCenter)

        self.Rextended_verticalLayout.addWidget(self.flag142_label)

        self.stateNumber13_label = ColorChangingFrame(self.Rextended_Frame)
        self.stateNumber13_label.setObjectName(u"stateNumber13_label")
        self.stateNumber13_label.setMinimumSize(QSize(0, 18))
        self.stateNumber13_label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber13_label.setFont(font)
        self.stateNumber13_label.setFrameShape(QFrame.Box)
        self.stateNumber13_label.setAlignment(Qt.AlignCenter)

        self.Rextended_verticalLayout.addWidget(self.stateNumber13_label)

        self.Rextended_Flag1_horizontalLayout = QHBoxLayout()
        self.Rextended_Flag1_horizontalLayout.setSpacing(0)
        self.Rextended_Flag1_horizontalLayout.setObjectName(u"Rextended_Flag1_horizontalLayout")
        self.flag67_label = ColorChangingFrame(self.Rextended_Frame)
        self.flag67_label.setObjectName(u"flag67_label")
        self.flag67_label.setMinimumSize(QSize(0, 0))
        self.flag67_label.setMaximumSize(QSize(16777215, 1000))
        self.flag67_label.setFont(font)
        self.flag67_label.setFrameShape(QFrame.Box)
        self.flag67_label.setAlignment(Qt.AlignCenter)
        self.flag67_label.setWordWrap(True)

        self.Rextended_Flag1_horizontalLayout.addWidget(self.flag67_label)

        self.flag67_lineEdit = QLineEdit(self.Rextended_Frame)
        self.flag67_lineEdit.setObjectName(u"flag67_lineEdit")
        sizePolicy.setHeightForWidth(self.flag67_lineEdit.sizePolicy().hasHeightForWidth())
        self.flag67_lineEdit.setSizePolicy(sizePolicy)
        self.flag67_lineEdit.setMinimumSize(QSize(30, 0))
        self.flag67_lineEdit.setMaximumSize(QSize(30, 16777215))
        self.flag67_lineEdit.setFont(font)
        self.flag67_lineEdit.setFrame(True)
        self.flag67_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag67_lineEdit.setReadOnly(True)

        self.Rextended_Flag1_horizontalLayout.addWidget(self.flag67_lineEdit)


        self.Rextended_verticalLayout.addLayout(self.Rextended_Flag1_horizontalLayout)


        self.horizontalLayout_42.addLayout(self.Rextended_verticalLayout)


        self.walikng_horizontalLayout.addWidget(self.Rextended_Frame)


        self.walking_verticalLayout.addLayout(self.walikng_horizontalLayout)


        self.horizontalLayout.addLayout(self.walking_verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_17.addWidget(self.frame)

        self.Stand2SitandSit2StandandSquatTasks_frame = QFrame(self.Main_widget)
        self.Stand2SitandSit2StandandSquatTasks_frame.setObjectName(u"Stand2SitandSit2StandandSquatTasks_frame")
        self.Stand2SitandSit2StandandSquatTasks_frame.setFrameShape(QFrame.StyledPanel)
        self.Stand2SitandSit2StandandSquatTasks_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.flag113_label = ColorChangingFrame(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.flag113_label.setObjectName(u"flag113_label")
        self.flag113_label.setMaximumSize(QSize(16777215, 18))
        self.flag113_label.setFont(font)
        self.flag113_label.setFrameShape(QFrame.Box)
        self.flag113_label.setAlignment(Qt.AlignCenter)
        self.flag113_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.flag113_label)

        self.Stand2SitandSit2StandandSquatTasks_subframe = QFrame(self.Stand2SitandSit2StandandSquatTasks_frame)
        self.Stand2SitandSit2StandandSquatTasks_subframe.setObjectName(u"Stand2SitandSit2StandandSquatTasks_subframe")
        self.Stand2SitandSit2StandandSquatTasks_subframe.setFrameShape(QFrame.StyledPanel)
        self.Stand2SitandSit2StandandSquatTasks_subframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Stopsd_or_Stopsq_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.Stopsd_or_Stopsq_Frame.setObjectName(u"Stopsd_or_Stopsq_Frame")
        self.Stopsd_or_Stopsq_Frame.setFrameShape(QFrame.StyledPanel)
        self.Stopsd_or_Stopsq_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Stopsd_or_Stopsq_Frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Stopsd_or_Stopsq_Label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.Stopsd_or_Stopsq_Label.setObjectName(u"Stopsd_or_Stopsq_Label")
        self.Stopsd_or_Stopsq_Label.setMaximumSize(QSize(16777215, 18))
        self.Stopsd_or_Stopsq_Label.setFont(font)
        self.Stopsd_or_Stopsq_Label.setFrameShape(QFrame.Box)
        self.Stopsd_or_Stopsq_Label.setAlignment(Qt.AlignCenter)
        self.Stopsd_or_Stopsq_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.Stopsd_or_Stopsq_Label)

        self.flag143_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag143_label.setObjectName(u"flag143_label")
        self.flag143_label.setMaximumSize(QSize(16777215, 18))
        self.flag143_label.setFont(font)
        self.flag143_label.setFrameShape(QFrame.Box)
        self.flag143_label.setAlignment(Qt.AlignCenter)
        self.flag143_label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.flag143_label)

        self.sd_stateNumber0_Label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.sd_stateNumber0_Label.setObjectName(u"sd_stateNumber0_Label")
        self.sd_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.sd_stateNumber0_Label.setFont(font)
        self.sd_stateNumber0_Label.setFrameShape(QFrame.Box)
        self.sd_stateNumber0_Label.setAlignment(Qt.AlignCenter)
        self.sd_stateNumber0_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.sd_stateNumber0_Label)

        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag1and2_horizontalLayout")
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag1and2_verticalLayout")
        self.flag105_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag105_label.setObjectName(u"flag105_label")
        self.flag105_label.setFont(font)
        self.flag105_label.setFrameShape(QFrame.Box)
        self.flag105_label.setAlignment(Qt.AlignCenter)
        self.flag105_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.addWidget(self.flag105_label)

        self.flag106_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag106_label.setObjectName(u"flag106_label")
        self.flag106_label.setFont(font)
        self.flag106_label.setFrameShape(QFrame.Box)
        self.flag106_label.setAlignment(Qt.AlignCenter)
        self.flag106_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag1and2_verticalLayout.addWidget(self.flag106_label)


        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.addLayout(self.Stopsd_or_Stopsq_Flag1and2_verticalLayout)

        self.flag105_and_flag106_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flag105_and_flag106_lineEdit.setObjectName(u"flag105_and_flag106_lineEdit")
        self.flag105_and_flag106_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag105_and_flag106_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag105_and_flag106_lineEdit.setFont(font)
        self.flag105_and_flag106_lineEdit.setFrame(True)
        self.flag105_and_flag106_lineEdit.setAlignment(Qt.AlignCenter)

        self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout.addWidget(self.flag105_and_flag106_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag1and2_horizontalLayout)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag31_horizontalLayout")
        self.flag107_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag107_label.setObjectName(u"flag107_label")
        self.flag107_label.setFont(font)
        self.flag107_label.setFrameShape(QFrame.Box)
        self.flag107_label.setAlignment(Qt.AlignCenter)
        self.flag107_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.addWidget(self.flag107_label)

        self.flag107_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flag107_lineEdit.setObjectName(u"flag107_lineEdit")
        self.flag107_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag107_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag107_lineEdit.setFont(font)
        self.flag107_lineEdit.setFrame(True)
        self.flag107_lineEdit.setAlignment(Qt.AlignCenter)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout.addWidget(self.flag107_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag31_horizontalLayout)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.setObjectName(u"Stopsd_or_Stopsq_Flag32and33_horizontalLayout")
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.setSpacing(0)
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.setObjectName(u"Stopsd_or_Stopsq_Flage32and33_verticalLayout")
        self.flag108_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag108_label.setObjectName(u"flag108_label")
        self.flag108_label.setFont(font)
        self.flag108_label.setFrameShape(QFrame.Box)
        self.flag108_label.setAlignment(Qt.AlignCenter)
        self.flag108_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.addWidget(self.flag108_label)

        self.flag109_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame)
        self.flag109_label.setObjectName(u"flag109_label")
        self.flag109_label.setFont(font)
        self.flag109_label.setFrameShape(QFrame.Box)
        self.flag109_label.setAlignment(Qt.AlignCenter)
        self.flag109_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout.addWidget(self.flag109_label)


        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.addLayout(self.Stopsd_or_Stopsq_Flage32and33_verticalLayout)

        self.flag108_and_flag109_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame)
        self.flag108_and_flag109_lineEdit.setObjectName(u"flag108_and_flag109_lineEdit")
        self.flag108_and_flag109_lineEdit.setMinimumSize(QSize(30, 25))
        self.flag108_and_flag109_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag108_and_flag109_lineEdit.setFont(font)
        self.flag108_and_flag109_lineEdit.setFrame(True)
        self.flag108_and_flag109_lineEdit.setAlignment(Qt.AlignCenter)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout.addWidget(self.flag108_and_flag109_lineEdit)


        self.verticalLayout_7.addLayout(self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.Stopsd_or_Stopsq_Frame)

        self.ss2sd_or_ss2sq_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.ss2sd_or_ss2sq_Frame.setObjectName(u"ss2sd_or_ss2sq_Frame")
        self.ss2sd_or_ss2sq_Frame.setFrameShape(QFrame.StyledPanel)
        self.ss2sd_or_ss2sq_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ss2sd_or_ss2sq_Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ss2sd_Label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.ss2sd_Label.setObjectName(u"ss2sd_Label")
        self.ss2sd_Label.setMaximumSize(QSize(16777215, 18))
        self.ss2sd_Label.setFont(font)
        self.ss2sd_Label.setFrameShape(QFrame.Box)
        self.ss2sd_Label.setAlignment(Qt.AlignCenter)
        self.ss2sd_Label.setWordWrap(True)

        self.verticalLayout.addWidget(self.ss2sd_Label)

        self.flag122_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag122_label.setObjectName(u"flag122_label")
        self.flag122_label.setMaximumSize(QSize(16777215, 18))
        self.flag122_label.setFont(font)
        self.flag122_label.setFrameShape(QFrame.Box)
        self.flag122_label.setAlignment(Qt.AlignCenter)
        self.flag122_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flag122_label)

        self.stateNumber4_or_10_Label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.stateNumber4_or_10_Label.setObjectName(u"stateNumber4_or_10_Label")
        self.stateNumber4_or_10_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber4_or_10_Label.setFont(font)
        self.stateNumber4_or_10_Label.setFrameShape(QFrame.Box)
        self.stateNumber4_or_10_Label.setAlignment(Qt.AlignCenter)
        self.stateNumber4_or_10_Label.setWordWrap(True)

        self.verticalLayout.addWidget(self.stateNumber4_or_10_Label)

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag1_horizontalLayout")
        self.flag72_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag72_label.setObjectName(u"flag72_label")
        self.flag72_label.setFont(font)
        self.flag72_label.setFrameShape(QFrame.Box)
        self.flag72_label.setAlignment(Qt.AlignCenter)
        self.flag72_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.addWidget(self.flag72_label)

        self.flag72_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag72_lineEdit.setObjectName(u"flag72_lineEdit")
        self.flag72_lineEdit.setMinimumSize(QSize(20, 30))
        self.flag72_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag72_lineEdit.setFont(font)
        self.flag72_lineEdit.setFrame(True)
        self.flag72_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag1_horizontalLayout.addWidget(self.flag72_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag1_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag2and3_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag2and3_verticalLayout")
        self.flag73_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag73_label.setObjectName(u"flag73_label")
        self.flag73_label.setFont(font)
        self.flag73_label.setFrameShape(QFrame.Box)
        self.flag73_label.setAlignment(Qt.AlignCenter)
        self.flag73_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.addWidget(self.flag73_label)

        self.flag74_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag74_label.setObjectName(u"flag74_label")
        self.flag74_label.setFont(font)
        self.flag74_label.setFrameShape(QFrame.Box)
        self.flag74_label.setAlignment(Qt.AlignCenter)
        self.flag74_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag2and3_verticalLayout.addWidget(self.flag74_label)


        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag2and3_verticalLayout)

        self.flag73_and_flag74_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag73_and_flag74_lineEdit.setObjectName(u"flag73_and_flag74_lineEdit")
        self.flag73_and_flag74_lineEdit.setMinimumSize(QSize(30, 30))
        self.flag73_and_flag74_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag73_and_flag74_lineEdit.setFont(font)
        self.flag73_and_flag74_lineEdit.setFrame(True)
        self.flag73_and_flag74_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout.addWidget(self.flag73_and_flag74_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag2and3_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag4and5_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag4and5_verticalLayout")
        self.flag75_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag75_label.setObjectName(u"flag75_label")
        self.flag75_label.setFont(font)
        self.flag75_label.setFrameShape(QFrame.Box)
        self.flag75_label.setAlignment(Qt.AlignCenter)
        self.flag75_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.addWidget(self.flag75_label)

        self.flag76_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag76_label.setObjectName(u"flag76_label")
        self.flag76_label.setFont(font)
        self.flag76_label.setFrameShape(QFrame.Box)
        self.flag76_label.setAlignment(Qt.AlignCenter)
        self.flag76_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag4and5_verticalLayout.addWidget(self.flag76_label)


        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag4and5_verticalLayout)

        self.flag75_and_flag76_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag75_and_flag76_lineEdit.setObjectName(u"flag75_and_flag76_lineEdit")
        self.flag75_and_flag76_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag75_and_flag76_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag75_and_flag76_lineEdit.setFont(font)
        self.flag75_and_flag76_lineEdit.setFrame(True)
        self.flag75_and_flag76_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout.addWidget(self.flag75_and_flag76_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag4and5_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag6and7_horizontalLayout")
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout = QVBoxLayout()
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag6and7_verticalLayout")
        self.flag77_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag77_label.setObjectName(u"flag77_label")
        self.flag77_label.setFont(font)
        self.flag77_label.setFrameShape(QFrame.Box)
        self.flag77_label.setAlignment(Qt.AlignCenter)
        self.flag77_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.addWidget(self.flag77_label)

        self.flag78_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag78_label.setObjectName(u"flag78_label")
        self.flag78_label.setFont(font)
        self.flag78_label.setFrameShape(QFrame.Box)
        self.flag78_label.setAlignment(Qt.AlignCenter)
        self.flag78_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag6and7_verticalLayout.addWidget(self.flag78_label)


        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.addLayout(self.ss2sd_or_ss2sq_Flag6and7_verticalLayout)

        self.flag77_and_flag78_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag77_and_flag78_lineEdit.setObjectName(u"flag77_and_flag78_lineEdit")
        self.flag77_and_flag78_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag77_and_flag78_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag77_and_flag78_lineEdit.setFont(font)
        self.flag77_and_flag78_lineEdit.setFrame(True)
        self.flag77_and_flag78_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout.addWidget(self.flag77_and_flag78_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag6and7_horizontalLayout)

        self.flag79_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag79_label.setObjectName(u"flag79_label")
        self.flag79_label.setMaximumSize(QSize(16777215, 18))
        self.flag79_label.setFont(font)
        self.flag79_label.setFrameShape(QFrame.Box)
        self.flag79_label.setAlignment(Qt.AlignCenter)
        self.flag79_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flag79_label)

        self.flag80_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag80_label.setObjectName(u"flag80_label")
        self.flag80_label.setMaximumSize(QSize(16777215, 18))
        self.flag80_label.setFont(font)
        self.flag80_label.setFrameShape(QFrame.Box)
        self.flag80_label.setAlignment(Qt.AlignCenter)
        self.flag80_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flag80_label)

        self.flag81_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag81_label.setObjectName(u"flag81_label")
        self.flag81_label.setMaximumSize(QSize(16777215, 18))
        self.flag81_label.setFont(font)
        self.flag81_label.setFrameShape(QFrame.Box)
        self.flag81_label.setAlignment(Qt.AlignCenter)
        self.flag81_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flag81_label)

        self.flag82_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag82_label.setObjectName(u"flag82_label")
        self.flag82_label.setMaximumSize(QSize(16777215, 18))
        self.flag82_label.setFont(font)
        self.flag82_label.setFrameShape(QFrame.Box)
        self.flag82_label.setAlignment(Qt.AlignCenter)
        self.flag82_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.flag82_label)

        self.ss2sd_or_ss2sq_Flag81_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag81_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag81_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag81_horizontalLayout")
        self.flag83_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag83_label.setObjectName(u"flag83_label")
        self.flag83_label.setFont(font)
        self.flag83_label.setFrameShape(QFrame.Box)
        self.flag83_label.setAlignment(Qt.AlignCenter)
        self.flag83_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag81_horizontalLayout.addWidget(self.flag83_label)

        self.flag83_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag83_lineEdit.setObjectName(u"flag83_lineEdit")
        self.flag83_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag83_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag83_lineEdit.setFont(font)
        self.flag83_lineEdit.setFrame(True)
        self.flag83_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag81_horizontalLayout.addWidget(self.flag83_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag81_horizontalLayout)

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout = QHBoxLayout()
        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.setSpacing(0)
        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.setObjectName(u"ss2sd_or_ss2sq_Flag82_horizontalLayout")
        self.flag84_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame)
        self.flag84_label.setObjectName(u"flag84_label")
        self.flag84_label.setFont(font)
        self.flag84_label.setFrameShape(QFrame.Box)
        self.flag84_label.setAlignment(Qt.AlignCenter)
        self.flag84_label.setWordWrap(True)

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.addWidget(self.flag84_label)

        self.flag84_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame)
        self.flag84_lineEdit.setObjectName(u"flag84_lineEdit")
        self.flag84_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag84_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag84_lineEdit.setFont(font)
        self.flag84_lineEdit.setFrame(True)
        self.flag84_lineEdit.setAlignment(Qt.AlignCenter)

        self.ss2sd_or_ss2sq_Flag82_horizontalLayout.addWidget(self.flag84_lineEdit)


        self.verticalLayout.addLayout(self.ss2sd_or_ss2sq_Flag82_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.ss2sd_or_ss2sq_Frame)

        self.SittingDown_or_Squat_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.SittingDown_or_Squat_Frame.setObjectName(u"SittingDown_or_Squat_Frame")
        self.SittingDown_or_Squat_Frame.setFrameShape(QFrame.StyledPanel)
        self.SittingDown_or_Squat_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.SittingDown_or_Squat_Frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.SittingDown_or_Squat_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.SittingDown_or_Squat_Label.setObjectName(u"SittingDown_or_Squat_Label")
        self.SittingDown_or_Squat_Label.setMaximumSize(QSize(16777215, 18))
        self.SittingDown_or_Squat_Label.setFont(font)
        self.SittingDown_or_Squat_Label.setFrameShape(QFrame.Box)
        self.SittingDown_or_Squat_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.SittingDown_or_Squat_Label)

        self.SittingDown_or_Squat_horizontalLayout = QHBoxLayout()
        self.SittingDown_or_Squat_horizontalLayout.setSpacing(0)
        self.SittingDown_or_Squat_horizontalLayout.setObjectName(u"SittingDown_or_Squat_horizontalLayout")
        self.sdMiddle_or_sqMiddle_verticalLayout = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_verticalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_verticalLayout.setObjectName(u"sdMiddle_or_sqMiddle_verticalLayout")
        self.flag121_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag121_label.setObjectName(u"flag121_label")
        self.flag121_label.setMaximumSize(QSize(16777215, 18))
        self.flag121_label.setFont(font)
        self.flag121_label.setFrameShape(QFrame.Box)
        self.flag121_label.setAlignment(Qt.AlignCenter)
        self.flag121_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout.addWidget(self.flag121_label)

        self.stateNumber_minus5_or_minus11_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.stateNumber_minus5_or_minus11_Label.setObjectName(u"stateNumber_minus5_or_minus11_Label")
        self.stateNumber_minus5_or_minus11_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus5_or_minus11_Label.setFont(font)
        self.stateNumber_minus5_or_minus11_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus5_or_minus11_Label.setAlignment(Qt.AlignCenter)
        self.stateNumber_minus5_or_minus11_Label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout.addWidget(self.stateNumber_minus5_or_minus11_Label)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag11_horizontalLayout")
        self.flag85_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag85_label.setObjectName(u"flag85_label")
        self.flag85_label.setFont(font)
        self.flag85_label.setFrameShape(QFrame.Box)
        self.flag85_label.setAlignment(Qt.AlignCenter)
        self.flag85_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.addWidget(self.flag85_label)

        self.flag85_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame)
        self.flag85_lineEdit.setObjectName(u"flag85_lineEdit")
        self.flag85_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag85_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag85_lineEdit.setFont(font)
        self.flag85_lineEdit.setFrame(True)
        self.flag85_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout.addWidget(self.flag85_lineEdit)


        self.sdMiddle_or_sqMiddle_verticalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout")
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_verticalLayout")
        self.flag86_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag86_label.setObjectName(u"flag86_label")
        self.flag86_label.setFont(font)
        self.flag86_label.setFrameShape(QFrame.Box)
        self.flag86_label.setAlignment(Qt.AlignCenter)
        self.flag86_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.addWidget(self.flag86_label)

        self.flag87_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag87_label.setObjectName(u"flag87_label")
        self.flag87_label.setFont(font)
        self.flag87_label.setFrameShape(QFrame.Box)
        self.flag87_label.setAlignment(Qt.AlignCenter)
        self.flag87_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout.addWidget(self.flag87_label)


        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout)

        self.flag86_and_flag87_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame)
        self.flag86_and_flag87_lineEdit.setObjectName(u"flag86_and_flag87_lineEdit")
        self.flag86_and_flag87_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag86_and_flag87_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag86_and_flag87_lineEdit.setFont(font)
        self.flag86_and_flag87_lineEdit.setFrame(True)
        self.flag86_and_flag87_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout.addWidget(self.flag86_and_flag87_lineEdit)


        self.sdMiddle_or_sqMiddle_verticalLayout.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout)


        self.SittingDown_or_Squat_horizontalLayout.addLayout(self.sdMiddle_or_sqMiddle_verticalLayout)

        self.sdFinal_or_sqDeep_verticalLayout = QVBoxLayout()
        self.sdFinal_or_sqDeep_verticalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_verticalLayout.setObjectName(u"sdFinal_or_sqDeep_verticalLayout")
        self.flag120_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag120_label.setObjectName(u"flag120_label")
        self.flag120_label.setMaximumSize(QSize(16777215, 18))
        self.flag120_label.setFont(font)
        self.flag120_label.setFrameShape(QFrame.Box)
        self.flag120_label.setAlignment(Qt.AlignCenter)
        self.flag120_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout.addWidget(self.flag120_label)

        self.stateNumber_minus6_or_minus12_Label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.stateNumber_minus6_or_minus12_Label.setObjectName(u"stateNumber_minus6_or_minus12_Label")
        self.stateNumber_minus6_or_minus12_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus6_or_minus12_Label.setFont(font)
        self.stateNumber_minus6_or_minus12_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus6_or_minus12_Label.setAlignment(Qt.AlignCenter)
        self.stateNumber_minus6_or_minus12_Label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout.addWidget(self.stateNumber_minus6_or_minus12_Label)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout = QHBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_horizontalLayout")
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout = QVBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_verticalLayout")
        self.flag88_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag88_label.setObjectName(u"flag88_label")
        self.flag88_label.setFont(font)
        self.flag88_label.setFrameShape(QFrame.Box)
        self.flag88_label.setAlignment(Qt.AlignCenter)
        self.flag88_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.addWidget(self.flag88_label)

        self.flag89_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame)
        self.flag89_label.setObjectName(u"flag89_label")
        self.flag89_label.setFont(font)
        self.flag89_label.setFrameShape(QFrame.Box)
        self.flag89_label.setAlignment(Qt.AlignCenter)
        self.flag89_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout.addWidget(self.flag89_label)


        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.addLayout(self.sdFinal_or_sqDeep_Flag1and2_verticalLayout)

        self.flag88_and_flag89_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame)
        self.flag88_and_flag89_lineEdit.setObjectName(u"flag88_and_flag89_lineEdit")
        self.flag88_and_flag89_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag88_and_flag89_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag88_and_flag89_lineEdit.setFont(font)
        self.flag88_and_flag89_lineEdit.setFrame(True)
        self.flag88_and_flag89_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout.addWidget(self.flag88_and_flag89_lineEdit)


        self.sdFinal_or_sqDeep_verticalLayout.addLayout(self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout)


        self.SittingDown_or_Squat_horizontalLayout.addLayout(self.sdFinal_or_sqDeep_verticalLayout)


        self.verticalLayout_13.addLayout(self.SittingDown_or_Squat_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.SittingDown_or_Squat_Frame)

        self.seated_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.seated_Frame.setObjectName(u"seated_Frame")
        self.seated_Frame.setFrameShape(QFrame.StyledPanel)
        self.seated_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.seated_Frame)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.flag119_label = ColorChangingFrame(self.seated_Frame)
        self.flag119_label.setObjectName(u"flag119_label")
        self.flag119_label.setMaximumSize(QSize(16777215, 36))
        self.flag119_label.setFont(font)
        self.flag119_label.setFrameShape(QFrame.Box)
        self.flag119_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.flag119_label)

        self.stateNumber_minus7_Label = ColorChangingFrame(self.seated_Frame)
        self.stateNumber_minus7_Label.setObjectName(u"stateNumber_minus7_Label")
        self.stateNumber_minus7_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus7_Label.setFont(font)
        self.stateNumber_minus7_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus7_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.stateNumber_minus7_Label)

        self.seated_Flag11_horizontalLayout = QHBoxLayout()
        self.seated_Flag11_horizontalLayout.setSpacing(0)
        self.seated_Flag11_horizontalLayout.setObjectName(u"seated_Flag11_horizontalLayout")
        self.flag90_label = ColorChangingFrame(self.seated_Frame)
        self.flag90_label.setObjectName(u"flag90_label")
        self.flag90_label.setMaximumSize(QSize(16777215, 800))
        self.flag90_label.setFont(font)
        self.flag90_label.setFrameShape(QFrame.Box)
        self.flag90_label.setAlignment(Qt.AlignCenter)
        self.flag90_label.setWordWrap(True)

        self.seated_Flag11_horizontalLayout.addWidget(self.flag90_label)

        self.flag90_lineEdit = QLineEdit(self.seated_Frame)
        self.flag90_lineEdit.setObjectName(u"flag90_lineEdit")
        self.flag90_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag90_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag90_lineEdit.setFont(font)
        self.flag90_lineEdit.setFrame(True)
        self.flag90_lineEdit.setAlignment(Qt.AlignCenter)

        self.seated_Flag11_horizontalLayout.addWidget(self.flag90_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag11_horizontalLayout)

        self.seated_Flag12and13_horizontalLayout = QHBoxLayout()
        self.seated_Flag12and13_horizontalLayout.setSpacing(0)
        self.seated_Flag12and13_horizontalLayout.setObjectName(u"seated_Flag12and13_horizontalLayout")
        self.seated_Flag12and13_verticalLayout = QVBoxLayout()
        self.seated_Flag12and13_verticalLayout.setSpacing(0)
        self.seated_Flag12and13_verticalLayout.setObjectName(u"seated_Flag12and13_verticalLayout")
        self.flag91_label = ColorChangingFrame(self.seated_Frame)
        self.flag91_label.setObjectName(u"flag91_label")
        self.flag91_label.setFont(font)
        self.flag91_label.setFrameShape(QFrame.Box)
        self.flag91_label.setAlignment(Qt.AlignCenter)
        self.flag91_label.setWordWrap(True)

        self.seated_Flag12and13_verticalLayout.addWidget(self.flag91_label)

        self.flag92_label = ColorChangingFrame(self.seated_Frame)
        self.flag92_label.setObjectName(u"flag92_label")
        self.flag92_label.setFont(font)
        self.flag92_label.setFrameShape(QFrame.Box)
        self.flag92_label.setAlignment(Qt.AlignCenter)
        self.flag92_label.setWordWrap(True)

        self.seated_Flag12and13_verticalLayout.addWidget(self.flag92_label)


        self.seated_Flag12and13_horizontalLayout.addLayout(self.seated_Flag12and13_verticalLayout)

        self.flag91_and_flag92_lineEdit = QLineEdit(self.seated_Frame)
        self.flag91_and_flag92_lineEdit.setObjectName(u"flag91_and_flag92_lineEdit")
        self.flag91_and_flag92_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag91_and_flag92_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag91_and_flag92_lineEdit.setFont(font)
        self.flag91_and_flag92_lineEdit.setFrame(True)
        self.flag91_and_flag92_lineEdit.setAlignment(Qt.AlignCenter)
        self.flag91_and_flag92_lineEdit.setReadOnly(False)

        self.seated_Flag12and13_horizontalLayout.addWidget(self.flag91_and_flag92_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag12and13_horizontalLayout)

        self.or_seated_Label = ColorChangingFrame(self.seated_Frame)
        self.or_seated_Label.setObjectName(u"or_seated_Label")
        self.or_seated_Label.setMaximumSize(QSize(16777215, 18))
        self.or_seated_Label.setFont(font)
        self.or_seated_Label.setFrameShape(QFrame.Box)
        self.or_seated_Label.setAlignment(Qt.AlignCenter)
        self.or_seated_Label.setWordWrap(True)

        self.verticalLayout_41.addWidget(self.or_seated_Label)

        self.seated_Flag2and3_horizontalLayout = QHBoxLayout()
        self.seated_Flag2and3_horizontalLayout.setSpacing(0)
        self.seated_Flag2and3_horizontalLayout.setObjectName(u"seated_Flag2and3_horizontalLayout")
        self.seated_Flag2and3_Label_verticalLayout = QVBoxLayout()
        self.seated_Flag2and3_Label_verticalLayout.setSpacing(0)
        self.seated_Flag2and3_Label_verticalLayout.setObjectName(u"seated_Flag2and3_Label_verticalLayout")
        self.flag93_label = ColorChangingFrame(self.seated_Frame)
        self.flag93_label.setObjectName(u"flag93_label")
        self.flag93_label.setFont(font)
        self.flag93_label.setFrameShape(QFrame.Box)
        self.flag93_label.setAlignment(Qt.AlignCenter)
        self.flag93_label.setWordWrap(True)

        self.seated_Flag2and3_Label_verticalLayout.addWidget(self.flag93_label)

        self.flag94_label = ColorChangingFrame(self.seated_Frame)
        self.flag94_label.setObjectName(u"flag94_label")
        self.flag94_label.setFont(font)
        self.flag94_label.setFrameShape(QFrame.Box)
        self.flag94_label.setAlignment(Qt.AlignCenter)
        self.flag94_label.setWordWrap(True)

        self.seated_Flag2and3_Label_verticalLayout.addWidget(self.flag94_label)


        self.seated_Flag2and3_horizontalLayout.addLayout(self.seated_Flag2and3_Label_verticalLayout)

        self.flag93_and_flag94_lineEdit = QLineEdit(self.seated_Frame)
        self.flag93_and_flag94_lineEdit.setObjectName(u"flag93_and_flag94_lineEdit")
        self.flag93_and_flag94_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag93_and_flag94_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag93_and_flag94_lineEdit.setFont(font)
        self.flag93_and_flag94_lineEdit.setFrame(True)
        self.flag93_and_flag94_lineEdit.setAlignment(Qt.AlignCenter)

        self.seated_Flag2and3_horizontalLayout.addWidget(self.flag93_and_flag94_lineEdit)


        self.verticalLayout_41.addLayout(self.seated_Flag2and3_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.seated_Frame)

        self.standingUp_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.standingUp_Frame.setObjectName(u"standingUp_Frame")
        self.standingUp_Frame.setFrameShape(QFrame.StyledPanel)
        self.standingUp_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.standingUp_Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.StandingUp_horizontalLayout = QHBoxLayout()
        self.StandingUp_horizontalLayout.setSpacing(0)
        self.StandingUp_horizontalLayout.setObjectName(u"StandingUp_horizontalLayout")
        self.seated2su_Frame = QFrame(self.standingUp_Frame)
        self.seated2su_Frame.setObjectName(u"seated2su_Frame")
        self.seated2su_Frame.setFrameShape(QFrame.StyledPanel)
        self.seated2su_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.seated2su_Frame)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.flag118_label = ColorChangingFrame(self.seated2su_Frame)
        self.flag118_label.setObjectName(u"flag118_label")
        self.flag118_label.setMaximumSize(QSize(16777215, 36))
        self.flag118_label.setFont(font)
        self.flag118_label.setFrameShape(QFrame.Box)
        self.flag118_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.flag118_label)

        self.stateNumber_minus8_Label = ColorChangingFrame(self.seated2su_Frame)
        self.stateNumber_minus8_Label.setObjectName(u"stateNumber_minus8_Label")
        self.stateNumber_minus8_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus8_Label.setFont(font)
        self.stateNumber_minus8_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus8_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.stateNumber_minus8_Label)

        self.seated2su_Flag1and2_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag1and2_horizontalLayout.setSpacing(0)
        self.seated2su_Flag1and2_horizontalLayout.setObjectName(u"seated2su_Flag1and2_horizontalLayout")
        self.seated2su_Flag1and2_verticalLayout = QVBoxLayout()
        self.seated2su_Flag1and2_verticalLayout.setSpacing(0)
        self.seated2su_Flag1and2_verticalLayout.setObjectName(u"seated2su_Flag1and2_verticalLayout")
        self.flag95_label = ColorChangingFrame(self.seated2su_Frame)
        self.flag95_label.setObjectName(u"flag95_label")
        self.flag95_label.setFont(font)
        self.flag95_label.setFrameShape(QFrame.Box)
        self.flag95_label.setAlignment(Qt.AlignCenter)
        self.flag95_label.setWordWrap(True)

        self.seated2su_Flag1and2_verticalLayout.addWidget(self.flag95_label)

        self.flag96_label = ColorChangingFrame(self.seated2su_Frame)
        self.flag96_label.setObjectName(u"flag96_label")
        self.flag96_label.setFont(font)
        self.flag96_label.setFrameShape(QFrame.Box)
        self.flag96_label.setAlignment(Qt.AlignCenter)
        self.flag96_label.setWordWrap(True)

        self.seated2su_Flag1and2_verticalLayout.addWidget(self.flag96_label)


        self.seated2su_Flag1and2_horizontalLayout.addLayout(self.seated2su_Flag1and2_verticalLayout)

        self.flag95_and_flag96_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flag95_and_flag96_lineEdit.setObjectName(u"flag95_and_flag96_lineEdit")
        self.flag95_and_flag96_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag95_and_flag96_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag95_and_flag96_lineEdit.setFont(font)
        self.flag95_and_flag96_lineEdit.setFrame(True)
        self.flag95_and_flag96_lineEdit.setAlignment(Qt.AlignCenter)

        self.seated2su_Flag1and2_horizontalLayout.addWidget(self.flag95_and_flag96_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag1and2_horizontalLayout)

        self.seated2su_Flag31_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag31_horizontalLayout.setSpacing(0)
        self.seated2su_Flag31_horizontalLayout.setObjectName(u"seated2su_Flag31_horizontalLayout")
        self.flag97_label = ColorChangingFrame(self.seated2su_Frame)
        self.flag97_label.setObjectName(u"flag97_label")
        self.flag97_label.setFont(font)
        self.flag97_label.setFrameShape(QFrame.Box)
        self.flag97_label.setAlignment(Qt.AlignCenter)
        self.flag97_label.setWordWrap(True)

        self.seated2su_Flag31_horizontalLayout.addWidget(self.flag97_label)

        self.flag97_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flag97_lineEdit.setObjectName(u"flag97_lineEdit")
        self.flag97_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag97_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag97_lineEdit.setFont(font)
        self.flag97_lineEdit.setFrame(True)
        self.flag97_lineEdit.setAlignment(Qt.AlignCenter)

        self.seated2su_Flag31_horizontalLayout.addWidget(self.flag97_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag31_horizontalLayout)

        self.seated2su_Flag32_horizontalLayout = QHBoxLayout()
        self.seated2su_Flag32_horizontalLayout.setSpacing(0)
        self.seated2su_Flag32_horizontalLayout.setObjectName(u"seated2su_Flag32_horizontalLayout")
        self.flag98_label = ColorChangingFrame(self.seated2su_Frame)
        self.flag98_label.setObjectName(u"flag98_label")
        self.flag98_label.setFont(font)
        self.flag98_label.setFrameShape(QFrame.Box)
        self.flag98_label.setAlignment(Qt.AlignCenter)
        self.flag98_label.setWordWrap(True)

        self.seated2su_Flag32_horizontalLayout.addWidget(self.flag98_label)

        self.flag98_lineEdit = QLineEdit(self.seated2su_Frame)
        self.flag98_lineEdit.setObjectName(u"flag98_lineEdit")
        self.flag98_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag98_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag98_lineEdit.setFont(font)
        self.flag98_lineEdit.setFrame(True)
        self.flag98_lineEdit.setAlignment(Qt.AlignCenter)

        self.seated2su_Flag32_horizontalLayout.addWidget(self.flag98_lineEdit)


        self.verticalLayout_43.addLayout(self.seated2su_Flag32_horizontalLayout)


        self.StandingUp_horizontalLayout.addWidget(self.seated2su_Frame)

        self.sub_standingUp_Frame = QFrame(self.standingUp_Frame)
        self.sub_standingUp_Frame.setObjectName(u"sub_standingUp_Frame")
        self.sub_standingUp_Frame.setFrameShape(QFrame.StyledPanel)
        self.sub_standingUp_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.sub_standingUp_Frame)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.flag117_label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.flag117_label.setObjectName(u"flag117_label")
        self.flag117_label.setMaximumSize(QSize(16777215, 36))
        self.flag117_label.setFont(font)
        self.flag117_label.setFrameShape(QFrame.Box)
        self.flag117_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.flag117_label)

        self.stateNumber_minus9_Label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.stateNumber_minus9_Label.setObjectName(u"stateNumber_minus9_Label")
        self.stateNumber_minus9_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus9_Label.setFont(font)
        self.stateNumber_minus9_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus9_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.stateNumber_minus9_Label)

        self.standingUp_Flag1_horizontalLayout = QHBoxLayout()
        self.standingUp_Flag1_horizontalLayout.setSpacing(0)
        self.standingUp_Flag1_horizontalLayout.setObjectName(u"standingUp_Flag1_horizontalLayout")
        self.flag99_label = ColorChangingFrame(self.sub_standingUp_Frame)
        self.flag99_label.setObjectName(u"flag99_label")
        self.flag99_label.setFont(font)
        self.flag99_label.setFrameShape(QFrame.Box)
        self.flag99_label.setAlignment(Qt.AlignCenter)
        self.flag99_label.setWordWrap(True)

        self.standingUp_Flag1_horizontalLayout.addWidget(self.flag99_label)

        self.flag99_lineEdit = QLineEdit(self.sub_standingUp_Frame)
        self.flag99_lineEdit.setObjectName(u"flag99_lineEdit")
        self.flag99_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag99_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag99_lineEdit.setFont(font)
        self.flag99_lineEdit.setFrame(True)
        self.flag99_lineEdit.setAlignment(Qt.AlignCenter)

        self.standingUp_Flag1_horizontalLayout.addWidget(self.flag99_lineEdit)


        self.verticalLayout_44.addLayout(self.standingUp_Flag1_horizontalLayout)


        self.StandingUp_horizontalLayout.addWidget(self.sub_standingUp_Frame)


        self.verticalLayout_2.addLayout(self.StandingUp_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.standingUp_Frame)

        self.su2ss_Frame = QFrame(self.Stand2SitandSit2StandandSquatTasks_subframe)
        self.su2ss_Frame.setObjectName(u"su2ss_Frame")
        self.su2ss_Frame.setFrameShape(QFrame.StyledPanel)
        self.su2ss_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.su2ss_Frame)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.su2ss_Label = ColorChangingFrame(self.su2ss_Frame)
        self.su2ss_Label.setObjectName(u"su2ss_Label")
        self.su2ss_Label.setMaximumSize(QSize(16777215, 18))
        self.su2ss_Label.setFont(font)
        self.su2ss_Label.setFrameShape(QFrame.Box)
        self.su2ss_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.su2ss_Label)

        self.flag128_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag128_label.setObjectName(u"flag128_label")
        self.flag128_label.setMaximumSize(QSize(16777215, 18))
        self.flag128_label.setFont(font)
        self.flag128_label.setFrameShape(QFrame.Box)
        self.flag128_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.flag128_label)

        self.su2ss_stateNumber0_Label = ColorChangingFrame(self.su2ss_Frame)
        self.su2ss_stateNumber0_Label.setObjectName(u"su2ss_stateNumber0_Label")
        self.su2ss_stateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.su2ss_stateNumber0_Label.setFont(font)
        self.su2ss_stateNumber0_Label.setFrameShape(QFrame.Box)
        self.su2ss_stateNumber0_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.su2ss_stateNumber0_Label)

        self.standingStill_Flag1and2_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag1and2_horizontalLayout.setSpacing(0)
        self.standingStill_Flag1and2_horizontalLayout.setObjectName(u"standingStill_Flag1and2_horizontalLayout")
        self.standingStill_Flag1and2_verticalLayout = QVBoxLayout()
        self.standingStill_Flag1and2_verticalLayout.setSpacing(0)
        self.standingStill_Flag1and2_verticalLayout.setObjectName(u"standingStill_Flag1and2_verticalLayout")
        self.flag100_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag100_label.setObjectName(u"flag100_label")
        self.flag100_label.setFont(font)
        self.flag100_label.setFrameShape(QFrame.Box)
        self.flag100_label.setAlignment(Qt.AlignCenter)
        self.flag100_label.setWordWrap(True)

        self.standingStill_Flag1and2_verticalLayout.addWidget(self.flag100_label)

        self.flag101_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag101_label.setObjectName(u"flag101_label")
        self.flag101_label.setFont(font)
        self.flag101_label.setFrameShape(QFrame.Box)
        self.flag101_label.setAlignment(Qt.AlignCenter)
        self.flag101_label.setWordWrap(True)

        self.standingStill_Flag1and2_verticalLayout.addWidget(self.flag101_label)


        self.standingStill_Flag1and2_horizontalLayout.addLayout(self.standingStill_Flag1and2_verticalLayout)

        self.flag100_and_flag101_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flag100_and_flag101_lineEdit.setObjectName(u"flag100_and_flag101_lineEdit")
        self.flag100_and_flag101_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag100_and_flag101_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag100_and_flag101_lineEdit.setFont(font)
        self.flag100_and_flag101_lineEdit.setFrame(True)
        self.flag100_and_flag101_lineEdit.setAlignment(Qt.AlignCenter)

        self.standingStill_Flag1and2_horizontalLayout.addWidget(self.flag100_and_flag101_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag1and2_horizontalLayout)

        self.standingStill_Flag31_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag31_horizontalLayout.setSpacing(0)
        self.standingStill_Flag31_horizontalLayout.setObjectName(u"standingStill_Flag31_horizontalLayout")
        self.flag102_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag102_label.setObjectName(u"flag102_label")
        self.flag102_label.setFont(font)
        self.flag102_label.setFrameShape(QFrame.Box)
        self.flag102_label.setAlignment(Qt.AlignCenter)
        self.flag102_label.setWordWrap(True)

        self.standingStill_Flag31_horizontalLayout.addWidget(self.flag102_label)

        self.flag102_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flag102_lineEdit.setObjectName(u"flag102_lineEdit")
        self.flag102_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag102_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag102_lineEdit.setFont(font)
        self.flag102_lineEdit.setFrame(True)
        self.flag102_lineEdit.setAlignment(Qt.AlignCenter)

        self.standingStill_Flag31_horizontalLayout.addWidget(self.flag102_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag31_horizontalLayout)

        self.standingStill_Flag31and32_horizontalLayout = QHBoxLayout()
        self.standingStill_Flag31and32_horizontalLayout.setSpacing(0)
        self.standingStill_Flag31and32_horizontalLayout.setObjectName(u"standingStill_Flag31and32_horizontalLayout")
        self.standingStill_Flag31and32_verticalLayout = QVBoxLayout()
        self.standingStill_Flag31and32_verticalLayout.setSpacing(0)
        self.standingStill_Flag31and32_verticalLayout.setObjectName(u"standingStill_Flag31and32_verticalLayout")
        self.flag103_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag103_label.setObjectName(u"flag103_label")
        self.flag103_label.setFont(font)
        self.flag103_label.setFrameShape(QFrame.Box)
        self.flag103_label.setAlignment(Qt.AlignCenter)
        self.flag103_label.setWordWrap(True)

        self.standingStill_Flag31and32_verticalLayout.addWidget(self.flag103_label)

        self.flag104_label = ColorChangingFrame(self.su2ss_Frame)
        self.flag104_label.setObjectName(u"flag104_label")
        self.flag104_label.setFont(font)
        self.flag104_label.setFrameShape(QFrame.Box)
        self.flag104_label.setAlignment(Qt.AlignCenter)
        self.flag104_label.setWordWrap(True)

        self.standingStill_Flag31and32_verticalLayout.addWidget(self.flag104_label)


        self.standingStill_Flag31and32_horizontalLayout.addLayout(self.standingStill_Flag31and32_verticalLayout)

        self.flag103_and_flag104_lineEdit = QLineEdit(self.su2ss_Frame)
        self.flag103_and_flag104_lineEdit.setObjectName(u"flag103_and_flag104_lineEdit")
        self.flag103_and_flag104_lineEdit.setMinimumSize(QSize(30, 20))
        self.flag103_and_flag104_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag103_and_flag104_lineEdit.setFont(font)
        self.flag103_and_flag104_lineEdit.setFrame(True)
        self.flag103_and_flag104_lineEdit.setAlignment(Qt.AlignCenter)

        self.standingStill_Flag31and32_horizontalLayout.addWidget(self.flag103_and_flag104_lineEdit)


        self.verticalLayout_47.addLayout(self.standingStill_Flag31and32_horizontalLayout)


        self.horizontalLayout_2.addWidget(self.su2ss_Frame)


        self.verticalLayout_3.addWidget(self.Stand2SitandSit2StandandSquatTasks_subframe)


        self.verticalLayout_17.addWidget(self.Stand2SitandSit2StandandSquatTasks_frame)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.turningTask_Frame = QFrame(self.Main_widget)
        self.turningTask_Frame.setObjectName(u"turningTask_Frame")
        self.turningTask_Frame.setFrameShape(QFrame.StyledPanel)
        self.turningTask_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.turningTask_Frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.flag111_label = ColorChangingFrame(self.turningTask_Frame)
        self.flag111_label.setObjectName(u"flag111_label")
        self.flag111_label.setMaximumSize(QSize(16777215, 18))
        self.flag111_label.setFont(font)
        self.flag111_label.setFrameShape(QFrame.Box)
        self.flag111_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.flag111_label)

        self.turningTask_sub_Frame = QFrame(self.turningTask_Frame)
        self.turningTask_sub_Frame.setObjectName(u"turningTask_sub_Frame")
        self.turningTask_sub_Frame.setFrameShape(QFrame.StyledPanel)
        self.turningTask_sub_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.turningTask_sub_Frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.ss2t_Frame = QFrame(self.turningTask_sub_Frame)
        self.ss2t_Frame.setObjectName(u"ss2t_Frame")
        self.ss2t_Frame.setFrameShape(QFrame.NoFrame)
        self.ss2t_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ss2t_Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ss2t_Label = ColorChangingFrame(self.ss2t_Frame)
        self.ss2t_Label.setObjectName(u"ss2t_Label")
        self.ss2t_Label.setMaximumSize(QSize(16777215, 18))
        self.ss2t_Label.setFont(font)
        self.ss2t_Label.setFrameShape(QFrame.Box)
        self.ss2t_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.ss2t_Label)

        self.flag125_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag125_label.setObjectName(u"flag125_label")
        self.flag125_label.setMaximumSize(QSize(16777215, 18))
        self.flag125_label.setFont(font)
        self.flag125_label.setFrameShape(QFrame.Box)
        self.flag125_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.flag125_label)

        self.stateNumber_minus1_Label = ColorChangingFrame(self.ss2t_Frame)
        self.stateNumber_minus1_Label.setObjectName(u"stateNumber_minus1_Label")
        self.stateNumber_minus1_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus1_Label.setFont(font)
        self.stateNumber_minus1_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus1_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.stateNumber_minus1_Label)

        self.turningStart_Flag1_horizontalLayout = QHBoxLayout()
        self.turningStart_Flag1_horizontalLayout.setSpacing(0)
        self.turningStart_Flag1_horizontalLayout.setObjectName(u"turningStart_Flag1_horizontalLayout")
        self.flag19_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag19_label.setObjectName(u"flag19_label")
        self.flag19_label.setFont(font)
        self.flag19_label.setFrameShape(QFrame.Box)
        self.flag19_label.setAlignment(Qt.AlignCenter)
        self.flag19_label.setWordWrap(True)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flag19_label)

        self.flag20_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag20_label.setObjectName(u"flag20_label")
        self.flag20_label.setFont(font)
        self.flag20_label.setFrameShape(QFrame.Box)
        self.flag20_label.setAlignment(Qt.AlignCenter)
        self.flag20_label.setWordWrap(True)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flag20_label)

        self.flag19_and_flag20_lineEdit = QLineEdit(self.ss2t_Frame)
        self.flag19_and_flag20_lineEdit.setObjectName(u"flag19_and_flag20_lineEdit")
        self.flag19_and_flag20_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag19_and_flag20_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag19_and_flag20_lineEdit.setFont(font)
        self.flag19_and_flag20_lineEdit.setFrame(True)
        self.flag19_and_flag20_lineEdit.setAlignment(Qt.AlignCenter)

        self.turningStart_Flag1_horizontalLayout.addWidget(self.flag19_and_flag20_lineEdit)


        self.verticalLayout_6.addLayout(self.turningStart_Flag1_horizontalLayout)

        self.turningStart_Flag2_horizontalLayout = QHBoxLayout()
        self.turningStart_Flag2_horizontalLayout.setSpacing(0)
        self.turningStart_Flag2_horizontalLayout.setObjectName(u"turningStart_Flag2_horizontalLayout")
        self.flag21_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag21_label.setObjectName(u"flag21_label")
        self.flag21_label.setFont(font)
        self.flag21_label.setFrameShape(QFrame.Box)
        self.flag21_label.setAlignment(Qt.AlignCenter)

        self.turningStart_Flag2_horizontalLayout.addWidget(self.flag21_label)

        self.flag21_lineEdit = QLineEdit(self.ss2t_Frame)
        self.flag21_lineEdit.setObjectName(u"flag21_lineEdit")
        self.flag21_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag21_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag21_lineEdit.setFont(font)
        self.flag21_lineEdit.setFrame(True)
        self.flag21_lineEdit.setAlignment(Qt.AlignCenter)

        self.turningStart_Flag2_horizontalLayout.addWidget(self.flag21_lineEdit)


        self.verticalLayout_6.addLayout(self.turningStart_Flag2_horizontalLayout)

        self.flag22_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag22_label.setObjectName(u"flag22_label")
        self.flag22_label.setMaximumSize(QSize(16777215, 18))
        self.flag22_label.setFont(font)
        self.flag22_label.setFrameShape(QFrame.Box)
        self.flag22_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.flag22_label)

        self.flag23_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag23_label.setObjectName(u"flag23_label")
        self.flag23_label.setMaximumSize(QSize(16777215, 18))
        self.flag23_label.setFont(font)
        self.flag23_label.setFrameShape(QFrame.Box)
        self.flag23_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.flag23_label)

        self.flag24_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag24_label.setObjectName(u"flag24_label")
        self.flag24_label.setMaximumSize(QSize(16777215, 18))
        self.flag24_label.setFont(font)
        self.flag24_label.setFrameShape(QFrame.Box)
        self.flag24_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.flag24_label)

        self.flag25_label = ColorChangingFrame(self.ss2t_Frame)
        self.flag25_label.setObjectName(u"flag25_label")
        self.flag25_label.setMaximumSize(QSize(16777215, 18))
        self.flag25_label.setFont(font)
        self.flag25_label.setFrameShape(QFrame.Box)
        self.flag25_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.flag25_label)


        self.horizontalLayout_53.addWidget(self.ss2t_Frame)

        self.turning_Frame = QFrame(self.turningTask_sub_Frame)
        self.turning_Frame.setObjectName(u"turning_Frame")
        self.turning_Frame.setFrameShape(QFrame.NoFrame)
        self.turning_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.turning_Frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.turning_Label = ColorChangingFrame(self.turning_Frame)
        self.turning_Label.setObjectName(u"turning_Label")
        self.turning_Label.setMaximumSize(QSize(16777215, 18))
        self.turning_Label.setFont(font)
        self.turning_Label.setFrameShape(QFrame.Box)
        self.turning_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.turning_Label)

        self.turning_horizontalLayout = QHBoxLayout()
        self.turning_horizontalLayout.setSpacing(0)
        self.turning_horizontalLayout.setObjectName(u"turning_horizontalLayout")
        self.turningMiddle_verticalLayout = QVBoxLayout()
        self.turningMiddle_verticalLayout.setSpacing(0)
        self.turningMiddle_verticalLayout.setObjectName(u"turningMiddle_verticalLayout")
        self.flag124_label = ColorChangingFrame(self.turning_Frame)
        self.flag124_label.setObjectName(u"flag124_label")
        self.flag124_label.setMaximumSize(QSize(16777215, 18))
        self.flag124_label.setFont(font)
        self.flag124_label.setFrameShape(QFrame.Box)
        self.flag124_label.setAlignment(Qt.AlignCenter)

        self.turningMiddle_verticalLayout.addWidget(self.flag124_label)

        self.stateNumber_minus2_Label = ColorChangingFrame(self.turning_Frame)
        self.stateNumber_minus2_Label.setObjectName(u"stateNumber_minus2_Label")
        self.stateNumber_minus2_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus2_Label.setFont(font)
        self.stateNumber_minus2_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus2_Label.setAlignment(Qt.AlignCenter)

        self.turningMiddle_verticalLayout.addWidget(self.stateNumber_minus2_Label)

        self.turningMiddle_Flag1_horizontalLayout = QHBoxLayout()
        self.turningMiddle_Flag1_horizontalLayout.setSpacing(0)
        self.turningMiddle_Flag1_horizontalLayout.setObjectName(u"turningMiddle_Flag1_horizontalLayout")
        self.flag26_label = ColorChangingFrame(self.turning_Frame)
        self.flag26_label.setObjectName(u"flag26_label")
        self.flag26_label.setFont(font)
        self.flag26_label.setFrameShape(QFrame.Box)
        self.flag26_label.setAlignment(Qt.AlignCenter)
        self.flag26_label.setWordWrap(True)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flag26_label)

        self.flag27_label = ColorChangingFrame(self.turning_Frame)
        self.flag27_label.setObjectName(u"flag27_label")
        self.flag27_label.setFont(font)
        self.flag27_label.setFrameShape(QFrame.Box)
        self.flag27_label.setAlignment(Qt.AlignCenter)
        self.flag27_label.setWordWrap(True)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flag27_label)

        self.flag26_and_flag27_lineEdit = QLineEdit(self.turning_Frame)
        self.flag26_and_flag27_lineEdit.setObjectName(u"flag26_and_flag27_lineEdit")
        self.flag26_and_flag27_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag26_and_flag27_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag26_and_flag27_lineEdit.setFont(font)
        self.flag26_and_flag27_lineEdit.setFrame(True)
        self.flag26_and_flag27_lineEdit.setAlignment(Qt.AlignCenter)

        self.turningMiddle_Flag1_horizontalLayout.addWidget(self.flag26_and_flag27_lineEdit)


        self.turningMiddle_verticalLayout.addLayout(self.turningMiddle_Flag1_horizontalLayout)

        self.turningMiddle_Flag2_horizontalLayout = QHBoxLayout()
        self.turningMiddle_Flag2_horizontalLayout.setSpacing(0)
        self.turningMiddle_Flag2_horizontalLayout.setObjectName(u"turningMiddle_Flag2_horizontalLayout")
        self.flag28_label = ColorChangingFrame(self.turning_Frame)
        self.flag28_label.setObjectName(u"flag28_label")
        self.flag28_label.setFont(font)
        self.flag28_label.setFrameShape(QFrame.Box)
        self.flag28_label.setAlignment(Qt.AlignCenter)
        self.flag28_label.setWordWrap(True)

        self.turningMiddle_Flag2_horizontalLayout.addWidget(self.flag28_label)

        self.flag28_lineEdit = QLineEdit(self.turning_Frame)
        self.flag28_lineEdit.setObjectName(u"flag28_lineEdit")
        self.flag28_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag28_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag28_lineEdit.setFont(font)
        self.flag28_lineEdit.setFrame(True)
        self.flag28_lineEdit.setAlignment(Qt.AlignCenter)

        self.turningMiddle_Flag2_horizontalLayout.addWidget(self.flag28_lineEdit)


        self.turningMiddle_verticalLayout.addLayout(self.turningMiddle_Flag2_horizontalLayout)


        self.turning_horizontalLayout.addLayout(self.turningMiddle_verticalLayout)

        self.turningFinal_verticalLayout = QVBoxLayout()
        self.turningFinal_verticalLayout.setSpacing(0)
        self.turningFinal_verticalLayout.setObjectName(u"turningFinal_verticalLayout")
        self.flag123_label = ColorChangingFrame(self.turning_Frame)
        self.flag123_label.setObjectName(u"flag123_label")
        self.flag123_label.setMaximumSize(QSize(16777215, 18))
        self.flag123_label.setFont(font)
        self.flag123_label.setFrameShape(QFrame.Box)
        self.flag123_label.setAlignment(Qt.AlignCenter)

        self.turningFinal_verticalLayout.addWidget(self.flag123_label)

        self.stateNumber_minus3_Label = ColorChangingFrame(self.turning_Frame)
        self.stateNumber_minus3_Label.setObjectName(u"stateNumber_minus3_Label")
        self.stateNumber_minus3_Label.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus3_Label.setFont(font)
        self.stateNumber_minus3_Label.setFrameShape(QFrame.Box)
        self.stateNumber_minus3_Label.setAlignment(Qt.AlignCenter)

        self.turningFinal_verticalLayout.addWidget(self.stateNumber_minus3_Label)

        self.turningFinal_Flag1_horizontalLayout = QHBoxLayout()
        self.turningFinal_Flag1_horizontalLayout.setSpacing(0)
        self.turningFinal_Flag1_horizontalLayout.setObjectName(u"turningFinal_Flag1_horizontalLayout")
        self.flag29_label = ColorChangingFrame(self.turning_Frame)
        self.flag29_label.setObjectName(u"flag29_label")
        self.flag29_label.setFont(font)
        self.flag29_label.setFrameShape(QFrame.Box)
        self.flag29_label.setAlignment(Qt.AlignCenter)
        self.flag29_label.setWordWrap(True)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flag29_label)

        self.flag30_label = ColorChangingFrame(self.turning_Frame)
        self.flag30_label.setObjectName(u"flag30_label")
        self.flag30_label.setFont(font)
        self.flag30_label.setFrameShape(QFrame.Box)
        self.flag30_label.setAlignment(Qt.AlignCenter)
        self.flag30_label.setWordWrap(True)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flag30_label)

        self.flag29_and_flag30_lineEdit = QLineEdit(self.turning_Frame)
        self.flag29_and_flag30_lineEdit.setObjectName(u"flag29_and_flag30_lineEdit")
        self.flag29_and_flag30_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag29_and_flag30_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag29_and_flag30_lineEdit.setFont(font)
        self.flag29_and_flag30_lineEdit.setFrame(True)
        self.flag29_and_flag30_lineEdit.setAlignment(Qt.AlignCenter)

        self.turningFinal_Flag1_horizontalLayout.addWidget(self.flag29_and_flag30_lineEdit)


        self.turningFinal_verticalLayout.addLayout(self.turningFinal_Flag1_horizontalLayout)


        self.turning_horizontalLayout.addLayout(self.turningFinal_verticalLayout)


        self.verticalLayout_21.addLayout(self.turning_horizontalLayout)


        self.horizontalLayout_53.addWidget(self.turning_Frame)

        self.t2ss_Frame = QFrame(self.turningTask_sub_Frame)
        self.t2ss_Frame.setObjectName(u"t2ss_Frame")
        self.t2ss_Frame.setFrameShape(QFrame.NoFrame)
        self.t2ss_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.t2ss_Frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stopTurning_Label = ColorChangingFrame(self.t2ss_Frame)
        self.stopTurning_Label.setObjectName(u"stopTurning_Label")
        self.stopTurning_Label.setMaximumSize(QSize(16777215, 18))
        self.stopTurning_Label.setFont(font)
        self.stopTurning_Label.setFrameShape(QFrame.Box)
        self.stopTurning_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.stopTurning_Label)

        self.stopTurning_verticalLayout = QVBoxLayout()
        self.stopTurning_verticalLayout.setSpacing(0)
        self.stopTurning_verticalLayout.setObjectName(u"stopTurning_verticalLayout")
        self.flag127_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag127_label.setObjectName(u"flag127_label")
        self.flag127_label.setMaximumSize(QSize(16777215, 18))
        self.flag127_label.setFont(font)
        self.flag127_label.setFrameShape(QFrame.Box)
        self.flag127_label.setAlignment(Qt.AlignCenter)

        self.stopTurning_verticalLayout.addWidget(self.flag127_label)

        self.stopTurning_StateNumber0_Label = ColorChangingFrame(self.t2ss_Frame)
        self.stopTurning_StateNumber0_Label.setObjectName(u"stopTurning_StateNumber0_Label")
        self.stopTurning_StateNumber0_Label.setMaximumSize(QSize(16777215, 18))
        self.stopTurning_StateNumber0_Label.setFont(font)
        self.stopTurning_StateNumber0_Label.setFrameShape(QFrame.Box)
        self.stopTurning_StateNumber0_Label.setAlignment(Qt.AlignCenter)

        self.stopTurning_verticalLayout.addWidget(self.stopTurning_StateNumber0_Label)

        self.stopTurning_Flag1_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag1_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag1_horizontalLayout.setObjectName(u"stopTurning_Flag1_horizontalLayout")
        self.flag31_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag31_label.setObjectName(u"flag31_label")
        font1 = QFont()
        font1.setPointSize(6)
        font1.setBold(False)
        self.flag31_label.setFont(font1)
        self.flag31_label.setFrameShape(QFrame.Box)
        self.flag31_label.setAlignment(Qt.AlignCenter)
        self.flag31_label.setWordWrap(True)

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flag31_label)

        self.flag32_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag32_label.setObjectName(u"flag32_label")
        self.flag32_label.setFont(font1)
        self.flag32_label.setFrameShape(QFrame.Box)
        self.flag32_label.setAlignment(Qt.AlignCenter)
        self.flag32_label.setWordWrap(True)

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flag32_label)

        self.flag31_and_flag32_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flag31_and_flag32_lineEdit.setObjectName(u"flag31_and_flag32_lineEdit")
        self.flag31_and_flag32_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag31_and_flag32_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag31_and_flag32_lineEdit.setFont(font)
        self.flag31_and_flag32_lineEdit.setFrame(True)
        self.flag31_and_flag32_lineEdit.setAlignment(Qt.AlignCenter)

        self.stopTurning_Flag1_horizontalLayout.addWidget(self.flag31_and_flag32_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag1_horizontalLayout)

        self.stopTurning_Flag2_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag2_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag2_horizontalLayout.setObjectName(u"stopTurning_Flag2_horizontalLayout")
        self.flag33_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag33_label.setObjectName(u"flag33_label")
        self.flag33_label.setFont(font)
        self.flag33_label.setFrameShape(QFrame.Box)
        self.flag33_label.setAlignment(Qt.AlignCenter)
        self.flag33_label.setWordWrap(True)

        self.stopTurning_Flag2_horizontalLayout.addWidget(self.flag33_label)

        self.flag33_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flag33_lineEdit.setObjectName(u"flag33_lineEdit")
        self.flag33_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag33_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag33_lineEdit.setFont(font)
        self.flag33_lineEdit.setFrame(True)
        self.flag33_lineEdit.setAlignment(Qt.AlignCenter)

        self.stopTurning_Flag2_horizontalLayout.addWidget(self.flag33_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag2_horizontalLayout)

        self.or_stopTurning_Label = ColorChangingFrame(self.t2ss_Frame)
        self.or_stopTurning_Label.setObjectName(u"or_stopTurning_Label")
        self.or_stopTurning_Label.setMaximumSize(QSize(16777215, 18))
        self.or_stopTurning_Label.setFont(font)
        self.or_stopTurning_Label.setFrameShape(QFrame.Box)
        self.or_stopTurning_Label.setAlignment(Qt.AlignCenter)
        self.or_stopTurning_Label.setWordWrap(True)

        self.stopTurning_verticalLayout.addWidget(self.or_stopTurning_Label)

        self.stopTurning_Flag31_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag31_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag31_horizontalLayout.setObjectName(u"stopTurning_Flag31_horizontalLayout")
        self.flag34_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag34_label.setObjectName(u"flag34_label")
        self.flag34_label.setFont(font)
        self.flag34_label.setFrameShape(QFrame.Box)
        self.flag34_label.setAlignment(Qt.AlignCenter)
        self.flag34_label.setWordWrap(True)

        self.stopTurning_Flag31_horizontalLayout.addWidget(self.flag34_label)

        self.flag34_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flag34_lineEdit.setObjectName(u"flag34_lineEdit")
        self.flag34_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag34_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag34_lineEdit.setFont(font)
        self.flag34_lineEdit.setFrame(True)
        self.flag34_lineEdit.setAlignment(Qt.AlignCenter)

        self.stopTurning_Flag31_horizontalLayout.addWidget(self.flag34_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag31_horizontalLayout)

        self.stopTurning_Flag32_horizontalLayout = QHBoxLayout()
        self.stopTurning_Flag32_horizontalLayout.setSpacing(0)
        self.stopTurning_Flag32_horizontalLayout.setObjectName(u"stopTurning_Flag32_horizontalLayout")
        self.flag35_label = ColorChangingFrame(self.t2ss_Frame)
        self.flag35_label.setObjectName(u"flag35_label")
        self.flag35_label.setFont(font)
        self.flag35_label.setFrameShape(QFrame.Box)
        self.flag35_label.setAlignment(Qt.AlignCenter)
        self.flag35_label.setWordWrap(True)

        self.stopTurning_Flag32_horizontalLayout.addWidget(self.flag35_label)

        self.flag35_lineEdit = QLineEdit(self.t2ss_Frame)
        self.flag35_lineEdit.setObjectName(u"flag35_lineEdit")
        self.flag35_lineEdit.setMinimumSize(QSize(30, 50))
        self.flag35_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag35_lineEdit.setFont(font)
        self.flag35_lineEdit.setFrame(True)
        self.flag35_lineEdit.setAlignment(Qt.AlignCenter)

        self.stopTurning_Flag32_horizontalLayout.addWidget(self.flag35_lineEdit)


        self.stopTurning_verticalLayout.addLayout(self.stopTurning_Flag32_horizontalLayout)


        self.verticalLayout_22.addLayout(self.stopTurning_verticalLayout)


        self.horizontalLayout_53.addWidget(self.t2ss_Frame)


        self.verticalLayout_28.addWidget(self.turningTask_sub_Frame)


        self.horizontalLayout_7.addWidget(self.turningTask_Frame)

        self.frame_2 = QFrame(self.Main_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.flag112_label = ColorChangingFrame(self.frame_2)
        self.flag112_label.setObjectName(u"flag112_label")
        self.flag112_label.setMaximumSize(QSize(16777215, 18))
        self.flag112_label.setFont(font)
        self.flag112_label.setFrameShape(QFrame.Box)
        self.flag112_label.setAlignment(Qt.AlignCenter)
        self.flag112_label.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.flag112_label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Stopsd_or_Stopsq_Frame_2 = QFrame(self.frame_2)
        self.Stopsd_or_Stopsq_Frame_2.setObjectName(u"Stopsd_or_Stopsq_Frame_2")
        self.Stopsd_or_Stopsq_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.Stopsd_or_Stopsq_Frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Stopsd_or_Stopsq_Frame_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Stopsq_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.Stopsq_label.setObjectName(u"Stopsq_label")
        self.Stopsq_label.setMaximumSize(QSize(16777215, 18))
        self.Stopsq_label.setFont(font)
        self.Stopsq_label.setFrameShape(QFrame.Box)
        self.Stopsq_label.setAlignment(Qt.AlignCenter)
        self.Stopsq_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.Stopsq_label)

        self.flag129_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flag129_label.setObjectName(u"flag129_label")
        self.flag129_label.setMaximumSize(QSize(16777215, 18))
        self.flag129_label.setFont(font)
        self.flag129_label.setFrameShape(QFrame.Box)
        self.flag129_label.setAlignment(Qt.AlignCenter)
        self.flag129_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.flag129_label)

        self.sd_stateNumber0_Label_3 = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.sd_stateNumber0_Label_3.setObjectName(u"sd_stateNumber0_Label_3")
        self.sd_stateNumber0_Label_3.setMaximumSize(QSize(16777215, 18))
        self.sd_stateNumber0_Label_3.setFont(font)
        self.sd_stateNumber0_Label_3.setFrameShape(QFrame.Box)
        self.sd_stateNumber0_Label_3.setAlignment(Qt.AlignCenter)
        self.sd_stateNumber0_Label_3.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.sd_stateNumber0_Label_3)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3 = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flag31_horizontalLayout_3")
        self.flag16_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flag16_label.setObjectName(u"flag16_label")
        self.flag16_label.setFont(font)
        self.flag16_label.setFrameShape(QFrame.Box)
        self.flag16_label.setAlignment(Qt.AlignCenter)
        self.flag16_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.addWidget(self.flag16_label)

        self.flag16_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame_2)
        self.flag16_lineEdit.setObjectName(u"flag16_lineEdit")
        self.flag16_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag16_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag16_lineEdit.setFont(font)
        self.flag16_lineEdit.setFrame(True)
        self.flag16_lineEdit.setAlignment(Qt.AlignCenter)

        self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3.addWidget(self.flag16_lineEdit)


        self.verticalLayout_11.addLayout(self.Stopsd_or_Stopsq_Flag31_horizontalLayout_3)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3 = QHBoxLayout()
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3")
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3 = QVBoxLayout()
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.setSpacing(0)
        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.setObjectName(u"Stopsd_or_Stopsq_Flage32and33_verticalLayout_3")
        self.flag17_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flag17_label.setObjectName(u"flag17_label")
        self.flag17_label.setFont(font)
        self.flag17_label.setFrameShape(QFrame.Box)
        self.flag17_label.setAlignment(Qt.AlignCenter)
        self.flag17_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.addWidget(self.flag17_label)

        self.flag18_label = ColorChangingFrame(self.Stopsd_or_Stopsq_Frame_2)
        self.flag18_label.setObjectName(u"flag18_label")
        self.flag18_label.setFont(font)
        self.flag18_label.setFrameShape(QFrame.Box)
        self.flag18_label.setAlignment(Qt.AlignCenter)
        self.flag18_label.setWordWrap(True)

        self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3.addWidget(self.flag18_label)


        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.addLayout(self.Stopsd_or_Stopsq_Flage32and33_verticalLayout_3)

        self.flag17_and_flag18_lineEdit = QLineEdit(self.Stopsd_or_Stopsq_Frame_2)
        self.flag17_and_flag18_lineEdit.setObjectName(u"flag17_and_flag18_lineEdit")
        self.flag17_and_flag18_lineEdit.setMinimumSize(QSize(30, 25))
        self.flag17_and_flag18_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag17_and_flag18_lineEdit.setFont(font)
        self.flag17_and_flag18_lineEdit.setFrame(True)
        self.flag17_and_flag18_lineEdit.setAlignment(Qt.AlignCenter)

        self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3.addWidget(self.flag17_and_flag18_lineEdit)


        self.verticalLayout_11.addLayout(self.Stopsd_or_Stopsq_Flag32and33_horizontalLayout_3)


        self.horizontalLayout_13.addWidget(self.Stopsd_or_Stopsq_Frame_2)

        self.ss2sd_or_ss2sq_Frame_2 = QFrame(self.frame_2)
        self.ss2sd_or_ss2sq_Frame_2.setObjectName(u"ss2sd_or_ss2sq_Frame_2")
        self.ss2sd_or_ss2sq_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.ss2sd_or_ss2sq_Frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ss2sd_or_ss2sq_Frame_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ss2sd_or_ss2sq_Label_2 = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.ss2sd_or_ss2sq_Label_2.setObjectName(u"ss2sd_or_ss2sq_Label_2")
        self.ss2sd_or_ss2sq_Label_2.setMaximumSize(QSize(16777215, 18))
        self.ss2sd_or_ss2sq_Label_2.setFont(font)
        self.ss2sd_or_ss2sq_Label_2.setFrameShape(QFrame.Box)
        self.ss2sd_or_ss2sq_Label_2.setAlignment(Qt.AlignCenter)
        self.ss2sd_or_ss2sq_Label_2.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.ss2sd_or_ss2sq_Label_2)

        self.flag116_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag116_label.setObjectName(u"flag116_label")
        self.flag116_label.setMaximumSize(QSize(16777215, 18))
        self.flag116_label.setFont(font)
        self.flag116_label.setFrameShape(QFrame.Box)
        self.flag116_label.setAlignment(Qt.AlignCenter)
        self.flag116_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flag116_label)

        self.stateNumber4_or_10_Label_2 = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.stateNumber4_or_10_Label_2.setObjectName(u"stateNumber4_or_10_Label_2")
        self.stateNumber4_or_10_Label_2.setMaximumSize(QSize(16777215, 18))
        self.stateNumber4_or_10_Label_2.setFont(font)
        self.stateNumber4_or_10_Label_2.setFrameShape(QFrame.Box)
        self.stateNumber4_or_10_Label_2.setAlignment(Qt.AlignCenter)
        self.stateNumber4_or_10_Label_2.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.stateNumber4_or_10_Label_2)

        self.flag0_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag0_label.setObjectName(u"flag0_label")
        self.flag0_label.setMaximumSize(QSize(16777215, 18))
        self.flag0_label.setFont(font)
        self.flag0_label.setFrameShape(QFrame.Box)
        self.flag0_label.setAlignment(Qt.AlignCenter)
        self.flag0_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flag0_label)

        self.flag1_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag1_label.setObjectName(u"flag1_label")
        self.flag1_label.setMaximumSize(QSize(16777215, 18))
        self.flag1_label.setFont(font)
        self.flag1_label.setFrameShape(QFrame.Box)
        self.flag1_label.setAlignment(Qt.AlignCenter)
        self.flag1_label.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.flag1_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.flag2_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag2_label.setObjectName(u"flag2_label")
        self.flag2_label.setFont(font)
        self.flag2_label.setFrameShape(QFrame.Box)
        self.flag2_label.setAlignment(Qt.AlignCenter)
        self.flag2_label.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.flag2_label)

        self.flag2_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag2_lineEdit.setObjectName(u"flag2_lineEdit")
        self.flag2_lineEdit.setMinimumSize(QSize(30, 30))
        self.flag2_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag2_lineEdit.setFont(font)
        self.flag2_lineEdit.setFrame(True)
        self.flag2_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.flag2_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.flag3_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag3_label.setObjectName(u"flag3_label")
        self.flag3_label.setFont(font)
        self.flag3_label.setFrameShape(QFrame.Box)
        self.flag3_label.setAlignment(Qt.AlignCenter)
        self.flag3_label.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.flag3_label)

        self.flag4_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag4_label.setObjectName(u"flag4_label")
        self.flag4_label.setFont(font)
        self.flag4_label.setFrameShape(QFrame.Box)
        self.flag4_label.setAlignment(Qt.AlignCenter)
        self.flag4_label.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.flag4_label)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)

        self.flag3_and_flag4_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag3_and_flag4_lineEdit.setObjectName(u"flag3_and_flag4_lineEdit")
        self.flag3_and_flag4_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag3_and_flag4_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag3_and_flag4_lineEdit.setFont(font)
        self.flag3_and_flag4_lineEdit.setFrame(True)
        self.flag3_and_flag4_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.flag3_and_flag4_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.flag5_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag5_label.setObjectName(u"flag5_label")
        self.flag5_label.setFont(font)
        self.flag5_label.setFrameShape(QFrame.Box)
        self.flag5_label.setAlignment(Qt.AlignCenter)
        self.flag5_label.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.flag5_label)

        self.flag6_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag6_label.setObjectName(u"flag6_label")
        self.flag6_label.setFont(font)
        self.flag6_label.setFrameShape(QFrame.Box)
        self.flag6_label.setAlignment(Qt.AlignCenter)
        self.flag6_label.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.flag6_label)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.flag5_and_flag6_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag5_and_flag6_lineEdit.setObjectName(u"flag5_and_flag6_lineEdit")
        self.flag5_and_flag6_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag5_and_flag6_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag5_and_flag6_lineEdit.setFont(font)
        self.flag5_and_flag6_lineEdit.setFrame(True)
        self.flag5_and_flag6_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.flag5_and_flag6_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.flag7_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag7_label.setObjectName(u"flag7_label")
        self.flag7_label.setMaximumSize(QSize(16777215, 103))
        self.flag7_label.setFont(font)
        self.flag7_label.setFrameShape(QFrame.Box)
        self.flag7_label.setAlignment(Qt.AlignCenter)
        self.flag7_label.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.flag7_label)

        self.flag8_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag8_label.setObjectName(u"flag8_label")
        self.flag8_label.setMaximumSize(QSize(16777215, 103))
        self.flag8_label.setFont(font)
        self.flag8_label.setFrameShape(QFrame.Box)
        self.flag8_label.setAlignment(Qt.AlignCenter)
        self.flag8_label.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.flag8_label)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)

        self.flag7_and_flag8_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag7_and_flag8_lineEdit.setObjectName(u"flag7_and_flag8_lineEdit")
        self.flag7_and_flag8_lineEdit.setMinimumSize(QSize(30, 28))
        self.flag7_and_flag8_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag7_and_flag8_lineEdit.setFont(font)
        self.flag7_and_flag8_lineEdit.setFrame(True)
        self.flag7_and_flag8_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.flag7_and_flag8_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.flag9_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag9_label.setObjectName(u"flag9_label")
        self.flag9_label.setFont(font)
        self.flag9_label.setFrameShape(QFrame.Box)
        self.flag9_label.setAlignment(Qt.AlignCenter)
        self.flag9_label.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.flag9_label)

        self.flag9_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag9_lineEdit.setObjectName(u"flag9_lineEdit")
        self.flag9_lineEdit.setMinimumSize(QSize(30, 30))
        self.flag9_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag9_lineEdit.setFont(font)
        self.flag9_lineEdit.setFrame(True)
        self.flag9_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.flag9_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.flag10_label = ColorChangingFrame(self.ss2sd_or_ss2sq_Frame_2)
        self.flag10_label.setObjectName(u"flag10_label")
        self.flag10_label.setFont(font)
        self.flag10_label.setFrameShape(QFrame.Box)
        self.flag10_label.setAlignment(Qt.AlignCenter)
        self.flag10_label.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.flag10_label)

        self.flag10_lineEdit = QLineEdit(self.ss2sd_or_ss2sq_Frame_2)
        self.flag10_lineEdit.setObjectName(u"flag10_lineEdit")
        self.flag10_lineEdit.setMinimumSize(QSize(30, 30))
        self.flag10_lineEdit.setMaximumSize(QSize(30, 5000))
        self.flag10_lineEdit.setFont(font)
        self.flag10_lineEdit.setFrame(True)
        self.flag10_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.flag10_lineEdit)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_13.addWidget(self.ss2sd_or_ss2sq_Frame_2)

        self.SittingDown_or_Squat_Frame_2 = QFrame(self.frame_2)
        self.SittingDown_or_Squat_Frame_2.setObjectName(u"SittingDown_or_Squat_Frame_2")
        self.SittingDown_or_Squat_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.SittingDown_or_Squat_Frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.SittingDown_or_Squat_Frame_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.SittingDown_or_Squat_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.SittingDown_or_Squat_Label_3.setObjectName(u"SittingDown_or_Squat_Label_3")
        self.SittingDown_or_Squat_Label_3.setMaximumSize(QSize(16777215, 18))
        self.SittingDown_or_Squat_Label_3.setFont(font)
        self.SittingDown_or_Squat_Label_3.setFrameShape(QFrame.Box)
        self.SittingDown_or_Squat_Label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.SittingDown_or_Squat_Label_3)

        self.SittingDown_or_Squat_horizontalLayout_3 = QHBoxLayout()
        self.SittingDown_or_Squat_horizontalLayout_3.setSpacing(0)
        self.SittingDown_or_Squat_horizontalLayout_3.setObjectName(u"SittingDown_or_Squat_horizontalLayout_3")
        self.sdMiddle_or_sqMiddle_verticalLayout_3 = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_verticalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_verticalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_verticalLayout_3")
        self.flag115_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag115_label.setObjectName(u"flag115_label")
        self.flag115_label.setMaximumSize(QSize(16777215, 18))
        self.flag115_label.setFont(font)
        self.flag115_label.setFrameShape(QFrame.Box)
        self.flag115_label.setAlignment(Qt.AlignCenter)
        self.flag115_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout_3.addWidget(self.flag115_label)

        self.stateNumber_minus5_or_minus11_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.stateNumber_minus5_or_minus11_Label_3.setObjectName(u"stateNumber_minus5_or_minus11_Label_3")
        self.stateNumber_minus5_or_minus11_Label_3.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus5_or_minus11_Label_3.setFont(font)
        self.stateNumber_minus5_or_minus11_Label_3.setFrameShape(QFrame.Box)
        self.stateNumber_minus5_or_minus11_Label_3.setAlignment(Qt.AlignCenter)
        self.stateNumber_minus5_or_minus11_Label_3.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_verticalLayout_3.addWidget(self.stateNumber_minus5_or_minus11_Label_3)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3 = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3")
        self.flag11_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag11_label.setObjectName(u"flag11_label")
        self.flag11_label.setFont(font)
        self.flag11_label.setFrameShape(QFrame.Box)
        self.flag11_label.setAlignment(Qt.AlignCenter)
        self.flag11_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.addWidget(self.flag11_label)

        self.flag11_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame_2)
        self.flag11_lineEdit.setObjectName(u"flag11_lineEdit")
        self.flag11_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag11_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag11_lineEdit.setFont(font)
        self.flag11_lineEdit.setFrame(True)
        self.flag11_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3.addWidget(self.flag11_lineEdit)


        self.sdMiddle_or_sqMiddle_verticalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag11_horizontalLayout_3)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3 = QHBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3")
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3 = QVBoxLayout()
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.setSpacing(0)
        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.setObjectName(u"sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3")
        self.flag12_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag12_label.setObjectName(u"flag12_label")
        self.flag12_label.setFont(font)
        self.flag12_label.setFrameShape(QFrame.Box)
        self.flag12_label.setAlignment(Qt.AlignCenter)
        self.flag12_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.addWidget(self.flag12_label)

        self.flag13_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag13_label.setObjectName(u"flag13_label")
        self.flag13_label.setFont(font)
        self.flag13_label.setFrameShape(QFrame.Box)
        self.flag13_label.setAlignment(Qt.AlignCenter)
        self.flag13_label.setWordWrap(True)

        self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3.addWidget(self.flag13_label)


        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_verticalLayout_3)

        self.flag12_and_flag13_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame_2)
        self.flag12_and_flag13_lineEdit.setObjectName(u"flag12_and_flag13_lineEdit")
        self.flag12_and_flag13_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag12_and_flag13_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag12_and_flag13_lineEdit.setFont(font)
        self.flag12_and_flag13_lineEdit.setFrame(True)
        self.flag12_and_flag13_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3.addWidget(self.flag12_and_flag13_lineEdit)


        self.sdMiddle_or_sqMiddle_verticalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_Flag12and13_horizontalLayout_3)


        self.SittingDown_or_Squat_horizontalLayout_3.addLayout(self.sdMiddle_or_sqMiddle_verticalLayout_3)

        self.sdFinal_or_sqDeep_verticalLayout_3 = QVBoxLayout()
        self.sdFinal_or_sqDeep_verticalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_verticalLayout_3.setObjectName(u"sdFinal_or_sqDeep_verticalLayout_3")
        self.flag114_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag114_label.setObjectName(u"flag114_label")
        self.flag114_label.setMaximumSize(QSize(16777215, 18))
        self.flag114_label.setFont(font)
        self.flag114_label.setFrameShape(QFrame.Box)
        self.flag114_label.setAlignment(Qt.AlignCenter)
        self.flag114_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout_3.addWidget(self.flag114_label)

        self.stateNumber_minus6_or_minus12_Label_3 = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.stateNumber_minus6_or_minus12_Label_3.setObjectName(u"stateNumber_minus6_or_minus12_Label_3")
        self.stateNumber_minus6_or_minus12_Label_3.setMaximumSize(QSize(16777215, 18))
        self.stateNumber_minus6_or_minus12_Label_3.setFont(font)
        self.stateNumber_minus6_or_minus12_Label_3.setFrameShape(QFrame.Box)
        self.stateNumber_minus6_or_minus12_Label_3.setAlignment(Qt.AlignCenter)
        self.stateNumber_minus6_or_minus12_Label_3.setWordWrap(True)

        self.sdFinal_or_sqDeep_verticalLayout_3.addWidget(self.stateNumber_minus6_or_minus12_Label_3)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3 = QHBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3")
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3 = QVBoxLayout()
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.setSpacing(0)
        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.setObjectName(u"sdFinal_or_sqDeep_Flag1and2_verticalLayout_3")
        self.flag14_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag14_label.setObjectName(u"flag14_label")
        self.flag14_label.setFont(font)
        self.flag14_label.setFrameShape(QFrame.Box)
        self.flag14_label.setAlignment(Qt.AlignCenter)
        self.flag14_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.addWidget(self.flag14_label)

        self.flag15_label = ColorChangingFrame(self.SittingDown_or_Squat_Frame_2)
        self.flag15_label.setObjectName(u"flag15_label")
        self.flag15_label.setFont(font)
        self.flag15_label.setFrameShape(QFrame.Box)
        self.flag15_label.setAlignment(Qt.AlignCenter)
        self.flag15_label.setWordWrap(True)

        self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3.addWidget(self.flag15_label)


        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.addLayout(self.sdFinal_or_sqDeep_Flag1and2_verticalLayout_3)

        self.flag14_lineEdit = QLineEdit(self.SittingDown_or_Squat_Frame_2)
        self.flag14_lineEdit.setObjectName(u"flag14_lineEdit")
        self.flag14_lineEdit.setMinimumSize(QSize(28, 20))
        self.flag14_lineEdit.setMaximumSize(QSize(28, 5000))
        self.flag14_lineEdit.setFont(font)
        self.flag14_lineEdit.setFrame(True)
        self.flag14_lineEdit.setAlignment(Qt.AlignCenter)

        self.sdFinal_or_sqDeep_Flag1and2_horizontalLayout_3.addWidget(self.flag14_lineEdit)


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
        self.Buttons_Frame.setFrameShape(QFrame.NoFrame)
        self.Buttons_Frame.setFrameShadow(QFrame.Raised)
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

        self.Sit2Stand_and_Stand2Sit_Mode_label = QLabel(self.Buttons_Frame)
        self.Sit2Stand_and_Stand2Sit_Mode_label.setObjectName(u"Sit2Stand_and_Stand2Sit_Mode_label")
        self.Sit2Stand_and_Stand2Sit_Mode_label.setMinimumSize(QSize(200, 0))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setMaximumSize(QSize(16777215, 88000))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setStyleSheet(u"#Sit2Stand_and_Stand2Sit_Mode_label {\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"font-weight: bold; \n"
"}")
        self.Sit2Stand_and_Stand2Sit_Mode_label.setFrameShape(QFrame.Box)
        self.Sit2Stand_and_Stand2Sit_Mode_label.setAlignment(Qt.AlignCenter)

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


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.flag110_label.setText(QCoreApplication.translate("Form", u"Walking Task", None))
        self.StopWalking_label.setText(QCoreApplication.translate("Form", u"Stop Walking", None))
        self.flag126_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.stopWalking_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag68_label.setText(QCoreApplication.translate("Form", u"wStopCounterLim", None))
        self.flag68_lineEdit.setText(QCoreApplication.translate("Form", u"200", None))
        self.flag68_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"200", None))
        self.flag69_label.setText(QCoreApplication.translate("Form", u"|RH-LH|<=\n wStopHipth", None))
        self.flag69_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag69_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag70_label.setText(QCoreApplication.translate("Form", u"|RKA|< wStopKneeAngTh", None))
        self.flag71_label.setText(QCoreApplication.translate("Form", u"|LKA|< wStopKneeAngTh", None))
        self.flag70_and_flag71_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag70_and_flag71_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.ss2w_label.setText(QCoreApplication.translate("Form", u"ss2w", None))
        self.flag130_label.setText(QCoreApplication.translate("Form", u"Walking Start", None))
        self.stateNumber1_Label.setText(QCoreApplication.translate("Form", u"1", None))
        self.flag36_label.setText(QCoreApplication.translate("Form", u"RH > wStartHipTh", None))
        self.flag37_label.setText(QCoreApplication.translate("Form", u"|RH-LH|> wStartHipTh", None))
        self.flag36_and_flag37_lineEdit.setText(QCoreApplication.translate("Form", u"7.5", None))
        self.flag36_and_flag37_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"7.5", None))
        self.flag38_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ >= wStartTimuXTh", None))
        self.flag38_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag38_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag39_label.setText(QCoreApplication.translate("Form", u"walkingFlag", None))
        self.flag40_label.setText(QCoreApplication.translate("Form", u"turning Flag", None))
        self.flag41_label.setText(QCoreApplication.translate("Form", u"sitStandFlag ", None))
        self.flag42_label.setText(QCoreApplication.translate("Form", u" StandingStill", None))
        self.walking_w_label.setText(QCoreApplication.translate("Form", u"Walking (w)", None))
        self.flag131_label.setText(QCoreApplication.translate("Form", u"RLS", None))
        self.stateNumber2_label.setText(QCoreApplication.translate("Form", u"2", None))
        self.flag43_label.setText(QCoreApplication.translate("Form", u"RH<= wStartHipTh", None))
        self.flag43_ineEdit.setText(QCoreApplication.translate("Form", u"7.5", None))
        self.flag43_ineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"7.5", None))
        self.flag44_label.setText(QCoreApplication.translate("Form", u"RWZ <= rlsTimuTh", None))
        self.flag44_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag44_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag132_label.setText(QCoreApplication.translate("Form", u"RHS", None))
        self.stateNumber3_label.setText(QCoreApplication.translate("Form", u"3", None))
        self.flag45_label.setText(QCoreApplication.translate("Form", u"RWZ <= rlsTimuTh", None))
        self.flag45_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag45_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag46_label.setText(QCoreApplication.translate("Form", u"RH > rhsHTh", None))
        self.flag46_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag46_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag47_label.setText(QCoreApplication.translate("Form", u"RK LM in", None))
        self.flag48_label.setText(QCoreApplication.translate("Form", u"hsWS", None))
        self.flag47_and_flag48_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag47_and_flag48_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag133_label.setText(QCoreApplication.translate("Form", u"LHO2MF", None))
        self.stateNumber4_label.setText(QCoreApplication.translate("Form", u"4", None))
        self.flag49_label.setText(QCoreApplication.translate("Form", u"LWZ <= lhoTimuTh", None))
        self.flag49_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag49_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag134_label.setText(QCoreApplication.translate("Form", u"LF2ET", None))
        self.stateNumber5_label.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag50_label.setText(QCoreApplication.translate("Form", u"LKA <= lfAngLim", None))
        self.flag50_lineEdit.setText(QCoreApplication.translate("Form", u"-60", None))
        self.flag50_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-60", None))
        self.StandingStill_label_23.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flag51_label.setText(QCoreApplication.translate("Form", u"LKA > lfAngLim", None))
        self.flag51_lineEdit.setText(QCoreApplication.translate("Form", u"-60", None))
        self.flag51_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-60", None))
        self.flag52_label.setText(QCoreApplication.translate("Form", u"LKA <=  LHOKA+ lfMinAllowAng", None))
        self.flag52_lineEdit.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flag52_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-10", None))
        self.flag53_label.setText(QCoreApplication.translate("Form", u"LKV >= lf2etKneeVelTh", None))
        self.flag53_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag53_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag135_label.setText(QCoreApplication.translate("Form", u"Lextension", None))
        self.stateNumber6_label.setText(QCoreApplication.translate("Form", u"6", None))
        self.flag54_label.setText(QCoreApplication.translate("Form", u"LKV > lf2etKneeVelTh", None))
        self.flag54_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag54_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag136_label.setText(QCoreApplication.translate("Form", u"Lextended", None))
        self.stateNumber7_label.setText(QCoreApplication.translate("Form", u"7", None))
        self.flag55_label.setText(QCoreApplication.translate("Form", u"LKA >= leAngLim", None))
        self.flag55_lineEdit.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flag55_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-10", None))
        self.flag137_label.setText(QCoreApplication.translate("Form", u"LLS", None))
        self.stateNumber8_label.setText(QCoreApplication.translate("Form", u"8", None))
        self.flag56_label.setText(QCoreApplication.translate("Form", u"LWZ >= llsTimuTh", None))
        self.flag56_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag56_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag138_label.setText(QCoreApplication.translate("Form", u"LHS", None))
        self.stateNumber9_label.setText(QCoreApplication.translate("Form", u"9", None))
        self.flag57_label.setText(QCoreApplication.translate("Form", u"LWZ >= llsTimuTh", None))
        self.flag57_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag57_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag58_label.setText(QCoreApplication.translate("Form", u"LH >lhsHTh", None))
        self.flag58_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag58_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag59_label.setText(QCoreApplication.translate("Form", u"LK LM in ", None))
        self.flag60_label.setText(QCoreApplication.translate("Form", u"hsWS", None))
        self.flag59_and_flag60_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag59_and_flag60_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag139_label.setText(QCoreApplication.translate("Form", u"RHO2MF", None))
        self.stateNumber10_label.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag61_label.setText(QCoreApplication.translate("Form", u"RWZ >= rhoTimuTh", None))
        self.flag61_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag61_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag140_label.setText(QCoreApplication.translate("Form", u"RF2ET", None))
        self.stateNumber11_label.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag62_label.setText(QCoreApplication.translate("Form", u"RKA >= rfAngLim", None))
        self.flag62_lineEdit.setText(QCoreApplication.translate("Form", u"60", None))
        self.flag62_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"60", None))
        self.StandingStill_label_35.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flag63_label.setText(QCoreApplication.translate("Form", u"RKA < rfAngLim", None))
        self.flag63_lineEdit.setText(QCoreApplication.translate("Form", u"60", None))
        self.flag63_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"60", None))
        self.flag64_label.setText(QCoreApplication.translate("Form", u"RKA >= RHOKA + rfMinAllowAng", None))
        self.flag64_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag64_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag65_label.setText(QCoreApplication.translate("Form", u"RKV <= rf2etKneeVelTh", None))
        self.flag65_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag65_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag141_label.setText(QCoreApplication.translate("Form", u"Rextension", None))
        self.stateNumber12_label.setText(QCoreApplication.translate("Form", u"12", None))
        self.flag66_label.setText(QCoreApplication.translate("Form", u"RKV < rf2etKneeVelTh", None))
        self.flag66_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag66_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag142_label.setText(QCoreApplication.translate("Form", u"Rextended", None))
        self.stateNumber13_label.setText(QCoreApplication.translate("Form", u"13", None))
        self.flag67_label.setText(QCoreApplication.translate("Form", u"RKA <=  reAngLim", None))
        self.flag67_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag67_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag113_label.setText(QCoreApplication.translate("Form", u"Stand2Sit, Sit2Stand Task", None))
        self.Stopsd_or_Stopsq_Label.setText(QCoreApplication.translate("Form", u"Stop sd ", None))
        self.flag143_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.sd_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag105_label.setText(QCoreApplication.translate("Form", u"RH < sdStopHipTh", None))
        self.flag106_label.setText(QCoreApplication.translate("Form", u"LH < sdStopHipTh", None))
        self.flag105_and_flag106_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag105_and_flag106_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag107_label.setText(QCoreApplication.translate("Form", u"sdStopWS", None))
        self.flag107_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.flag107_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.flag108_label.setText(QCoreApplication.translate("Form", u"RKA < sdStopKneeAngTh", None))
        self.flag109_label.setText(QCoreApplication.translate("Form", u"|LKA| < sdStopKneeAngTh", None))
        self.flag108_and_flag109_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag108_and_flag109_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.ss2sd_Label.setText(QCoreApplication.translate("Form", u"ss2sd", None))
        self.flag122_label.setText(QCoreApplication.translate("Form", u"sd Start", None))
        self.stateNumber4_or_10_Label.setText(QCoreApplication.translate("Form", u"-4 ", None))
        self.flag72_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ <= sdStartTimuXTh", None))
        self.flag72_lineEdit.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flag72_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-10", None))
        self.flag73_label.setText(QCoreApplication.translate("Form", u"RKA>= sdStartKneeAngTh", None))
        self.flag74_label.setText(QCoreApplication.translate("Form", u"|LKA|>=sdStartKneeAngTh", None))
        self.flag73_and_flag74_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag73_and_flag74_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag75_label.setText(QCoreApplication.translate("Form", u"RKV > sdStartKneeVelTh", None))
        self.flag76_label.setText(QCoreApplication.translate("Form", u"LKV< sdStartKneeVelTh", None))
        self.flag75_and_flag76_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag75_and_flag76_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag77_label.setText(QCoreApplication.translate("Form", u"RH> sdStartHipTh", None))
        self.flag78_label.setText(QCoreApplication.translate("Form", u"LH> sdStartHipTh", None))
        self.flag77_and_flag78_lineEdit.setText(QCoreApplication.translate("Form", u"22", None))
        self.flag77_and_flag78_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"22", None))
        self.flag79_label.setText(QCoreApplication.translate("Form", u"walkingFlag", None))
        self.flag80_label.setText(QCoreApplication.translate("Form", u"turningFlag", None))
        self.flag81_label.setText(QCoreApplication.translate("Form", u"sitStandFlag", None))
        self.flag82_label.setText(QCoreApplication.translate("Form", u"StandingStill", None))
        self.flag83_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.flag83_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag83_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flag84_label.setText(QCoreApplication.translate("Form", u"BWX < sdStartBimuTh", None))
        self.flag84_lineEdit.setText(QCoreApplication.translate("Form", u"-5", None))
        self.flag84_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-5", None))
        self.SittingDown_or_Squat_Label.setText(QCoreApplication.translate("Form", u"Sitting Down (sd)", None))
        self.flag121_label.setText(QCoreApplication.translate("Form", u"sd Middle", None))
        self.stateNumber_minus5_or_minus11_Label.setText(QCoreApplication.translate("Form", u"-5", None))
        self.flag85_label.setText(QCoreApplication.translate("Form", u"stand2sitWs", None))
        self.flag85_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag85_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flag86_label.setText(QCoreApplication.translate("Form", u"RKA >= sdMiddleKneeAngTh", None))
        self.flag87_label.setText(QCoreApplication.translate("Form", u"|LKA|>= sdMiddleKneeAngTh", None))
        self.flag86_and_flag87_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag86_and_flag87_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag120_label.setText(QCoreApplication.translate("Form", u"sd Final", None))
        self.stateNumber_minus6_or_minus12_Label.setText(QCoreApplication.translate("Form", u"-6", None))
        self.flag88_label.setText(QCoreApplication.translate("Form", u"RKA > sdFinalKneeAngTh", None))
        self.flag89_label.setText(QCoreApplication.translate("Form", u"|LKA|> sdFinalKneeAngTh", None))
        self.flag88_and_flag89_lineEdit.setText(QCoreApplication.translate("Form", u"65", None))
        self.flag88_and_flag89_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"65", None))
        self.flag119_label.setText(QCoreApplication.translate("Form", u"Seated", None))
        self.stateNumber_minus7_Label.setText(QCoreApplication.translate("Form", u"-7", None))
        self.flag90_label.setText(QCoreApplication.translate("Form", u"seatedWS", None))
        self.flag90_lineEdit.setText(QCoreApplication.translate("Form", u"50", None))
        self.flag90_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"50", None))
        self.flag91_label.setText(QCoreApplication.translate("Form", u"|RWZ| < seatedTimuTh", None))
        self.flag92_label.setText(QCoreApplication.translate("Form", u"|LWZ| < seatedTimuTh", None))
        self.flag91_and_flag92_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag91_and_flag92_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.or_seated_Label.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flag93_label.setText(QCoreApplication.translate("Form", u"RKA >=  sdFinalKneeAngTh + seatedAddedKneeAng", None))
        self.flag94_label.setText(QCoreApplication.translate("Form", u"|LKA| >= sdFinalKneeAngTh + seatedAddedKneeAng", None))
        self.flag93_and_flag94_lineEdit.setText(QCoreApplication.translate("Form", u"15", None))
        self.flag93_and_flag94_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.flag118_label.setText(QCoreApplication.translate("Form", u"Seated2su", None))
        self.stateNumber_minus8_Label.setText(QCoreApplication.translate("Form", u"-8", None))
        self.flag95_label.setText(QCoreApplication.translate("Form", u"RKA > seated2suMinAllowKneeAng", None))
        self.flag96_label.setText(QCoreApplication.translate("Form", u"|LKA| > seated2suMinAllowKneeAng", None))
        self.flag95_and_flag96_lineEdit.setText(QCoreApplication.translate("Form", u"65", None))
        self.flag95_and_flag96_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"65", None))
        self.flag97_label.setText(QCoreApplication.translate("Form", u"seated2suWS", None))
        self.flag97_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag97_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flag98_label.setText(QCoreApplication.translate("Form", u"|BWX| < seated2suBimuTh", None))
        self.flag98_lineEdit.setText(QCoreApplication.translate("Form", u"-30", None))
        self.flag98_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-30", None))
        self.flag117_label.setText(QCoreApplication.translate("Form", u"StandingUp (su)", None))
        self.stateNumber_minus9_Label.setText(QCoreApplication.translate("Form", u"-9", None))
        self.flag99_label.setText(QCoreApplication.translate("Form", u"elapsedTime > timeRisePeak", None))
        self.flag99_lineEdit.setText(QCoreApplication.translate("Form", u"0.15", None))
        self.flag99_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.15", None))
        self.su2ss_Label.setText(QCoreApplication.translate("Form", u"su2ss", None))
        self.flag128_label.setText(QCoreApplication.translate("Form", u"StandingStill", None))
        self.su2ss_stateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag100_label.setText(QCoreApplication.translate("Form", u"RKA < su2ssKneeAngTh", None))
        self.flag101_label.setText(QCoreApplication.translate("Form", u"|LKA| < su2ssKneeAngTh", None))
        self.flag100_and_flag101_lineEdit.setText(QCoreApplication.translate("Form", u"15", None))
        self.flag100_and_flag101_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"15", None))
        self.flag102_label.setText(QCoreApplication.translate("Form", u"su2ssWS", None))
        self.flag102_lineEdit.setText(QCoreApplication.translate("Form", u"20", None))
        self.flag102_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"20", None))
        self.flag103_label.setText(QCoreApplication.translate("Form", u"|RKV| < su2ssKneeVelTh", None))
        self.flag104_label.setText(QCoreApplication.translate("Form", u"|LKV| < su2ssKneeVelTh", None))
        self.flag103_and_flag104_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag103_and_flag104_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag111_label.setText(QCoreApplication.translate("Form", u"Turning Task", None))
        self.ss2t_Label.setText(QCoreApplication.translate("Form", u"ss2t", None))
        self.flag125_label.setText(QCoreApplication.translate("Form", u"Turning Start", None))
        self.stateNumber_minus1_Label.setText(QCoreApplication.translate("Form", u"-1", None))
        self.flag19_label.setText(QCoreApplication.translate("Form", u"|RWY| > tStartTimuTh", None))
        self.flag20_label.setText(QCoreApplication.translate("Form", u"|LWY| > tStartTimuTh", None))
        self.flag19_and_flag20_lineEdit.setText(QCoreApplication.translate("Form", u"80", None))
        self.flag19_and_flag20_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"80", None))
        self.flag21_label.setText(QCoreApplication.translate("Form", u"|BWY| > tStartBimuTh", None))
        self.flag21_lineEdit.setText(QCoreApplication.translate("Form", u"40", None))
        self.flag21_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"40", None))
        self.flag22_label.setText(QCoreApplication.translate("Form", u"walkingFlag == False", None))
        self.flag23_label.setText(QCoreApplication.translate("Form", u"turningFlag == False", None))
        self.flag24_label.setText(QCoreApplication.translate("Form", u"sitStandFlag == False", None))
        self.flag25_label.setText(QCoreApplication.translate("Form", u"StandingStill", None))
        self.turning_Label.setText(QCoreApplication.translate("Form", u"Turning (t)", None))
        self.flag124_label.setText(QCoreApplication.translate("Form", u"Turning Middle", None))
        self.stateNumber_minus2_Label.setText(QCoreApplication.translate("Form", u"-2", None))
        self.flag26_label.setText(QCoreApplication.translate("Form", u"|RWY| > tMiddleTimuTh", None))
        self.flag27_label.setText(QCoreApplication.translate("Form", u"|LWY| > tMiddleTimuTh", None))
        self.flag26_and_flag27_lineEdit.setText(QCoreApplication.translate("Form", u"135", None))
        self.flag26_and_flag27_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"135", None))
        self.flag28_label.setText(QCoreApplication.translate("Form", u"|BWY| > tMiddleBimuTh", None))
        self.flag28_lineEdit.setText(QCoreApplication.translate("Form", u"70", None))
        self.flag28_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"70", None))
        self.flag123_label.setText(QCoreApplication.translate("Form", u"Turning Final", None))
        self.stateNumber_minus3_Label.setText(QCoreApplication.translate("Form", u"-3", None))
        self.flag29_label.setText(QCoreApplication.translate("Form", u"|RWY| > tFinalTimuTh", None))
        self.flag30_label.setText(QCoreApplication.translate("Form", u"|LWY| > tFinalTimuTh", None))
        self.flag29_and_flag30_lineEdit.setText(QCoreApplication.translate("Form", u"120", None))
        self.flag29_and_flag30_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"120", None))
        self.stopTurning_Label.setText(QCoreApplication.translate("Form", u"Stop Turning", None))
        self.flag127_label.setText(QCoreApplication.translate("Form", u"StandingStill(ss)", None))
        self.stopTurning_StateNumber0_Label.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag31_label.setText(QCoreApplication.translate("Form", u"|RWY| < tStopTimuTh", None))
        self.flag32_label.setText(QCoreApplication.translate("Form", u"|LWY| < tStopTimuTh", None))
        self.flag31_and_flag32_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag31_and_flag32_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag33_label.setText(QCoreApplication.translate("Form", u"|BWY| < tStopBimuTh", None))
        self.flag33_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag33_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.or_stopTurning_Label.setText(QCoreApplication.translate("Form", u"Or", None))
        self.flag34_label.setText(QCoreApplication.translate("Form", u"tWS", None))
        self.flag34_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.flag34_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.flag35_label.setText(QCoreApplication.translate("Form", u"|LWY| < tStopTimuTh", None))
        self.flag35_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.flag35_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"10", None))
        self.flag112_label.setText(QCoreApplication.translate("Form", u"Squat Task", None))
        self.Stopsq_label.setText(QCoreApplication.translate("Form", u"Stop sq", None))
        self.flag129_label.setText(QCoreApplication.translate("Form", u"StandingStill (ss)", None))
        self.sd_stateNumber0_Label_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag16_label.setText(QCoreApplication.translate("Form", u"sdStopWS", None))
        self.flag16_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.flag16_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.flag17_label.setText(QCoreApplication.translate("Form", u"RKA < sdStopKneeAngTh", None))
        self.flag18_label.setText(QCoreApplication.translate("Form", u"|LKA| < sdStopKneeAngTh", None))
        self.flag17_and_flag18_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag17_and_flag18_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.ss2sd_or_ss2sq_Label_2.setText(QCoreApplication.translate("Form", u"ss2sq", None))
        self.flag116_label.setText(QCoreApplication.translate("Form", u"Squat Start", None))
        self.stateNumber4_or_10_Label_2.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flag0_label.setText(QCoreApplication.translate("Form", u"Squat Flag", None))
        self.flag1_label.setText(QCoreApplication.translate("Form", u"standingstill", None))
        self.flag2_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ <= \n sdStartTimuXTh", None))
        self.flag2_lineEdit.setText(QCoreApplication.translate("Form", u"-10", None))
        self.flag2_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-10", None))
        self.flag3_label.setText(QCoreApplication.translate("Form", u"RKA>= sdStartKneeAngTh", None))
        self.flag4_label.setText(QCoreApplication.translate("Form", u"|LKA|>=sdStartKneeAngTh", None))
        self.flag3_and_flag4_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag3_and_flag4_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag5_label.setText(QCoreApplication.translate("Form", u"RKV > sdStartKneeVelTh", None))
        self.flag6_label.setText(QCoreApplication.translate("Form", u"LKV< sdStartKneeVelTh", None))
        self.flag5_and_flag6_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.flag5_and_flag6_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.flag7_label.setText(QCoreApplication.translate("Form", u"RH> sdStartHipTh", None))
        self.flag8_label.setText(QCoreApplication.translate("Form", u"LH> sdStartHipTh", None))
        self.flag7_and_flag8_lineEdit.setText(QCoreApplication.translate("Form", u"22", None))
        self.flag7_and_flag8_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"22", None))
        self.flag9_label.setText(QCoreApplication.translate("Form", u"stand2sitWS", None))
        self.flag9_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag9_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flag10_label.setText(QCoreApplication.translate("Form", u"RWZ*LWZ <= sdStartTimuXTh", None))
        self.flag10_lineEdit.setText(QCoreApplication.translate("Form", u"-5", None))
        self.flag10_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"-5", None))
        self.SittingDown_or_Squat_Label_3.setText(QCoreApplication.translate("Form", u"Squat (sq)", None))
        self.flag115_label.setText(QCoreApplication.translate("Form", u"sq Middle", None))
        self.stateNumber_minus5_or_minus11_Label_3.setText(QCoreApplication.translate("Form", u"-11", None))
        self.flag11_label.setText(QCoreApplication.translate("Form", u"stand2sitWs", None))
        self.flag11_lineEdit.setText(QCoreApplication.translate("Form", u"11", None))
        self.flag11_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"11", None))
        self.flag12_label.setText(QCoreApplication.translate("Form", u"RKA >= \n sdMiddle \n KneeAngTh", None))
        self.flag13_label.setText(QCoreApplication.translate("Form", u"|LKA|>= \n sdMiddle \n KneeAngTh", None))
        self.flag12_and_flag13_lineEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.flag12_and_flag13_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"5", None))
        self.flag114_label.setText(QCoreApplication.translate("Form", u"sq Deep", None))
        self.stateNumber_minus6_or_minus12_Label_3.setText(QCoreApplication.translate("Form", u"-12", None))
        self.flag14_label.setText(QCoreApplication.translate("Form", u"RKA > sdFinalKneeAngTh", None))
        self.flag15_label.setText(QCoreApplication.translate("Form", u"|LKA|> sdFinalKneeAngTh", None))
        self.flag14_lineEdit.setText(QCoreApplication.translate("Form", u"65", None))
        self.flag14_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"65", None))
        self.record_Button.setText("")
        self.Apply_Button.setText(QCoreApplication.translate("Form", u"Apply Advanced Parameters", None))
        self.Save_All_Parameters_Button.setText(QCoreApplication.translate("Form", u"Save All Parameters", None))
        self.Sit2Stand_and_Stand2Sit_Mode_label.setText(QCoreApplication.translate("Form", u"Sti2Stand and Stand2Sit", None))
        self.Reset_Button.setText(QCoreApplication.translate("Form", u"Reset Advanced Parameters", None))
    # retranslateUi



from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QSize # Import QSize for fixed size if needed


class ColorChangingFrame(QLabel): # Inherit directly from QLabel
    def __init__(self, *args, **kwargs):
        # Call the QLabel constructor with all arguments passed
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

