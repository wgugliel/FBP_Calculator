# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/william/Desktop/formula_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogFBP(object):
    def setupUi(self, DialogFBP):
        DialogFBP.setObjectName("DialogFBP")
        DialogFBP.resize(320, 264)
        self.gridLayout = QtWidgets.QGridLayout(DialogFBP)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(DialogFBP)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.lineEditSteps = QtWidgets.QLineEdit(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSteps.sizePolicy().hasHeightForWidth())
        self.lineEditSteps.setSizePolicy(sizePolicy)
        self.lineEditSteps.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEditSteps.setReadOnly(True)
        self.lineEditSteps.setObjectName("lineEditSteps")
        self.gridLayout.addWidget(self.lineEditSteps, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(DialogFBP)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.labelLoadingImage = QtWidgets.QLabel(DialogFBP)
        self.labelLoadingImage.setText("")
        self.labelLoadingImage.setObjectName("labelLoadingImage")
        self.gridLayout_2.addWidget(self.labelLoadingImage, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 2)
        self.lineEditSymbols = QtWidgets.QLineEdit(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSymbols.sizePolicy().hasHeightForWidth())
        self.lineEditSymbols.setSizePolicy(sizePolicy)
        self.lineEditSymbols.setReadOnly(True)
        self.lineEditSymbols.setObjectName("lineEditSymbols")
        self.gridLayout.addWidget(self.lineEditSymbols, 1, 0, 1, 1)
        self.labelSymbols = QtWidgets.QLabel(DialogFBP)
        self.labelSymbols.setObjectName("labelSymbols")
        self.gridLayout.addWidget(self.labelSymbols, 0, 0, 1, 1)
        self.labelSteps = QtWidgets.QLabel(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSteps.sizePolicy().hasHeightForWidth())
        self.labelSteps.setSizePolicy(sizePolicy)
        self.labelSteps.setMinimumSize(QtCore.QSize(50, 0))
        self.labelSteps.setObjectName("labelSteps")
        self.gridLayout.addWidget(self.labelSteps, 0, 1, 1, 1)
        self.textBrowserFormula = QtWidgets.QTextBrowser(DialogFBP)
        self.textBrowserFormula.setObjectName("textBrowserFormula")
        self.gridLayout.addWidget(self.textBrowserFormula, 4, 0, 1, 2)

        self.retranslateUi(DialogFBP)
        QtCore.QMetaObject.connectSlotsByName(DialogFBP)

    def retranslateUi(self, DialogFBP):
        _translate = QtCore.QCoreApplication.translate
        DialogFBP.setWindowTitle(_translate("DialogFBP", "Formula based predictor"))
        self.label.setText(_translate("DialogFBP", "Formula:"))
        self.labelSymbols.setText(_translate("DialogFBP", "Symbols:"))
        self.labelSteps.setText(_translate("DialogFBP", "Steps:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogFBP = QtWidgets.QDialog()
    ui = Ui_DialogFBP()
    ui.setupUi(DialogFBP)
    DialogFBP.show()
    sys.exit(app.exec_())

