from PySide6.QtCore import QObject, Signal
import websocket
import json
import time

class WebsocketWorker(QObject):
    """
    این کلاس در یک ترد جداگانه اجرا می‌شود و تمام ارتباطات وب‌ساکت را مدیریت می‌کند.
    """
    connected = Signal()
    disconnected = Signal()
    error_occurred = Signal(str)
    data_received = Signal(dict)

    def __init__(self, url="ws://10.42.0.1:1383"):
        super().__init__()
        self.url = url
        self.ws = None
        self.is_running = False

    def connect(self):
        """
        متد اصلی برای اجرا در ترد. به سرور متصل شده و به پیام‌ها گوش می‌دهد.
        """
        self.is_running = True
        try:
            self.ws = websocket.create_connection(self.url)
            self.ws.send("Can you hear me?")
            self.connected.emit()

            while self.is_running:
                try:
                    message = self.ws.recv()
                    data = json.loads(message)
                    self.data_received.emit(data)
                except websocket.WebSocketConnectionClosedException:
                    print("Connection closed by server.")
                    self.is_running = False
                    break
                except json.JSONDecodeError:
                    print(f"Could not decode JSON from message: {message}")
                except Exception as e:
                    print(f"An error occurred while receiving data: {e}")
                    self.error_occurred.emit(str(e))
                    self.is_running = False
                    break
        except Exception as e:
            print(f"Failed to connect to WebSocket: {e}")
            self.error_occurred.emit(str(e))

        if self.ws:
            self.ws.close()
        self.disconnected.emit()
        print("Worker thread finished.")

    def send_message(self, message):
        """
        یک پیام JSON را به سرور وب‌ساکت ارسال می‌کند.
        """
        if self.ws and self.is_running:
            try:
                self.ws.send(json.dumps(message))
                print(f"Sent message: {message}")
            except Exception as e:
                print(f"Error sending message: {e}")
                self.error_occurred.emit(str(e))

    def stop(self):
        """
        حلقه دریافت پیام را متوقف کرده و اتصال را می‌بندد.
        """
        print("Stopping worker...")
        self.is_running = False
