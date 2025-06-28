from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QSizePolicy
)
from PyQt6.QtCore import Qt
import requests

API_URL = "http://localhost:5000/api/models"
HEALTH_URL = "http://localhost:5000/health"

class TopboxLan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(250)
        self.setMaximumHeight(300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("LAN Settings Panel")
        layout.addWidget(self.label)

        # Connect button
        self.connect_btn = QPushButton("Connect to LAN Server")
        self.connect_btn.clicked.connect(self.connect_server)
        layout.addWidget(self.connect_btn)

        # List of models/ports
        self.model_list = QListWidget()
        self.model_list.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.model_list)

        # Add port/model section
        add_layout = QHBoxLayout()
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.port_input.setMaximumWidth(60)
        add_layout.addWidget(self.port_input)
        self.model_input = QLineEdit()
        self.model_input.setPlaceholderText("Model name")
        self.model_input.setMaximumWidth(100)
        add_layout.addWidget(self.model_input)
        self.add_btn = QPushButton("Add/Assign")
        self.add_btn.setMaximumWidth(80)
        self.add_btn.clicked.connect(self.add_model)
        add_layout.addWidget(self.add_btn)
        layout.addLayout(add_layout)

        # Refresh button
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.setMaximumWidth(80)
        self.refresh_btn.clicked.connect(self.refresh_models)
        layout.addWidget(self.refresh_btn)

        # Unregister button
        self.remove_btn = QPushButton("Remove Selected")
        self.remove_btn.setMaximumWidth(120)
        self.remove_btn.clicked.connect(self.remove_selected_model)
        layout.addWidget(self.remove_btn)

        self.connected = False

    def connect_server(self):
        try:
            resp = requests.get(HEALTH_URL)
            if resp.status_code == 200:
                self.connected = True
                QMessageBox.information(self, "Connected", "Connected to LAN server.")
                self.refresh_models()
            else:
                QMessageBox.warning(self, "Connection Failed", "Could not connect to LAN server.")
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", str(e))

    def refresh_models(self):
        self.model_list.clear()
        if not self.connected:
            self.model_list.addItem("Not connected.")
            return
        try:
            resp = requests.get(API_URL)
            if resp.status_code == 200:
                models = resp.json()
                for name, info in models.items():
                    item = QListWidgetItem(f"{name} | Port: {info['port']} | Loaded: {info['loaded']}")
                    self.model_list.addItem(item)
            else:
                self.model_list.addItem("Error loading models")
        except Exception as e:
            self.model_list.addItem(f"API error: {e}")

    def add_model(self):
        model_name = self.model_input.text().strip()
        port = self.port_input.text().strip()
        if not model_name or not port:
            QMessageBox.warning(self, "Input Error", "Model name and port required.")
            return
        try:
            resp = requests.post(f"{API_URL}/register", json={"model_name": model_name, "port": int(port)})
            if resp.status_code == 200:
                QMessageBox.information(self, "Success", f"Model '{model_name}' assigned to port {port}.")
                self.refresh_models()
            else:
                QMessageBox.warning(self, "Error", resp.json().get('error', 'Unknown error'))
        except Exception as e:
            QMessageBox.critical(self, "API Error", str(e))

    def remove_selected_model(self):
        selected = self.model_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Selection Error", "No model selected.")
            return
        name = selected.text().split("|")[0].strip()
        try:
            resp = requests.post(f"{API_URL}/unregister", json={"model_name": name})
            if resp.status_code == 200:
                QMessageBox.information(self, "Success", f"Model '{name}' unregistered.")
                self.refresh_models()
            else:
                QMessageBox.warning(self, "Error", resp.json().get('error', 'Unknown error'))
        except Exception as e:
            QMessageBox.critical(self, "API Error", str(e))
