# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'scoreboard.ui'

#

# Created by: PyQt5 UI code generator 5.14.2

#

# WARNING! All changes made in this file will be lost!





from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.resize(360, 244)

        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")

        self.label = QtWidgets.QLabel(Dialog)

        self.label.setGeometry(QtCore.QRect(80, 60, 201, 33))

        font = QtGui.QFont()

        font.setFamily("Arial")

        font.setPointSize(14)

        font.setBold(False)

        font.setItalic(False)

        font.setWeight(50)

        self.label.setFont(font)

        self.label.setStyleSheet("font: 14pt \"Arial\";")

        self.label.setObjectName("label")

        self.finalscore = QtWidgets.QLabel(Dialog)

        self.finalscore.setGeometry(QtCore.QRect(110, 120, 131, 41))

        font = QtGui.QFont()

        font.setFamily("Arial")

        font.setPointSize(18)

        font.setBold(False)

        font.setItalic(False)

        font.setWeight(50)

        self.finalscore.setFont(font)

        self.finalscore.setStyleSheet("color: rgb(50, 195, 0);\n"

                                      "\n"

                                      "font: 18pt \"Arial\";")

        self.finalscore.setAlignment(QtCore.Qt.AlignCenter)

        self.finalscore.setObjectName("finalscore")



        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.label.setText(_translate("Dialog", "Your Team Score :"))

        self.finalscore.setText(_translate("Dialog", "0"))





if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog()

    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec_())
