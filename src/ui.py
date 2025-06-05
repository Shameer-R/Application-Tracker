import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QTableWidget, QTableWidgetItem, \
    QHeaderView
from PyQt5.QtCore import Qt

from src import Database
application_database = Database.Database()

company_column = 0
position_column = 1
status_column = 2
date_column = 3
notes_column = 4

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Application-Tracker')
        self.resize(900, 600)
        self.createTable()
        self.tableWidget.cellClicked.connect(self.getCurrentCompany)
        self.tableWidget.cellChanged.connect(self.handle_cell_change)
        self.currentCompany = None
        self.currentField = None

    def getCurrentCompany(self, row, column):
        company = self.tableWidget.item(row, company_column)
        currentItem = self.tableWidget.horizontalHeaderItem(column)
        if company is not None and currentItem is not None:
            self.currentCompany = company.text()
            self.currentField = currentItem.text()

    def handle_cell_change(self, row, column):
        newField = self.tableWidget.item(row, column)
        if self.currentCompany and self.currentField is not None and self.currentField != newField.text():
            application_database.update_field(self.currentCompany, self.currentField, newField.text())


    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Company", "Position", "Status", "Date Applied", "Notes"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.tableWidget)
        self.initializeApplications()

        # Set Column Width
        self.tableWidget.setColumnWidth(company_column, 200)
        self.tableWidget.setColumnWidth(position_column, 300)
        self.tableWidget.setColumnWidth(status_column, 65)
        self.tableWidget.setColumnWidth(date_column, 95)
        self.tableWidget.setColumnWidth(notes_column, 100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(notes_column, QHeaderView.Stretch)

    def initializeApplications(self):
        all_applications = application_database.get_all_applications()

        row_index = 0

        for application in all_applications:
            company = application[1]
            position = application[2]
            status = application[3]
            date_applied = application[4]
            notes = application[5]

            self.tableWidget.setItem(row_index, company_column, QTableWidgetItem(company)) # Company
            self.tableWidget.setItem(row_index, position_column, QTableWidgetItem(position)) # Position
            self.tableWidget.setItem(row_index, status_column, QTableWidgetItem(status)) # Status
            self.tableWidget.setItem(row_index, date_column, QTableWidgetItem(date_applied)) # Date_Applied
            self.tableWidget.setItem(row_index, notes_column, QTableWidgetItem(notes)) # Notes

            row_index += 1


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
