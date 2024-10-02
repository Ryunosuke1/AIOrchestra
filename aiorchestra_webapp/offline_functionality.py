from flask import Flask
from flask_socketio import SocketIO

class OfflineFunctionality:
    def __init__(self):
        """
        Initializes the OfflineFunctionality with ServiceWorker.
        """
        self.service_worker = ServiceWorker()

    def register_service_worker(self) -> None:
        """
        Registers a service worker for offline functionality.
        """
        self.service_worker.register()

    def sync_offline_data(self) -> None:
        """
        Synchronizes data when the application comes online after being offline.
        """
        self.service_worker.sync()
