# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogFBP(object):
    def setupUi(self, DialogFBP):
        DialogFBP.setObjectName("DialogFBP")
        DialogFBP.resize(380, 400)
        self.gridLayout = QtWidgets.QGridLayout(DialogFBP)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditSymbols = QtWidgets.QLineEdit(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSymbols.sizePolicy().hasHeightForWidth())
        self.lineEditSymbols.setSizePolicy(sizePolicy)
        self.lineEditSymbols.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEditSymbols.setReadOnly(True)
        self.lineEditSymbols.setObjectName("lineEditSymbols")
        self.gridLayout.addWidget(self.lineEditSymbols, 2, 0, 1, 1)
        self.textBrowserFormula = QtWidgets.QTextBrowser(DialogFBP)
        self.textBrowserFormula.setEnabled(False)
        self.textBrowserFormula.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textBrowserFormula.setObjectName("textBrowserFormula")
        self.gridLayout.addWidget(self.textBrowserFormula, 7, 0, 1, 2)
        self.labelSteps = QtWidgets.QLabel(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSteps.sizePolicy().hasHeightForWidth())
        self.labelSteps.setSizePolicy(sizePolicy)
        self.labelSteps.setMinimumSize(QtCore.QSize(50, 0))
        self.labelSteps.setObjectName("labelSteps")
        self.gridLayout.addWidget(self.labelSteps, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelLoadingImage = QtWidgets.QLabel(DialogFBP)
        self.labelLoadingImage.setText("")
        self.labelLoadingImage.setObjectName("labelLoadingImage")
        self.gridLayout_2.addWidget(self.labelLoadingImage, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.comboBoxFormulaType = QtWidgets.QComboBox(DialogFBP)
        self.comboBoxFormulaType.setEnabled(False)
        self.comboBoxFormulaType.setObjectName("comboBoxFormulaType")
        self.comboBoxFormulaType.addItem("")
        self.comboBoxFormulaType.addItem("")
        self.comboBoxFormulaType.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxFormulaType, 0, 1, 1, 1)
        self.labelComputing = QtWidgets.QLabel(DialogFBP)
        self.labelComputing.setObjectName("labelComputing")
        self.gridLayout_2.addWidget(self.labelComputing, 0, 3, 1, 1)
        self.toolButtonSave = QtWidgets.QToolButton(DialogFBP)
        self.toolButtonSave.setText("")
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.toolButtonSave.setIcon(icon)
        self.toolButtonSave.setIconSize(QtCore.QSize(18, 18))
        self.toolButtonSave.setAutoRaise(True)
        self.toolButtonSave.setObjectName("toolButtonSave")
        self.gridLayout_2.addWidget(self.toolButtonSave, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        self.labelSymbols = QtWidgets.QLabel(DialogFBP)
        self.labelSymbols.setObjectName("labelSymbols")
        self.gridLayout.addWidget(self.labelSymbols, 1, 0, 1, 1)
        self.lineEditSteps = QtWidgets.QLineEdit(DialogFBP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSteps.sizePolicy().hasHeightForWidth())
        self.lineEditSteps.setSizePolicy(sizePolicy)
        self.lineEditSteps.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEditSteps.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEditSteps.setReadOnly(True)
        self.lineEditSteps.setObjectName("lineEditSteps")
        self.gridLayout.addWidget(self.lineEditSteps, 2, 1, 1, 1)
        self.tableWidgetFormula = QtWidgets.QTableWidget(DialogFBP)
        self.tableWidgetFormula.setEnabled(False)
        self.tableWidgetFormula.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetFormula.setAlternatingRowColors(True)
        self.tableWidgetFormula.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetFormula.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetFormula.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetFormula.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetFormula.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetFormula.setWordWrap(False)
        self.tableWidgetFormula.setObjectName("tableWidgetFormula")
        self.tableWidgetFormula.setColumnCount(0)
        self.tableWidgetFormula.setRowCount(0)
        self.tableWidgetFormula.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetFormula.horizontalHeader().setDefaultSectionSize(0)
        self.tableWidgetFormula.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidgetFormula.verticalHeader().setVisible(False)
        self.tableWidgetFormula.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetFormula.verticalHeader().setMinimumSectionSize(0)
        self.gridLayout.addWidget(self.tableWidgetFormula, 9, 0, 1, 2)
        self.listFormula = QtWidgets.QListWidget(DialogFBP)
        self.listFormula.setEnabled(False)
        self.listFormula.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listFormula.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listFormula.setAlternatingRowColors(True)
        self.listFormula.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listFormula.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listFormula.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listFormula.setUniformItemSizes(False)
        self.listFormula.setObjectName("listFormula")
        self.gridLayout.addWidget(self.listFormula, 8, 0, 1, 2)
        self.line = QtWidgets.QFrame(DialogFBP)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.retranslateUi(DialogFBP)
        QtCore.QMetaObject.connectSlotsByName(DialogFBP)
        DialogFBP.setTabOrder(self.lineEditSymbols, self.lineEditSteps)

    def retranslateUi(self, DialogFBP):
        _translate = QtCore.QCoreApplication.translate
        DialogFBP.setWindowTitle(_translate("DialogFBP", " "))
        self.labelSteps.setText(_translate("DialogFBP", "Steps:"))
        self.comboBoxFormulaType.setItemText(0, _translate("DialogFBP", "Formula"))
        self.comboBoxFormulaType.setItemText(1, _translate("DialogFBP", "List"))
        self.comboBoxFormulaType.setItemText(2, _translate("DialogFBP", "Table"))
        self.labelComputing.setText(_translate("DialogFBP", "Computing"))
        self.labelSymbols.setText(_translate("DialogFBP", "Symbols:"))

from fbp_calculator import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogFBP = QtWidgets.QDialog()
    ui = Ui_DialogFBP()
    ui.setupUi(DialogFBP)
    DialogFBP.show()
    sys.exit(app.exec_())

