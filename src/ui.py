import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QTableWidget, QTableWidgetItem, \
    QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Application-Tracker')
        self.resize(500, 500)

        self.createTable()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Company", "Position", "Status", "Date Applied", "Notes"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setCentralWidget(self.tableWidget)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()