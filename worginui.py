from PyQt5 import QtWidgets

from worginform import Ui_WorginForm

import worgin

import sys

class WorginUi(QtWidgets.QWidget):
    def __init__(self):
        super(WorginUi, self).__init__()
        self.ui = Ui_WorginForm()

        self.ui.setupUi(self)

        self.ui.addBtn.clicked.connect(self.addWoIToList)
        self.ui.removeBtn.clicked.connect(self.removeWoIFromList)
        self.ui.startBtn.clicked.connect(self.startWorgin)

    def addWoIToList(self):
        self.ui.wordsList.addItem(self.ui.newWordEdit.text())
        self.ui.newWordEdit.clear()

    def removeWoIFromList(self):
        self.ui.wordsList.takeItem(self.ui.wordsList.currentIndex().row())

    def startWorgin(self):
        if self.ui.wordsList.count() == 0:
            print('no words of interest selected')
            return
        
        if self.ui.addressEdit.text() == '':
            print('no target address selected')
            return

        worgin.worging(self.ui.addressEdit.text(), self.ui.wordsList.item(0).text())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    w = WorginUi()
    w.show()

    sys.exit(app.exec())