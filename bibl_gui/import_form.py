# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_form.ui'
#
# Created: Tue Nov 16 19:56:44 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PyQt4 import QtCore, QtGui
class ImportDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("ImportForm")
        Dialog.resize(640, 352)
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)

        self.label_add = QtGui.QLabel(self.groupBox)
        self.label_add.setObjectName("label_add")
        self.gridLayout.addWidget(self.label_add, 5, 1, 1, 1)
        self.label_add.setText(QtGui.QApplication.translate("Dialog", "Импортировать в...", None, QtGui.QApplication.UnicodeUTF8))

        self.tableComboBox = QtGui.QComboBox(self.groupBox)
        self.tableComboBox.setObjectName("tableComboBox")
        self.gridLayout.addWidget(self.tableComboBox, 5, 2, 1, 1)

        self.lineSpinBox = QtGui.QSpinBox(self.groupBox)
        self.lineSpinBox.setObjectName("lineSpinBox")
        self.lineSpinBox.setMaximum(100000)
        self.gridLayout.addWidget(self.lineSpinBox, 4, 2, 1, 1)
        self.encComboBox = QtGui.QComboBox(self.groupBox)
        self.encComboBox.setObjectName("encComboBox")
        self.encComboBox.addItem("")
        self.encComboBox.addItem("")
        self.encComboBox.setEnabled(False)
        self.gridLayout.addWidget(self.encComboBox, 2, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 2)
        self.fileLineEdit = QtGui.QLineEdit(self.groupBox)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.gridLayout.addWidget(self.fileLineEdit, 1, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtGui.QTableView(self.groupBox_3)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 2, 0, 1, 4)
        self.colNameComboBox = QtGui.QComboBox(self.groupBox_3)
        self.colNameComboBox.setObjectName("colNameComboBox")
        self.gridLayout_3.addWidget(self.colNameComboBox, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.tabCheckBox.setObjectName("tabCheckBox")
        self.gridLayout_2.addWidget(self.tabCheckBox, 0, 0, 1, 1)
        self.commaCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.commaCheckBox.setObjectName("commaCheckBox")
        self.gridLayout_2.addWidget(self.commaCheckBox, 0, 1, 1, 1)
        self.otherCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.otherCheckBox.setObjectName("otherCheckBox")
        self.gridLayout_2.addWidget(self.otherCheckBox, 0, 2, 1, 1)
        self.semicolCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.semicolCheckBox.setObjectName("semicolCheckBox")
        self.gridLayout_2.addWidget(self.semicolCheckBox, 1, 0, 1, 1)
        self.spaceCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.spaceCheckBox.setObjectName("spaceCheckBox")
        self.gridLayout_2.addWidget(self.spaceCheckBox, 1, 1, 1, 1)
        self.otherLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.otherLineEdit.setObjectName("otherLineEdit")
        self.gridLayout_2.addWidget(self.otherLineEdit, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 3, 2, 1, 1)

        self.sepGroup = QtGui.QButtonGroup()
        self.sepGroup.addButton(self.tabCheckBox)
        self.sepGroup.addButton(self.semicolCheckBox)
        self.sepGroup.addButton(self.commaCheckBox)
        self.sepGroup.addButton(self.spaceCheckBox)
        self.sepGroup.addButton(self.otherCheckBox)
        
        self.semicolCheckBox.setChecked(True)

        self.sepGroup.setExclusive(True)

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.close)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Импорт", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Импорт", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Кодировка", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Со строки", None, QtGui.QApplication.UnicodeUTF8))
        self.encComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "UTF-8", None, QtGui.QApplication.UnicodeUTF8))
        self.encComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Win-1251", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Выбрать файл", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Поля", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Имя столбца", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Разделитель", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCheckBox.setText(QtGui.QApplication.translate("Dialog", "Табуляция", None, QtGui.QApplication.UnicodeUTF8))
        self.commaCheckBox.setText(QtGui.QApplication.translate("Dialog", "Запятая", None, QtGui.QApplication.UnicodeUTF8))
        self.otherCheckBox.setText(QtGui.QApplication.translate("Dialog", "Другие", None, QtGui.QApplication.UnicodeUTF8))
        self.semicolCheckBox.setText(QtGui.QApplication.translate("Dialog", "Точка с запятой", None, QtGui.QApplication.UnicodeUTF8))
        self.spaceCheckBox.setText(QtGui.QApplication.translate("Dialog", "Пробел", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Разделитель текста", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "\"", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "\'", None, QtGui.QApplication.UnicodeUTF8))
