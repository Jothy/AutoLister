# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(394, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dateEditStart = QtGui.QDateEdit(self.groupBox)
        self.dateEditStart.setObjectName(_fromUtf8("dateEditStart"))
        self.horizontalLayout.addWidget(self.dateEditStart)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEditEnd = QtGui.QDateEdit(self.groupBox)
        self.dateEditEnd.setObjectName(_fromUtf8("dateEditEnd"))
        self.horizontalLayout_2.addWidget(self.dateEditEnd)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEditSrvName = QtGui.QLineEdit(self.groupBox)
        self.lineEditSrvName.setObjectName(_fromUtf8("lineEditSrvName"))
        self.horizontalLayout_4.addWidget(self.lineEditSrvName)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEditDgatePath = QtGui.QLineEdit(self.groupBox)
        self.lineEditDgatePath.setObjectName(_fromUtf8("lineEditDgatePath"))
        self.horizontalLayout_5.addWidget(self.lineEditDgatePath)
        self.pushButtonDgatePath = QtGui.QPushButton(self.groupBox)
        self.pushButtonDgatePath.setText(_fromUtf8(""))
        self.pushButtonDgatePath.setObjectName(_fromUtf8("pushButtonDgatePath"))
        self.horizontalLayout_5.addWidget(self.pushButtonDgatePath)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableWidgetPatLst = QtGui.QTableWidget(self.splitter)
        self.tableWidgetPatLst.setObjectName(_fromUtf8("tableWidgetPatLst"))
        self.tableWidgetPatLst.setColumnCount(3)
        self.tableWidgetPatLst.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetPatLst.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetPatLst.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetPatLst.setHorizontalHeaderItem(2, item)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButtonQuery = QtGui.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonQuery.setIcon(icon1)
        self.pushButtonQuery.setObjectName(_fromUtf8("pushButtonQuery"))
        self.horizontalLayout_6.addWidget(self.pushButtonQuery)
        spacerItem1 = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AutoLister", None))
        self.groupBox.setTitle(_translate("Dialog", "Settings (Ver 1.0)", None))
        self.label.setText(_translate("Dialog", "Study Start Date:", None))
        self.label_2.setText(_translate("Dialog", "Study End Date:", None))
        self.label_3.setText(_translate("Dialog", "Server:", None))
        self.lineEditSrvName.setText(_translate("Dialog", "ConquestMASTER", None))
        self.label_4.setText(_translate("Dialog", "Dgate path:", None))
        self.lineEditDgatePath.setText(_translate("Dialog", "D:\\dicomserverMaster", None))
        item = self.tableWidgetPatLst.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Sr.No", None))
        item = self.tableWidgetPatLst.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "StudyDate", None))
        item = self.tableWidgetPatLst.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "patient Name", None))
        self.pushButtonQuery.setText(_translate("Dialog", "Query", None))

import Resource_file_rc
