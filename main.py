from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from frontpage import MySideBar
import sys
import re
from PySide6.QtCore import QSize, QRegularExpression, Qt,QTimer

from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
from PySide6.QtWidgets import QLabel ,QMessageBox, QProgressDialog, QFormLayout, QDialogButtonBox
import time
import asyncio
from websockets.asyncio.client import connect
import json
import qasync
from debug_page2 import ColorChangingFrame

class CustomDialog(QDialog):
    def __init__(self, title = "Enter Date and Time",parent = None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.time = QLineEdit()
        self.date = QLineEdit()
        form = QFormLayout()
        form.addRow("Date: ",self.date)
        form.addRow("Time: ", self.time)
        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(form)
        main_layout.addWidget(button)

    def get_values(self):
        if self.result() == QDialog.Accepted:
            print([self.date.text(),self.time.text()])
            return self.date.text().strip(), self.time.text().strip()
        return "",""
        

class ClientGUI(MySideBar):
    def __init__(self):
        super().__init__()
        self.user_id = "Default"
        self.name = "User"
        # Handle Clicks
        self.Mode = None
        self.current_progress = 0
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.time = "0"
        self.date = "0"

        self.Connect_Button.toggled.connect(self.start_connection)
        self.lunch_Button.toggled.connect(self.Motor_Button)
        # self.lunch_Button.clicked.connect(self.Motor_Button)
        # Robot Control Page Buttons
        self.page_robot_control_instance.SavePT_Parameters_Button.clicked.connect(self.SavePTParams)
        self.page_robot_control_instance.Reset_PT_Parameters_Button.clicked.connect(self.ResetPTParams)
        self.page_robot_control_instance.add_user_Button.clicked.connect(self.AddUser)
        self.page_robot_control_instance.Sign_In_Button.clicked.connect(self.LoadUser)
        self.page_robot_control_instance.pushButton.clicked.connect(self.ShowAllUsers)
        self.page_robot_control_instance.Automatic_Mode_Button.clicked.connect(self.AutoButtonClick)
        self.page_robot_control_instance.Squat_Mode_Button.clicked.connect(self.SquatButtonClick)
        self.page_robot_control_instance.Stand2Sit_and_Sit2Stand_Mode_Button.clicked.connect(self.Sit2StandButtonClick)
        self.page_robot_control_instance.zeroTorque_Mode_Button.clicked.connect(self.ZeroButtonClick)
        self.page_robot_control_instance.record_Button.toggled.connect(self.Record)
        # Debug Page Buttons
        self.page_debug_instance.Apply_Button.clicked.connect(self.apply_advanced_params)
        self.page_debug_instance.Save_All_Parameters_Button.clicked.connect(self.save_advanced_params)
        self.page_debug_instance.Reset_Button.clicked.connect(self.ResetAdvanceParams)
        self.page_robot_control_instance.Apply_PT_Parameters_Run_Button.clicked.connect(self.send_mode)
        self.websocket = None
        self.flags = None
        self.ZPDuration = 10000 #ms
        self.Mode_label.setText("Not Ready")
        self.AdvanceLineEdits = self.page_debug_instance.findChildren(QLineEdit)
        self.AdvanceLineEdits = sorted(self.AdvanceLineEdits, key = self.extract_number_from_name)
        # for j,i in enumerate(self.AdvanceLineEdits):
        #     print(i.objectName())
        #     print(j)
        
        # Connect labels
        self.page_robot_control_instance.LeftFlexionLimitEdit.textChanged.connect(
            lambda txt:(
                self.page_debug_instance.label_2.setText(txt),
                self.page_debug_instance.label_3.setText(txt)
            )
        )
        self.page_robot_control_instance.RightFlexionLimitEdit.textChanged.connect(
            lambda txt:(
                self.page_debug_instance.label_9.setText(txt),
                self.page_debug_instance.label_10.setText(txt)
            )
        )
        self.page_robot_control_instance.LeftFlexionMinimumEdit.textChanged.connect(
            lambda txt:self.page_debug_instance.label_4.setText(txt)
        )
        self.page_robot_control_instance.RightFlexionMinimumEdit.textChanged.connect(
            lambda txt:self.page_debug_instance.label_11.setText(txt)
        )
        self.page_robot_control_instance.LeftExtensionAngleLimit.textChanged.connect(
            lambda txt:self.page_debug_instance.label_6.setText(txt)
        )
        self.page_robot_control_instance.RightExtensionAngleLimit.textChanged.connect(
            lambda txt:self.page_debug_instance.label_13.setText(txt)
        )
        self.flags = self.page_debug_instance.findChildren(ColorChangingFrame)
        self.flags = sorted(self.flags, key=lambda lbl: lbl.objectName())
        self.filtered_frames = [
            frame for frame in self.flags
            if "flag" in frame.objectName().lower() # .lower() makes the check case-insensitive
        ]
        self.filtered_frames = sorted(self.filtered_frames, key=self.extract_number_from_name)
        # for f in self.findChildren(ColorChangingFrame):
        #     print(f.objectName())
        self.all_flags = self.findChildren(ColorChangingFrame)
        self.sensor_flags = [
            frame for frame in self.all_flags
            if "sensor" in frame.objectName().lower() # .lower() makes the check case-insensitive
        ]
        print(len(self.sensor_flags))

        

    async def Connect_to_Server(self, checked):
        if checked:
            try:
                # self.websocket = await connect ("ws://localhost:8765")
                self.websocket = await connect ("ws://10.42.0.1:1383")
                self.Mode_label.setText("Connected")
                self.Mode_label.setStyleSheet("color: rgba(107, 245, 155, 1);font-weight:bold;")
                await self.websocket.send("Can you hear me?")
                asyncio.create_task(self.listen())


            except Exception as e:
                print(e)
                self.websocket = None
        else:
                message = json.dumps({"action":"disable"})
                await self.websocket.send(message)
                self.Mode_label.setText("Disconnected")
                self.Mode_label.setStyleSheet("color : red;font-weight: bold;")
                self.lunch_Button.setChecked(False)
                await self.websocket.close()
                


                
    async def listen(self):
        try:
            async for message in self.websocket:
                try: 
                    data = json.loads(message)
                    if "sensors" in data:
                        sensor_flags = data["sensors"]
                        for i in range(len(sensor_flags)):
                            self.sensor_flags[i].flag = sensor_flags[i]
                            self.sensor_flags[i].update_color()
                            # print(sensor_flags[i])
                    if "flags" in data:
                        debug_flags = data["flags"]
                        for i in range(len(debug_flags)):
                            self.filtered_frames[i].flag = debug_flags[i]
                            self.filtered_frames[i].update_color()
                    if "action" in data:
                        print(data)
                        status = data.get("status","Unknown")
                        self.general_popup(status,data["action"])
                        if data['action'] == "enable":
                            self.progress = QProgressDialog()
                            self.progress.setWindowTitle("Zero Positioning")
                            self.progress.setAutoClose(True)
                            self.progress.show()
                            self.progress.setLabelText("Do Not Move!")
                            self.timer.timeout.connect(self.update_progressbar)
                            self.timer.start()
                        elif data['action'] == "show_all_user":
                            print(data)
                            ids = data.get('user_ids',[0])
                            names = data.get("name",['a'])
                            merged = "\n".join(f"{id_}\t{name}" for id_, name in zip(ids, names))
                            self.general_popup(merged,windowtitle="Patients List")
                        elif data['action'] == "load_patient":
                            self.name = data["name"]
                            self.user_id = data["user_id"]
                            self.User_label.setText(self.name + "(" + self.user_id + ")")
                        elif data['action'] == "disable":
                            for i in self.sensor_flags:
                                i.flag = False
                                i.update_color()

                        
                            
                    if "user_id" in data:
                        self.user_id = data["user_id"]

                    if "params" in data:
                        params = data["params"]
                        params = [str(x) for x in params]
                        for i in range(len(params)):
                            self.AdvanceLineEdits[i].setText(params[i])
                    if "pt_params" in data:
                        pt_params = data["pt_params"]
                        print(pt_params)
                        self.page_robot_control_instance.LeftFlexionLimitEdit.setText(str(pt_params.get("lfAngLim",0)))
                        self.page_robot_control_instance.RightFlexionLimitEdit.setText(str(pt_params.get("rfAngLim",0)))
                        self.page_robot_control_instance.LeftExtensionAngleLimit.setText(str(pt_params.get("leAngLim",0)))
                        self.page_robot_control_instance.RightExtensionAngleLimit.setText(str(pt_params.get("reAngLim",0)))
                        self.page_robot_control_instance.LeftFlexionMinimumEdit.setText(str(pt_params.get("lfMinAllowAng",0)))
                        self.page_robot_control_instance.RightFlexionMinimumEdit.setText(str(pt_params.get("rfMinAllowAng",0)))
                        self.page_robot_control_instance.ThighLenghtEdit.setText(str(pt_params.get("thighLen",0)))
                        self.page_robot_control_instance.ShankLenghtEdit.setText(str(pt_params.get("shankLen",0)))
                        self.page_robot_control_instance.AutoAssistWeightEdit.setText(str(pt_params.get("assist_weight",0)))
                        self.page_robot_control_instance.RightFlexionMaximumEdit.setText(str(pt_params.get("rfMaxTorque",0)))
                        self.page_robot_control_instance.RightFlexionKEdit.setText(str(pt_params.get("rfK",0)))
                        self.page_robot_control_instance.LeftFlexionMaxEdit.setText(str(pt_params.get("lfMaxTorque",0)))
                        self.page_robot_control_instance.LeftFlexionKEdit.setText(str(pt_params.get("lfK",0)))
                        self.page_robot_control_instance.RightExtensionMaxEdit.setText(str(pt_params.get("reMaxTorque",0)))
                        self.page_robot_control_instance.RightExtensionKEdit.setText(str(pt_params.get("reK",0)))
                        self.page_robot_control_instance.LeftExtensionKEdit.setText(str(pt_params.get("leK",0)))
                        self.page_robot_control_instance.RightEccentricMaxEdit.setText(str(pt_params.get("wREccMaxTorque",0)))
                        self.page_robot_control_instance.RightEccentricKEdit.setText(str(pt_params.get("wREccK",0)))
                        self.page_robot_control_instance.LeftEccentricMaxEdit.setText(str(pt_params.get("wLEccMaxTorque",99)))
                        self.page_robot_control_instance.LeftEccentricKEdit.setText(str(pt_params.get("wLEccK",99)))
                        self.page_robot_control_instance.LeftExtensionMaxEdit.setText(str(pt_params.get("leMaxTorque",99)))
                        self.page_robot_control_instance.WalkingSSMaxEdit.setText(str(pt_params.get("ssEccMaxTorque",0)))
                        self.page_robot_control_instance.s2s_ssEccK_lineEdit.setText(str(pt_params.get("ssEccK",0)))
                        self.page_robot_control_instance.SquatAssistWeightEdit.setText(str(pt_params.get("assist_weight",0)))
                        self.page_robot_control_instance.WalkingSSEccKEdit.setText(str(pt_params.get("ssEccK",0)))



                except Exception as e:
                    print(e)
                    print(f'Message recived: {message}')

        except Exception as e:
            print("Connection closed")
            # self.ui.Status_Label.setText("disconnected")
            self.websocket = None

    def start_connection(self,checked):
        asyncio.ensure_future(self.Connect_to_Server(checked))

    def Motor_Button(self,checked):
        if checked:
            if self.websocket:
                asyncio.ensure_future(self.general_send({"action": "enable"}))
                self.Mode_label.setText("Ready")
                self.Mode_label.setStyleSheet("color: rgba(107, 245, 155, 1); font-weight: bold;")
            else:
                self.general_popup("First you should connect to the robot", "Connection Required")
                self.lunch_Button.setChecked(False)
        else:
            if self.websocket:
                asyncio.ensure_future(self.general_send({"action":"disable"}))

    def Record(self,checked):
        if checked:
            dlg = CustomDialog()
            dlg.exec_()
            self.time, self.date = dlg.get_values()
            message = {"action":"start_record","name":self.name,"user_id":self.user_id,"time":self.time,"date":self.date}
            
        else:
            message = {"action":"stop_record"}
        asyncio.ensure_future(self.general_send(message))


    def send_mode(self):
        if self.Mode == "Squat":
            PtParams = {"assit_weight":self.page_robot_control_instance.SquatAssistWeightEdit.text(),"ssEccMaxTorque":self.page_robot_control_instance.sq_ssEccMaxTorque_lineEdit.text(),
                        "ssEccK":self.page_robot_control_instance.sq_ssEccK_lineEdit.text()}
            
        elif self.Mode == "Sit2Stand":
             PtParams = {"assit_weight":self.page_robot_control_instance.auto_assistweight_lineEdit.text(),"ssEccMaxTorque":self.page_robot_control_instance.s2s_ssEccMaxTorque_lineEdit.text(),
                        "ssEccK":self.page_robot_control_instance.s2s_ssEccK_lineEdit.text()}         
        elif self.Mode == "Auto":
            PtParams = {"lfAngLim":self.page_robot_control_instance.LeftFlexionLimitEdit.text(),"rfAngLim":self.page_robot_control_instance.RightFlexionLimitEdit.text(),
                        "leAngLim":self.page_robot_control_instance.LeftExtensionAngleLimit.text(),"reAngLim":self.page_robot_control_instance.RightExtensionAngleLimit.text(),
                        "lfMinAllowAng":self.page_robot_control_instance.LeftFlexionMinimumEdit.text(),"rfMinAllowAng":self.page_robot_control_instance.RightFlexionMinimumEdit.text(),
                        "thighLen":self.page_robot_control_instance.ShankLenghtEdit.text(),"shankLen":self.page_robot_control_instance.ThighLenghtEdit.text(),
                        "assit_weight":self.page_robot_control_instance.AutoAssistWeightEdit.text(),"rfMaxTorque":self.page_robot_control_instance.RightFlexionMaximumEdit.text(),
                        "rfK":self.page_robot_control_instance.RightFlexionKEdit.text(),"lfMaxTorque":self.page_robot_control_instance.LeftFlexionMaxEdit.text(),
                        "lfK":self.page_robot_control_instance.RightFlexionKEdit.text(),"reMaxTorque":self.page_robot_control_instance.RightExtensionMaxEdit.text(),
                        "reK":self.page_robot_control_instance.RightExtensionKEdit.text(),"leMaxTorque":self.page_robot_control_instance.RightExtensionMaxEdit.text(),
                        "leK":self.page_robot_control_instance.RightExtensionKEdit.text(),"wREccMaxTorque":self.page_robot_control_instance.RightEccentricMaxEdit.text(),
                        "wREccK":self.page_robot_control_instance.RightEccentricKEdit.text(),"wLEccMaxTorque":self.page_robot_control_instance.LeftEccentricMaxEdit.text(),
                        "wLEccK":self.page_robot_control_instance.LeftEccentricKEdit.text(),"ssEccMaxTorque":self.page_robot_control_instance.WalkingSSMaxEdit.text(),
                        "ssEccK":self.page_robot_control_instance.WalkingSSEccKEdit.text()}
        else:
            PtParams = None  
        if self.websocket:
            message = {"mode":self.Mode,"action":"assist","PT Params":PtParams}
            asyncio.ensure_future(self.general_send(message))
        else:
            popup = QMessageBox()
            popup.setWindowTitle("Warning")
            popup.setFixedSize(QSize(400, 200))
            popup.setText("You are not connected")
            popup.setStandardButtons(QMessageBox.StandardButton.Ok)
            popup.exec()

    def apply_advanced_params(self):
        AdvanceParams = list()
        for i in self.AdvanceLineEdits:
            AdvanceParams.append(i.text())

        print(AdvanceParams)
        message = {"Advance Params": AdvanceParams,"action":"advanced_params"}
        asyncio.ensure_future(self.general_send(message))

    def save_advanced_params(self):
        AdvanceParams = list()
        for i in self.AdvanceLineEdits:
            AdvanceParams.append(i.text())
        message = {"Advance Params": AdvanceParams,"action":"save_advance_params"}
        asyncio.ensure_future(self.general_send(message))       

    def AutoButtonClick(self):
        self.Mode = "Auto"
        self.Mode_label.setText("Mode: Auto")  
        asyncio.ensure_future(self.general_send({"action":"initialize"}))

    def SquatButtonClick(self):
        self.Mode = "Squat"
        self.Mode_label.setText("Mode: Squat")
        asyncio.ensure_future(self.general_send({"action": "initialize"}))

    def Sit2StandButtonClick(self):
        self.Mode = "Sit2Stand"
        self.Mode_label.setText("Mode: Sit2Stand")
        asyncio.ensure_future(self.general_send({"action": "initialize"}))

    def ZeroButtonClick(self):
        self.Mode = "Zero"
        self.Mode_label.setText("Mode: Zero")
        asyncio.ensure_future(self.general_send({"action": "initialize"}))

    def AddUser(self):
        message = {"action":"add_patient","user_id":self.page_robot_control_instance.user_ID_signup_lineEdit.text(),"name":self.page_robot_control_instance.Name_and_LastName_lineEdit.text(),
                   "gender":self.page_robot_control_instance.comboBox.currentText(),"age":self.page_robot_control_instance.Age_lineEdit.text(),
                   "height":self.page_robot_control_instance.Height_lineEdit.text(),"weight":self.page_robot_control_instance.Weight_lineEdit.text()}
        asyncio.ensure_future(self.general_send(message))

    def LoadUser(self):
        self.user_id = self.page_robot_control_instance.user_ID_login_lineEdit.text()
        message = {"action":"load_patient","user_id":self.page_robot_control_instance.user_ID_login_lineEdit.text()}
        asyncio.ensure_future(self.general_send(message))

    def ResetPTParams(self):
        message = {"action":"reset_pt_params","user_id":self.user_id}
        asyncio.ensure_future(self.general_send(message))



    def SavePTParams(self):
        PtParams = {"lfAngLim":self.page_robot_control_instance.LeftFlexionLimitEdit.text(),"rfAngLim":self.page_robot_control_instance.RightFlexionLimitEdit.text(),
            "leAngLim":self.page_robot_control_instance.LeftExtensionAngleLimit.text(),"reAngLim":self.page_robot_control_instance.RightExtensionAngleLimit.text(),
            "lfMinAllowAng":self.page_robot_control_instance.LeftFlexionMinimumEdit.text(),"rfMinAllowAng":self.page_robot_control_instance.RightFlexionMinimumEdit.text(),
            "thighLen":self.page_robot_control_instance.ShankLenghtEdit.text(),"shankLen":self.page_robot_control_instance.ThighLenghtEdit.text(),
            "assit_weight":self.page_robot_control_instance.AutoAssistWeightEdit.text(),"rfMaxTorque":self.page_robot_control_instance.RightFlexionMaximumEdit.text(),
            "rfK":self.page_robot_control_instance.RightFlexionKEdit.text(),"lfMaxTorque":self.page_robot_control_instance.LeftFlexionMaxEdit.text(),
            "lfK":self.page_robot_control_instance.LeftFlexionKEdit.text(),"reMaxTorque":self.page_robot_control_instance.RightExtensionMaxEdit.text(),
            "reK":self.page_robot_control_instance.RightExtensionKEdit.text(),"leMaxTorque":self.page_robot_control_instance.LeftExtensionMaxEdit.text(),
            "leK":self.page_robot_control_instance.LeftExtensionKEdit.text(),"wREccMaxTorque":self.page_robot_control_instance.RightEccentricMaxEdit.text(),
            "wREccK":self.page_robot_control_instance.RightEccentricKEdit.text(),"wLEccMaxTorque":self.page_robot_control_instance.LeftEccentricMaxEdit.text(),
            "wLEccK":self.page_robot_control_instance.LeftEccentricKEdit.text(),"ssEccMaxTorque":self.page_robot_control_instance.WalkingSSMaxEdit.text(),
            "ssEccK":self.page_robot_control_instance.WalkingSSEccKEdit.text(),
            "ssEccMaxTorque":self.page_robot_control_instance.WalkingSSMaxEdit.text()}
        message = {"action":"pt_params_save","PT Params" : PtParams,"user_id":self.user_id}
        asyncio.ensure_future(self.general_send(message))


    async def Initialize(self):
        msg = json.dumps({"action":"initialize"})
        await self.websocket.send(msg)

    async def general_send(self,msg):
        await self.websocket.send(json.dumps(msg))
        print(msg)

    def general_popup(self, text, windowtitle="Warning", icon=None):
        dialog = QDialog(self)  # parent optional
        dialog.setWindowTitle(windowtitle)

        # Layout
        layout = QVBoxLayout(dialog)

        # Text label with word wrapping
        label = QLabel(text)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(label)

        # OK button
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(dialog.accept)
        layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

        # Force resize based on text AFTER widgets are added
        dialog.adjustSize()

        # Optional: Add padding to make dialog slightly bigger
        dialog.resize(dialog.width() + 20, dialog.height() + 20)

        dialog.exec()


    def check_button(self):

        self.progress = QProgressDialog()
        self.progress.setWindowTitle("Zero Positioning")
        self.progress.setAutoClose(True)
        self.progress.setLabelText("Do Not Move!")
        self.progress.show()
        self.timer.timeout.connect(self.update_progressbar)
        self.timer.start()
    def extract_number_from_name(self,frame):
        match = re.search(r'(\d+)', frame.objectName()) # Find one or more digits
        if match:
            return int(match.group(1)) # Convert the found digits to an integer
        return float('inf')
    
    def update_progressbar(self):
        self.current_progress += 100/(self.ZPDuration//50)
        self.progress.setValue(self.current_progress)
        if(self.current_progress >100):
            self.progress.close()
            self.timer.stop()
            self.current_progress = 0

    def ShowAllUsers(self):
        asyncio.ensure_future(self.general_send({"action":"show_all_user"}))

    def ResetAdvanceParams(self):
        asyncio.ensure_future(self.general_send({"action":"reset_advance_params"}))
def main():
    app = QApplication(sys.argv)
    # Set up qasync to integrate asyncio with Qt
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = ClientGUI()
    window.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()