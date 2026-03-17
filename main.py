import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui/janela1.ui", self)
        self.setWindowTitle("Aplicação PyQt6 mínima")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())