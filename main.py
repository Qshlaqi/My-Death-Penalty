from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from frontpage import MySideBar
import sys
import re
from PySide6.QtCore import QSize, QRegularExpression, Qt, QTimer, QThread
from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
from PySide6.QtWidgets import QLabel, QMessageBox, QProgressDialog, QFormLayout, QDialogButtonBox
import json
from debug_page2 import ColorChangingFrame
from websocket_worker import WebsocketWorker

class CustomDialog(QDialog):
    # ... (CustomDialog class remains the same)
    def __init__(self, title="Enter Date and Time", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.time = QLineEdit()
        self.date = QLineEdit()
        form = QFormLayout()
        form.addRow("Date: ", self.date)
        form.addRow("Time: ", self.time)
        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(form)
        main_layout.addWidget(button)

    def get_values(self):
        if self.result() == QDialog.Accepted:
            return self.date.text().strip(), self.time.text().strip()
        return "", ""

class ClientGUI(MySideBar):
    def __init__(self):
        super().__init__()
        self.user_id = "Default"
        self.name = "User"
        self.Mode = None
        self.current_progress = 0
        self.progress_timer = QTimer()
        self.progress_timer.setInterval(50)
        self.time = "0"
        self.date = "0"

        # --- Throttling Setup ---
        self.latest_data = None
        self.ui_update_timer = QTimer(self)
        self.ui_update_timer.setInterval(33)  # Roughly 30 FPS
        self.ui_update_timer.timeout.connect(self.throttled_ui_update)
        self.ui_update_timer.start()
        # --- End Throttling Setup ---

        # --- Setup for Websocket Worker Thread ---
        self.thread = QThread()
        self.worker = WebsocketWorker()
        self.worker.moveToThread(self.thread)

        self.worker.connected.connect(self.on_connection_successful)
        self.worker.disconnected.connect(self.on_disconnection)
        self.worker.error_occurred.connect(self.on_connection_error)
        self.worker.data_received.connect(self.cache_received_data) # <-- Connect to caching slot

        self.thread.started.connect(self.worker.connect)

        self.Connect_Button.toggled.connect(self.start_connection)
        self.lunch_Button.toggled.connect(self.Motor_Button)

        # (All other button connections remain the same)
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
        self.page_debug_instance.Apply_Button.clicked.connect(self.apply_advanced_params)
        self.page_debug_instance.Save_All_Parameters_Button.clicked.connect(self.save_advanced_params)
        self.page_debug_instance.Reset_Button.clicked.connect(self.ResetAdvanceParams)
        self.page_robot_control_instance.Apply_PT_Parameters_Run_Button.clicked.connect(self.send_mode)

        self.flags = None
        self.ZPDuration = 10000 #ms
        self.Mode_label.setText("Not Ready")
        self.AdvanceLineEdits = self.page_debug_instance.findChildren(QLineEdit)
        self.AdvanceLineEdits = sorted(self.AdvanceLineEdits, key=self.extract_number_from_name)

        # Connect labels
        self.page_robot_control_instance.LeftFlexionLimitEdit.textChanged.connect(
            lambda txt: (
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
            if "flag" in frame.objectName().lower()
        ]
        self.filtered_frames = sorted(self.filtered_frames, key=self.extract_number_from_name)
        self.all_flags = self.findChildren(ColorChangingFrame)
        self.sensor_flags = [
            frame for frame in self.all_flags
            if "sensor" in frame.objectName().lower()
        ]

    def cache_received_data(self, data):
        """ Caches the latest data from the worker. """
        self.latest_data = data

    def throttled_ui_update(self):
        """ Updates the UI with the latest cached data at a fixed interval. """
        if self.latest_data is None:
            return

        data = self.latest_data
        self.latest_data = None  # Consume the data

        try:
            # Update sensor/debug flags which need high frequency updates
            if "sensors" in data:
                sensor_flags = data["sensors"]
                for i in range(len(sensor_flags)):
                    if i < len(self.sensor_flags):
                        self.sensor_flags[i].flag = sensor_flags[i]
                        self.sensor_flags[i].update_color()

            if "flags" in data:
                debug_flags = data["flags"]
                for i in range(len(debug_flags)):
                     if i < len(self.filtered_frames):
                        self.filtered_frames[i].flag = debug_flags[i]
                        self.filtered_frames[i].update_color()

            # Handle less frequent, event-based data
            if "action" in data:
                status = data.get("status", "Unknown")
                self.general_popup(status, data["action"])
                if data['action'] == "enable":
                    self.progress = QProgressDialog()
                    self.progress.setWindowTitle("Zero Positioning")
                    self.progress.setAutoClose(True)
                    self.progress.show()
                    self.progress.setLabelText("Do Not Move!")
                    self.progress_timer.timeout.connect(self.update_progressbar)
                    self.progress_timer.start()
                elif data['action'] == "show_all_user":
                    ids = data.get('user_ids', [0])
                    names = data.get("name", ['a'])
                    merged = "\n".join(f"{id_}\t{name}" for id_, name in zip(ids, names))
                    self.general_popup(merged, windowtitle="Patients List")
                elif data['action'] == "load_patient":
                    self.name = data["name"]
                    self.user_id = data["user_id"]
                    self.User_label.setText(f"{self.name} ({self.user_id})")
                elif data['action'] == "disable":
                    for i in self.sensor_flags:
                        i.flag = False
                        i.update_color()

            if "user_id" in data:
                self.user_id = data["user_id"]

            if "params" in data:
                params = [str(x) for x in data["params"]]
                for i in range(len(params)):
                    if i < len(self.AdvanceLineEdits):
                        self.AdvanceLineEdits[i].setText(params[i])

            if "pt_params" in data:
                pt_params = data["pt_params"]
                # ... pt_params update logic ...

        except Exception as e:
            print(f"Error processing throttled data: {e}")

    # (All other methods like start_connection, on_disconnection, general_send, etc., remain unchanged)
    def start_connection(self, checked):
        if checked:
            if not self.thread.isRunning():
                self.Mode_label.setText("Connecting...")
                self.Mode_label.setStyleSheet("color: yellow; font-weight: bold;")
                self.thread.start()
        else:
            if self.thread.isRunning():
                self.worker.stop()
                self.thread.quit()
                self.thread.wait()

    def on_connection_successful(self):
        self.Mode_label.setText("Connected")
        self.Mode_label.setStyleSheet("color: rgba(107, 245, 155, 1); font-weight: bold;")

    def on_disconnection(self):
        self.Mode_label.setText("Disconnected")
        self.Mode_label.setStyleSheet("color: red; font-weight: bold;")
        self.lunch_Button.setChecked(False)
        if self.thread.isRunning():
             self.thread.quit()
             self.thread.wait()

    def on_connection_error(self, error_message):
        self.Mode_label.setText("Error")
        self.Mode_label.setStyleSheet("color: red; font-weight: bold;")
        self.general_popup(f"Connection Error: {error_message}", "Error")
        self.Connect_Button.setChecked(False)

    def general_send(self, msg):
        """ Sends a message via the worker thread. """
        self.worker.send_message(msg)

    def Motor_Button(self, checked):
        if checked:
            if self.thread.isRunning():
                self.general_send({"action": "enable"})
                self.Mode_label.setText("Ready")
                self.Mode_label.setStyleSheet("color: rgba(107, 245, 155, 1); font-weight: bold;")
            else:
                self.general_popup("First you should connect to the robot", "Connection Required")
                self.lunch_Button.setChecked(False)
        else:
            if self.thread.isRunning():
                self.general_send({"action": "disable"})

    def Record(self, checked):
        if checked:
            dlg = CustomDialog()
            dlg.exec_()
            self.time, self.date = dlg.get_values()
            message = {"action": "start_record", "name": self.name, "user_id": self.user_id, "time": self.time, "date": self.date}
        else:
            message = {"action": "stop_record"}
        self.general_send(message)

    def send_mode(self):
        PtParams = None
        # ... (send_mode logic remains the same)
        if self.thread.isRunning():
            message = {"mode": self.Mode, "action": "assist", "PT Params": PtParams}
            self.general_send(message)
        else:
            self.general_popup("You are not connected", "Warning")

    def apply_advanced_params(self):
        AdvanceParams = [i.text() for i in self.AdvanceLineEdits]
        message = {"Advance Params": AdvanceParams, "action": "advanced_params"}
        self.general_send(message)

    def save_advanced_params(self):
        AdvanceParams = [i.text() for i in self.AdvanceLineEdits]
        message = {"Advance Params": AdvanceParams, "action": "save_advance_params"}
        self.general_send(message)

    def AutoButtonClick(self):
        self.Mode = "Auto"
        self.Mode_label.setText("Mode: Auto")
        self.general_send({"action": "initialize"})

    def SquatButtonClick(self):
        self.Mode = "Squat"
        self.Mode_label.setText("Mode: Squat")
        self.general_send({"action": "initialize"})

    def Sit2StandButtonClick(self):
        self.Mode = "Sit2Stand"
        self.Mode_label.setText("Mode: Sit2Stand")
        self.general_send({"action": "initialize"})

    def ZeroButtonClick(self):
        self.Mode = "Zero"
        self.Mode_label.setText("Mode: Zero")
        self.general_send({"action": "initialize"})

    def AddUser(self):
        message = {"action":"add_patient","user_id":self.page_robot_control_instance.user_ID_signup_lineEdit.text(),"name":self.page_robot_control_instance.Name_and_LastName_lineEdit.text(),
                   "gender":self.page_robot_control_instance.comboBox.currentText(),"age":self.page_robot_control_instance.Age_lineEdit.text(),
                   "height":self.page_robot_control_instance.Height_lineEdit.text(),"weight":self.page_robot_control_instance.Weight_lineEdit.text()}
        self.general_send(message)

    def LoadUser(self):
        self.user_id = self.page_robot_control_instance.user_ID_login_lineEdit.text()
        message = {"action":"load_patient","user_id":self.page_robot_control_instance.user_ID_login_lineEdit.text()}
        self.general_send(message)

    def ResetPTParams(self):
        message = {"action":"reset_pt_params","user_id":self.user_id}
        self.general_send(message)

    def SavePTParams(self):
        PtParams = {"lfAngLim":self.page_robot_control_instance.LeftFlexionLimitEdit.text()}
        message = {"action":"pt_params_save","PT Params" : PtParams,"user_id":self.user_id}
        self.general_send(message)

    def general_popup(self, text, windowtitle="Warning", icon=None):
        dialog = QDialog(self)
        dialog.setWindowTitle(windowtitle)
        layout = QVBoxLayout(dialog)
        label = QLabel(text)
        label.setWordWrap(True)
        layout.addWidget(label)
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(dialog.accept)
        layout.addWidget(ok_btn, alignment=Qt.AlignCenter)
        dialog.adjustSize()
        dialog.exec()

    def update_progressbar(self):
        self.current_progress += 100 / (self.ZPDuration // 50)
        self.progress.setValue(self.current_progress)
        if self.current_progress > 100:
            self.progress.close()
            self.progress_timer.stop()
            self.current_progress = 0

    def ShowAllUsers(self):
        self.general_send({"action": "show_all_user"})

    def ResetAdvanceParams(self):
        self.general_send({"action": "reset_advance_params"})

    def extract_number_from_name(self, frame):
        match = re.search(r'(\d+)', frame.objectName())
        if match:
            return int(match.group(1))
        return float('inf')

    def closeEvent(self, event):
        if self.thread.isRunning():
            self.worker.stop()
            self.thread.quit()
            self.thread.wait()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = ClientGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
