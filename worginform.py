# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worginform.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorginForm(object):
    def setupUi(self, WorginForm):
        WorginForm.setObjectName("WorginForm")
        WorginForm.resize(422, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/worginicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WorginForm.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(WorginForm)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(WorginForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.addressEdit = QtWidgets.QLineEdit(WorginForm)
        self.addressEdit.setObjectName("addressEdit")
        self.horizontalLayout.addWidget(self.addressEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(WorginForm)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.wordsList = QtWidgets.QListWidget(WorginForm)
        self.wordsList.setObjectName("wordsList")
        self.horizontalLayout_2.addWidget(self.wordsList)
        self.frame = QtWidgets.QFrame(WorginForm)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.removeBtn = QtWidgets.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeBtn.setIcon(icon1)
        self.removeBtn.setObjectName("removeBtn")
        self.verticalLayout.addWidget(self.removeBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(WorginForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.newWordEdit = QtWidgets.QLineEdit(WorginForm)
        self.newWordEdit.setObjectName("newWordEdit")
        self.horizontalLayout_3.addWidget(self.newWordEdit)
        self.addBtn = QtWidgets.QToolButton(WorginForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon2)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_3.addWidget(self.addBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(WorginForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(WorginForm)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.startBtn = QtWidgets.QPushButton(WorginForm)
        self.startBtn.setIcon(icon)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_4.addWidget(self.startBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.logOutput = QtWidgets.QTextBrowser(WorginForm)
        self.logOutput.setObjectName("logOutput")
        self.verticalLayout_2.addWidget(self.logOutput)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(WorginForm)
        self.addBtn.clicked.connect(self.somethingHappened)
        self.startBtn.clicked.connect(WorginForm.repaint)
        self.removeBtn.clicked.connect(WorginForm.repaint)
        QtCore.QMetaObject.connectSlotsByName(WorginForm)

    def retranslateUi(self, WorginForm):
        _translate = QtCore.QCoreApplication.translate
        WorginForm.setWindowTitle(_translate("WorginForm", "Worgin"))
        self.label.setText(_translate("WorginForm", "Address of The Target:"))
        self.label_2.setText(_translate("WorginForm", "Words List:"))
        self.removeBtn.setText(_translate("WorginForm", "..."))
        self.label_3.setText(_translate("WorginForm", "New Word:"))
        self.addBtn.setText(_translate("WorginForm", "..."))
        self.label_4.setText(_translate("WorginForm", "Logs:"))
        self.startBtn.setText(_translate("WorginForm", "Worgin"))

    def somethingHappened(self):
        print('Something happened')

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WorginForm = QtWidgets.QWidget()
    ui = Ui_WorginForm()
    ui.setupUi(WorginForm)
    WorginForm.show()
    sys.exit(app.exec_())
