from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class CRUDForm(QWidget):
    def __init__(self):
        super().__init__()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        add_button = QPushButton('Add Record')
        add_button.clicked.connect(self.add_record)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel('Age:'))
        layout.addWidget(self.age_input)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def add_record(self):
        name = self.name_input.text()
        age = self.age_input.text()
        # Code to add the record to the data source

if __name__ == '__main__':
    app = QApplication([])
    form = CRUDForm()
    form.show()
    app.exec()
