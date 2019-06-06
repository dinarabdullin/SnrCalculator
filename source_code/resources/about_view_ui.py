# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_view_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(379, 155)
        self.gridLayout = QtWidgets.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(AboutDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(AboutDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(AboutDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.label_3.setText(_translate("AboutDialog", "Author: Dinar Abdullin"))
        self.label_4.setText(_translate("AboutDialog", "E-mail: abdullin@pc.uni-bonn.de"))
        self.label_2.setText(_translate("AboutDialog", "Version: 1.0"))
        self.label_5.setText(_translate("AboutDialog", "(c) 2019 This program can be distributed under GNU General Public License."))
        self.label.setText(_translate("AboutDialog", "Signal/Noise Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutDialog = QtWidgets.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())

