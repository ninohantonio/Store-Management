from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QVBoxLayout


class CardCommande(QWidget):
    def __init__(self, numero, parent=None):
        super().__init__(parent)

        # Création du cadre (carte)
        self.frame = QFrame(self)
        self.frame.setStyleSheet("border: 1px solid black; margin: 5px; border-radius: 10px;")

        # Ajouter un label avec un numéro unique
        self.label = QLabel(f"Carte {numero}", self.frame)


        # Ajouter tout dans un layout
        self.layout = QVBoxLayout(self.frame)
        self.layout.addWidget(self.label)


