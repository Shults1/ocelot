# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tune_panel_top.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_TunePanel_Top(object):
    def setupUi(self, Form_TunePanel_Top):
        Form_TunePanel_Top.setObjectName("Form_TunePanel_Top")
        Form_TunePanel_Top.resize(305, 91)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_TunePanel_Top.sizePolicy().hasHeightForWidth())
        Form_TunePanel_Top.setSizePolicy(sizePolicy)
        Form_TunePanel_Top.setMinimumSize(QtCore.QSize(285, 80))
        Form_TunePanel_Top.setMaximumSize(QtCore.QSize(400, 91))
        Form_TunePanel_Top.setAutoFillBackground(False)
        Form_TunePanel_Top.setStyleSheet(".QWidget {background-color: rgb(238, 238, 236); border-top: 1px solid rgb(255, 255, 255);}")
        Form_TunePanel_Top.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(Form_TunePanel_Top)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.check = QtWidgets.QCheckBox(Form_TunePanel_Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check.sizePolicy().hasHeightForWidth())
        self.check.setSizePolicy(sizePolicy)
        self.check.setMinimumSize(QtCore.QSize(120, 0))
        self.check.setAutoFillBackground(False)
        self.check.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.check.setText("")
        self.check.setObjectName("check")
        self.horizontalLayout_6.addWidget(self.check)
        self.label_f = QtWidgets.QLabel(Form_TunePanel_Top)
        self.label_f.setMinimumSize(QtCore.QSize(50, 0))
        self.label_f.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_f.setObjectName("label_f")
        self.horizontalLayout_6.addWidget(self.label_f)
        self.factor = QtWidgets.QLineEdit(Form_TunePanel_Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.factor.sizePolicy().hasHeightForWidth())
        self.factor.setSizePolicy(sizePolicy)
        self.factor.setMinimumSize(QtCore.QSize(0, 20))
        self.factor.setObjectName("factor")
        self.horizontalLayout_6.addWidget(self.factor)
        self.xbutton = QtWidgets.QPushButton(Form_TunePanel_Top)
        self.xbutton.setMaximumSize(QtCore.QSize(30, 30))
        self.xbutton.setObjectName("xbutton")
        self.horizontalLayout_6.addWidget(self.xbutton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_c = QtWidgets.QLabel(Form_TunePanel_Top)
        self.label_c.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_c.setObjectName("label_c")
        self.horizontalLayout_5.addWidget(self.label_c)
        self.curval = QtWidgets.QDoubleSpinBox(Form_TunePanel_Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curval.sizePolicy().hasHeightForWidth())
        self.curval.setSizePolicy(sizePolicy)
        self.curval.setMinimumSize(QtCore.QSize(90, 23))
        self.curval.setDecimals(6)
        self.curval.setMinimum(-1000000000000000.0)
        self.curval.setMaximum(1e+16)
        self.curval.setSingleStep(0.01)
        self.curval.setObjectName("curval")
        self.horizontalLayout_5.addWidget(self.curval)
        self.label_o = QtWidgets.QLabel(Form_TunePanel_Top)
        self.label_o.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_o.setObjectName("label_o")
        self.horizontalLayout_5.addWidget(self.label_o)
        self.oldval = QtWidgets.QLineEdit(Form_TunePanel_Top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldval.sizePolicy().hasHeightForWidth())
        self.oldval.setSizePolicy(sizePolicy)
        self.oldval.setMinimumSize(QtCore.QSize(70, 0))
        self.oldval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.oldval.setReadOnly(True)
        self.oldval.setObjectName("oldval")
        self.horizontalLayout_5.addWidget(self.oldval)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.retranslateUi(Form_TunePanel_Top)
        QtCore.QMetaObject.connectSlotsByName(Form_TunePanel_Top)

    def retranslateUi(self, Form_TunePanel_Top):
        _translate = QtCore.QCoreApplication.translate
        Form_TunePanel_Top.setWindowTitle(_translate("Form_TunePanel_Top", "Form"))
        self.label_f.setText(_translate("Form_TunePanel_Top", "factor:"))
        self.factor.setText(_translate("Form_TunePanel_Top", "0.01"))
        self.xbutton.setText(_translate("Form_TunePanel_Top", "x"))
        self.label_c.setText(_translate("Form_TunePanel_Top", "value:"))
        self.label_o.setText(_translate("Form_TunePanel_Top", "old value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_TunePanel_Top = QtWidgets.QWidget()
    ui = Ui_Form_TunePanel_Top()
    ui.setupUi(Form_TunePanel_Top)
    Form_TunePanel_Top.show()
    sys.exit(app.exec_())
