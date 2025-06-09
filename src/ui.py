import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QTableWidget, QTableWidgetItem, \
    QHeaderView, QPushButton, QWidget, QVBoxLayout, QDialog, QFormLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

from src import Database

company_column = 0
position_column = 1
status_column = 2
date_column = 3
notes_column = 4

class MainWindow(QMainWindow):
    def __init__(self, database_string):
        super().__init__()
        self.database_string = database_string
        self.application_database = Database.Database(database_string)
        self.setWindowTitle('Application-Tracker')
        self.resize(900, 600)
        self.initUI()
        self.currentCompany = None
        self.currentField = None

    def initUI(self):
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create vertical layout
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Create Table
        self.createTable()

        # Create Button
        self.createButton()

    def getCurrentCompany(self, row, column):
        company = self.tableWidget.item(row, company_column)
        currentItem = self.tableWidget.horizontalHeaderItem(column)
        if company is not None and currentItem is not None:
            self.currentCompany = company.text()
            self.currentField = currentItem.text()

    def handle_cell_change(self, row, column):
        newField = self.tableWidget.item(row, column)
        if self.currentCompany and self.currentField is not None and self.currentField != newField.text():
            self.application_database.update_field(self.currentCompany, self.currentField, newField.text())

    def createTable(self):

        application_count = self.application_database.getApplicationCount()
        print(application_count)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(application_count)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Company", "Position", "Status", "Date Applied", "Notes", "Delete"])
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.initializeApplications()

        # Table Event Handlers
        self.tableWidget.cellClicked.connect(self.getCurrentCompany)
        self.tableWidget.cellChanged.connect(self.handle_cell_change)

        # Set Column Width
        self.tableWidget.setColumnWidth(company_column, 200)
        self.tableWidget.setColumnWidth(position_column, 300)
        self.tableWidget.setColumnWidth(status_column, 65)
        self.tableWidget.setColumnWidth(date_column, 95)
        self.tableWidget.setColumnWidth(notes_column, 100)
        self.tableWidget.setColumnWidth(5, 25)
        self.tableWidget.horizontalHeader().setSectionResizeMode(notes_column, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)

        # Add table widget to layout
        self.layout.addWidget(self.tableWidget)

    def createButton(self):
        button = QPushButton("Add")
        button.clicked.connect(self.open_add_application_window)
        self.layout.addWidget(button)

    def refresh_window(self):
        self.tableWidget.setRowCount(0)  # Clear rows
        self.initializeApplications()

    def initializeApplications(self):
        all_applications = self.application_database.get_all_applications()
        application_count = len(all_applications)
        self.tableWidget.setRowCount(application_count)

        row_index = 0

        for application in all_applications:
            company = application[1]
            position = application[2]
            status = application[3]
            date_applied = application[4]
            notes = application[5]

            self.tableWidget.setItem(row_index, company_column, QTableWidgetItem(company))  # Company
            self.tableWidget.setItem(row_index, position_column, QTableWidgetItem(position))  # Position
            self.tableWidget.setItem(row_index, status_column, QTableWidgetItem(status))  # Status
            self.tableWidget.setItem(row_index, date_column, QTableWidgetItem(date_applied))  # Date_Applied
            self.tableWidget.setItem(row_index, notes_column, QTableWidgetItem(notes))  # Notes

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, company_name=company: self.delete_application(company_name))
            self.tableWidget.setCellWidget(row_index, 5, delete_button)

            row_index += 1

    def open_add_application_window(self):
        dialog = AddApplicationDialog(self.database_string, self.application_database, self.refresh_window)
        dialog.exec_()

    def delete_application(self, company_name):
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete the application for {company_name}?",
            QMessageBox.No | QMessageBox.Yes,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.application_database.delete_application(company_name)
            self.refresh_window()


class AddApplicationDialog(QDialog):
    def __init__(self, database_string, application_database, refresh_window):
        super().__init__()
        self.database_string = database_string
        self.application_database = application_database
        self.refresh_window = refresh_window

        self.setWindowTitle("Add application")

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.company_input = QLineEdit()
        self.position_input = QLineEdit()
        self.status_input = QLineEdit()
        self.date_input = QLineEdit()
        self.notes_input = QLineEdit()

        self.form_layout.addRow("Company: ", self.company_input)
        self.form_layout.addRow("Position: ", self.position_input)
        self.form_layout.addRow("Status: ", self.status_input)
        self.form_layout.addRow("Date Applied: ", self.date_input)
        self.form_layout.addRow("Notes: ", self.notes_input)

        self.layout.addLayout(self.form_layout)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit_form(self):
        company_input = self.company_input.text()
        position_input = self.position_input.text()
        status_input = self.status_input.text()
        date_input = self.date_input.text()
        notes_input = self.notes_input.text()

        if not all([company_input, position_input, status_input, date_input]):
            QMessageBox.warning(self, "Error", "Please fill in all required fields")
        else:
            self.application_database.insert_application(company_input, position_input, status_input,
                                                         date_input, notes_input)
            self.refresh_window()

            self.accept()


def main(database_string):
    app = QApplication(sys.argv)
    window = MainWindow(database_string)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main("../database/internship_database.db")