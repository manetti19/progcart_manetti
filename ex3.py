from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
import sys
from PyQt6.QtWidgets import QPushButton

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Minha aplicação")

botao = QPushButton("Clique aqui")

msg = QMessageBox()
msg.setWindowTitle("Alerta")
msg.setText("Esta é uma mensagem de aviso.")
msg.setIcon(QMessageBox.Icon.Warning)
msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        


def ao_clicar():
    print("Botão clicado!")
    msg.exec()

botao.clicked.connect(ao_clicar)
janela.setLayout(QVBoxLayout())
janela.layout().addWidget(botao)
botao.show()
janela.show()



sys.exit(app.exec())
