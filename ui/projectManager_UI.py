# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ozgur/maya/scripts/oy-maya-scripts/oyTools/oyProjectManager/ui/projectManager.ui'
#
# Created: Thu Oct  8 15:15:41 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(481, 328)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.servers_label = QtGui.QLabel(self.horizontalWidget)
        self.servers_label.setMinimumSize(QtCore.QSize(118, 0))
        self.servers_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.servers_label.setObjectName("servers_label")
        self.horizontalLayout_13.addWidget(self.servers_label)
        self.servers_comboBox = QtGui.QComboBox(self.horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.servers_comboBox.sizePolicy().hasHeightForWidth())
        self.servers_comboBox.setSizePolicy(sizePolicy)
        self.servers_comboBox.setObjectName("servers_comboBox")
        self.horizontalLayout_13.addWidget(self.servers_comboBox)
        self.verticalLayout_5.addWidget(self.horizontalWidget)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.createProjectTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.createProjectTab.sizePolicy().hasHeightForWidth())
        self.createProjectTab.setSizePolicy(sizePolicy)
        self.createProjectTab.setObjectName("createProjectTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.createProjectTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalWidget = QtGui.QWidget(self.createProjectTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget1 = QtGui.QWidget(self.verticalWidget)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setMargin(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridWidget = QtGui.QWidget(self.horizontalWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout.setMargin(6)
        self.gridLayout.setObjectName("gridLayout")
        self.project_label1 = QtGui.QLabel(self.gridWidget)
        self.project_label1.setMinimumSize(QtCore.QSize(100, 0))
        self.project_label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label1.setObjectName("project_label1")
        self.gridLayout.addWidget(self.project_label1, 0, 0, 1, 1)
        self.project_lineEdit1 = QtGui.QLineEdit(self.gridWidget)
        self.project_lineEdit1.setObjectName("project_lineEdit1")
        self.gridLayout.addWidget(self.project_lineEdit1, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget)
        self.verticalLayout.addWidget(self.horizontalWidget1)
        self.horizontalWidget2 = QtGui.QWidget(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget2.setSizePolicy(sizePolicy)
        self.horizontalWidget2.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalWidget2.setObjectName("horizontalWidget2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.createProject_pushButton = QtGui.QPushButton(self.horizontalWidget2)
        self.createProject_pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.createProject_pushButton.setObjectName("createProject_pushButton")
        self.horizontalLayout_6.addWidget(self.createProject_pushButton)
        self.verticalLayout.addWidget(self.horizontalWidget2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.verticalWidget)
        self.tabWidget.addTab(self.createProjectTab, "")
        self.createSequenceTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.createSequenceTab.sizePolicy().hasHeightForWidth())
        self.createSequenceTab.setSizePolicy(sizePolicy)
        self.createSequenceTab.setObjectName("createSequenceTab")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.createSequenceTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalWidget_2 = QtGui.QWidget(self.createSequenceTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalWidget_2 = QtGui.QWidget(self.verticalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridWidget_2 = QtGui.QWidget(self.horizontalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.gridWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.project_label2 = QtGui.QLabel(self.gridWidget_2)
        self.project_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label2.setObjectName("project_label2")
        self.gridLayout_3.addWidget(self.project_label2, 0, 0, 1, 1)
        self.project_comboBox2 = QtGui.QComboBox(self.gridWidget_2)
        self.project_comboBox2.setObjectName("project_comboBox2")
        self.gridLayout_3.addWidget(self.project_comboBox2, 0, 1, 1, 1)
        self.sequence_label2 = QtGui.QLabel(self.gridWidget_2)
        self.sequence_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_label2.setObjectName("sequence_label2")
        self.gridLayout_3.addWidget(self.sequence_label2, 1, 0, 1, 1)
        self.sequence_lineEdit2 = QtGui.QLineEdit(self.gridWidget_2)
        self.sequence_lineEdit2.setObjectName("sequence_lineEdit2")
        self.gridLayout_3.addWidget(self.sequence_lineEdit2, 1, 1, 1, 1)
        self.shotRange_label2 = QtGui.QLabel(self.gridWidget_2)
        self.shotRange_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shotRange_label2.setObjectName("shotRange_label2")
        self.gridLayout_3.addWidget(self.shotRange_label2, 2, 0, 1, 1)
        self.shotRange_lineEdit2 = QtGui.QLineEdit(self.gridWidget_2)
        self.shotRange_lineEdit2.setObjectName("shotRange_lineEdit2")
        self.gridLayout_3.addWidget(self.shotRange_lineEdit2, 2, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.gridWidget_2)
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)
        self.horizontalWidget3 = QtGui.QWidget(self.verticalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget3.setSizePolicy(sizePolicy)
        self.horizontalWidget3.setObjectName("horizontalWidget3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.createSequence_pushButton = QtGui.QPushButton(self.horizontalWidget3)
        self.createSequence_pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.createSequence_pushButton.setObjectName("createSequence_pushButton")
        self.horizontalLayout_7.addWidget(self.createSequence_pushButton)
        self.verticalLayout_3.addWidget(self.horizontalWidget3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.verticalWidget_2)
        self.tabWidget.addTab(self.createSequenceTab, "")
        self.addShotsTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.addShotsTab.sizePolicy().hasHeightForWidth())
        self.addShotsTab.setSizePolicy(sizePolicy)
        self.addShotsTab.setObjectName("addShotsTab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.addShotsTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalWidget_3 = QtGui.QWidget(self.addShotsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_4 = QtGui.QWidget(self.verticalWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget_4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_4.setSizePolicy(sizePolicy)
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gridWidget_3 = QtGui.QWidget(self.horizontalWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gridWidget_3.sizePolicy().hasHeightForWidth())
        self.gridWidget_3.setSizePolicy(sizePolicy)
        self.gridWidget_3.setObjectName("gridWidget_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.gridWidget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.project_label3 = QtGui.QLabel(self.gridWidget_3)
        self.project_label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label3.setObjectName("project_label3")
        self.gridLayout_4.addWidget(self.project_label3, 0, 0, 1, 1)
        self.project_comboBox3 = QtGui.QComboBox(self.gridWidget_3)
        self.project_comboBox3.setObjectName("project_comboBox3")
        self.gridLayout_4.addWidget(self.project_comboBox3, 0, 1, 1, 1)
        self.sequence_label3 = QtGui.QLabel(self.gridWidget_3)
        self.sequence_label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_label3.setObjectName("sequence_label3")
        self.gridLayout_4.addWidget(self.sequence_label3, 1, 0, 1, 1)
        self.shotRange_label3 = QtGui.QLabel(self.gridWidget_3)
        self.shotRange_label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shotRange_label3.setObjectName("shotRange_label3")
        self.gridLayout_4.addWidget(self.shotRange_label3, 2, 0, 1, 1)
        self.shotRange_lineEdit3 = QtGui.QLineEdit(self.gridWidget_3)
        self.shotRange_lineEdit3.setObjectName("shotRange_lineEdit3")
        self.gridLayout_4.addWidget(self.shotRange_lineEdit3, 2, 1, 1, 1)
        self.sequence_comboBox3 = QtGui.QComboBox(self.gridWidget_3)
        self.sequence_comboBox3.setObjectName("sequence_comboBox3")
        self.gridLayout_4.addWidget(self.sequence_comboBox3, 1, 1, 1, 1)
        self.horizontalLayout_8.addWidget(self.gridWidget_3)
        self.verticalLayout_4.addWidget(self.horizontalWidget_4)
        self.horizontalWidget_3 = QtGui.QWidget(self.verticalWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy)
        self.horizontalWidget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.addShots_pushButton = QtGui.QPushButton(self.horizontalWidget_3)
        self.addShots_pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.addShots_pushButton.setObjectName("addShots_pushButton")
        self.horizontalLayout_9.addWidget(self.addShots_pushButton)
        self.verticalLayout_4.addWidget(self.horizontalWidget_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.verticalWidget_3)
        self.tabWidget.addTab(self.addShotsTab, "")
        self.addAlternativeShotsTab = QtGui.QWidget()
        self.addAlternativeShotsTab.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.addAlternativeShotsTab.sizePolicy().hasHeightForWidth())
        self.addAlternativeShotsTab.setSizePolicy(sizePolicy)
        self.addAlternativeShotsTab.setObjectName("addAlternativeShotsTab")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.addAlternativeShotsTab)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalWidget_4 = QtGui.QWidget(self.addAlternativeShotsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalWidget_6 = QtGui.QWidget(self.verticalWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget_6.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_6.setSizePolicy(sizePolicy)
        self.horizontalWidget_6.setObjectName("horizontalWidget_6")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridWidget_4 = QtGui.QWidget(self.horizontalWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gridWidget_4.sizePolicy().hasHeightForWidth())
        self.gridWidget_4.setSizePolicy(sizePolicy)
        self.gridWidget_4.setObjectName("gridWidget_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.gridWidget_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.project_label4 = QtGui.QLabel(self.gridWidget_4)
        self.project_label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label4.setObjectName("project_label4")
        self.gridLayout_5.addWidget(self.project_label4, 0, 0, 1, 1)
        self.project_comboBox4 = QtGui.QComboBox(self.gridWidget_4)
        self.project_comboBox4.setObjectName("project_comboBox4")
        self.gridLayout_5.addWidget(self.project_comboBox4, 0, 1, 1, 1)
        self.sequence_label4 = QtGui.QLabel(self.gridWidget_4)
        self.sequence_label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_label4.setObjectName("sequence_label4")
        self.gridLayout_5.addWidget(self.sequence_label4, 1, 0, 1, 1)
        self.shotNumber_label4 = QtGui.QLabel(self.gridWidget_4)
        self.shotNumber_label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.shotNumber_label4.setObjectName("shotNumber_label4")
        self.gridLayout_5.addWidget(self.shotNumber_label4, 2, 0, 1, 1)
        self.sequence_comboBox4 = QtGui.QComboBox(self.gridWidget_4)
        self.sequence_comboBox4.setObjectName("sequence_comboBox4")
        self.gridLayout_5.addWidget(self.sequence_comboBox4, 1, 1, 1, 1)
        self.shotNumber_comboBox4 = QtGui.QComboBox(self.gridWidget_4)
        self.shotNumber_comboBox4.setObjectName("shotNumber_comboBox4")
        self.gridLayout_5.addWidget(self.shotNumber_comboBox4, 2, 1, 1, 1)
        self.horizontalLayout_10.addWidget(self.gridWidget_4)
        self.verticalLayout_6.addWidget(self.horizontalWidget_6)
        self.horizontalWidget_5 = QtGui.QWidget(self.verticalWidget_4)
        self.horizontalWidget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalWidget_5.setObjectName("horizontalWidget_5")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.addAlternativeShot_pushButton = QtGui.QPushButton(self.horizontalWidget_5)
        self.addAlternativeShot_pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.addAlternativeShot_pushButton.setObjectName("addAlternativeShot_pushButton")
        self.horizontalLayout_11.addWidget(self.addAlternativeShot_pushButton)
        self.verticalLayout_6.addWidget(self.horizontalWidget_5)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_12.addWidget(self.verticalWidget_4)
        self.tabWidget.addTab(self.addAlternativeShotsTab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.servers_comboBox, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.project_lineEdit1)
        MainWindow.setTabOrder(self.project_lineEdit1, self.createProject_pushButton)
        MainWindow.setTabOrder(self.createProject_pushButton, self.project_comboBox2)
        MainWindow.setTabOrder(self.project_comboBox2, self.sequence_lineEdit2)
        MainWindow.setTabOrder(self.sequence_lineEdit2, self.shotRange_lineEdit2)
        MainWindow.setTabOrder(self.shotRange_lineEdit2, self.createSequence_pushButton)
        MainWindow.setTabOrder(self.createSequence_pushButton, self.project_comboBox3)
        MainWindow.setTabOrder(self.project_comboBox3, self.sequence_comboBox3)
        MainWindow.setTabOrder(self.sequence_comboBox3, self.shotRange_lineEdit3)
        MainWindow.setTabOrder(self.shotRange_lineEdit3, self.addShots_pushButton)
        MainWindow.setTabOrder(self.addShots_pushButton, self.project_comboBox4)
        MainWindow.setTabOrder(self.project_comboBox4, self.sequence_comboBox4)
        MainWindow.setTabOrder(self.sequence_comboBox4, self.shotNumber_comboBox4)
        MainWindow.setTabOrder(self.shotNumber_comboBox4, self.addAlternativeShot_pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.servers_label.setText(QtGui.QApplication.translate("MainWindow", "server", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label1.setText(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.createProject_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createProjectTab), QtGui.QApplication.translate("MainWindow", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label2.setText(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label2.setText(QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.shotRange_label2.setText(QtGui.QApplication.translate("MainWindow", "Shot Range", None, QtGui.QApplication.UnicodeUTF8))
        self.createSequence_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createSequenceTab), QtGui.QApplication.translate("MainWindow", "Create Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label3.setText(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label3.setText(QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.shotRange_label3.setText(QtGui.QApplication.translate("MainWindow", "Shot Range", None, QtGui.QApplication.UnicodeUTF8))
        self.addShots_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addShotsTab), QtGui.QApplication.translate("MainWindow", "Add Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label4.setText(QtGui.QApplication.translate("MainWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label4.setText(QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.shotNumber_label4.setText(QtGui.QApplication.translate("MainWindow", "Shot Number", None, QtGui.QApplication.UnicodeUTF8))
        self.addAlternativeShot_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Alternative Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addAlternativeShotsTab), QtGui.QApplication.translate("MainWindow", "Add Alternative Shots", None, QtGui.QApplication.UnicodeUTF8))

