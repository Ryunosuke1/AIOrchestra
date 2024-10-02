from flask import Flask
from flask_socketio import SocketIO

class RealtimeMonitoring:
    def __init__(self):
        self.socketio = SocketIO()
        self.app = Flask(__name__)

    def start_server(self):
        """
        Starts the real-time monitoring server.
        """
        self.socketio.run(self.app, debug=True)

    def stop_server(self):
        """
        Stops the real-time monitoring server.
        """
        self.socketio.stop()

    def emit_event(self, event_name: str, data: dict) -> None:
        """
        Emits an event to all connected clients.

        Args:
            event_name (str): The name of the event to emit.
            data (dict): The data to send with the event.
        """
        self.socketio.emit(event_name, data)
