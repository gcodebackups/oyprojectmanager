# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eoyilmaz/Documents/development/oyProjectManager/oyProjectManager/ui/version_creator.ui'
#
# Created: Fri Mar 30 10:34:20 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(1312, 689)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.projects_label = QtGui.QLabel(self.verticalWidget)
        self.projects_label.setObjectName("projects_label")
        self.horizontalLayout_11.addWidget(self.projects_label)
        self.projects_comboBox = QtGui.QComboBox(self.verticalWidget)
        self.projects_comboBox.setObjectName("projects_comboBox")
        self.horizontalLayout_11.addWidget(self.projects_comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.user_label = QtGui.QLabel(self.verticalWidget)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout_11.addWidget(self.user_label)
        self.users_comboBox = QtGui.QComboBox(self.verticalWidget)
        self.users_comboBox.setObjectName("users_comboBox")
        self.horizontalLayout_11.addWidget(self.users_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.line_3 = QtGui.QFrame(self.verticalWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtGui.QTabWidget(self.verticalWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.assets_tab = QtGui.QWidget()
        self.assets_tab.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.assets_tab.sizePolicy().hasHeightForWidth())
        self.assets_tab.setSizePolicy(sizePolicy)
        self.assets_tab.setObjectName("assets_tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.assets_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.asset_info_groupBox = QtGui.QGroupBox(self.assets_tab)
        self.asset_info_groupBox.setFlat(False)
        self.asset_info_groupBox.setObjectName("asset_info_groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.asset_info_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.asset_name_label = QtGui.QLabel(self.asset_info_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.asset_name_label.setFont(font)
        self.asset_name_label.setObjectName("asset_name_label")
        self.horizontalLayout_9.addWidget(self.asset_name_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.create_asset_pushButton = QtGui.QPushButton(self.asset_info_groupBox)
        self.create_asset_pushButton.setObjectName("create_asset_pushButton")
        self.horizontalLayout_9.addWidget(self.create_asset_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.assets_listWidget = QtGui.QListWidget(self.asset_info_groupBox)
        self.assets_listWidget.setObjectName("assets_listWidget")
        self.verticalLayout_2.addWidget(self.assets_listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.asset_info_groupBox)
        self.tabWidget.addTab(self.assets_tab, "")
        self.shots_tab = QtGui.QWidget()
        self.shots_tab.setEnabled(True)
        self.shots_tab.setObjectName("shots_tab")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.shots_tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.sequences_label = QtGui.QLabel(self.shots_tab)
        self.sequences_label.setObjectName("sequences_label")
        self.horizontalLayout_15.addWidget(self.sequences_label)
        self.sequences_comboBox = QtGui.QComboBox(self.shots_tab)
        self.sequences_comboBox.setObjectName("sequences_comboBox")
        self.horizontalLayout_15.addWidget(self.sequences_comboBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.asset_info_groupBox_2 = QtGui.QGroupBox(self.shots_tab)
        self.asset_info_groupBox_2.setFlat(False)
        self.asset_info_groupBox_2.setObjectName("asset_info_groupBox_2")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.asset_info_groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.shot_name_label = QtGui.QLabel(self.asset_info_groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.shot_name_label.setFont(font)
        self.shot_name_label.setObjectName("shot_name_label")
        self.horizontalLayout_13.addWidget(self.shot_name_label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.create_shot_pushButton = QtGui.QPushButton(self.asset_info_groupBox_2)
        self.create_shot_pushButton.setEnabled(True)
        self.create_shot_pushButton.setObjectName("create_shot_pushButton")
        self.horizontalLayout_13.addWidget(self.create_shot_pushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.shots_listWidget = QtGui.QListWidget(self.asset_info_groupBox_2)
        self.shots_listWidget.setObjectName("shots_listWidget")
        self.verticalLayout_9.addWidget(self.shots_listWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_range_label = QtGui.QLabel(self.asset_info_groupBox_2)
        self.frame_range_label.setObjectName("frame_range_label")
        self.gridLayout.addWidget(self.frame_range_label, 0, 0, 1, 1)
        self.start_frame_spinBox = QtGui.QSpinBox(self.asset_info_groupBox_2)
        self.start_frame_spinBox.setMaximum(9999)
        self.start_frame_spinBox.setObjectName("start_frame_spinBox")
        self.gridLayout.addWidget(self.start_frame_spinBox, 0, 1, 1, 1)
        self.end_frame_spinBox = QtGui.QSpinBox(self.asset_info_groupBox_2)
        self.end_frame_spinBox.setMaximum(9999)
        self.end_frame_spinBox.setObjectName("end_frame_spinBox")
        self.gridLayout.addWidget(self.end_frame_spinBox, 0, 2, 1, 1)
        self.handles_label = QtGui.QLabel(self.asset_info_groupBox_2)
        self.handles_label.setObjectName("handles_label")
        self.gridLayout.addWidget(self.handles_label, 1, 0, 1, 1)
        self.handle_at_start_spinBox = QtGui.QSpinBox(self.asset_info_groupBox_2)
        self.handle_at_start_spinBox.setMaximum(9999)
        self.handle_at_start_spinBox.setObjectName("handle_at_start_spinBox")
        self.gridLayout.addWidget(self.handle_at_start_spinBox, 1, 1, 1, 1)
        self.handle_at_end_spinBox = QtGui.QSpinBox(self.asset_info_groupBox_2)
        self.handle_at_end_spinBox.setMaximum(9999)
        self.handle_at_end_spinBox.setObjectName("handle_at_end_spinBox")
        self.gridLayout.addWidget(self.handle_at_end_spinBox, 1, 2, 1, 1)
        self.shot_info_update_pushButton = QtGui.QPushButton(self.asset_info_groupBox_2)
        self.shot_info_update_pushButton.setObjectName("shot_info_update_pushButton")
        self.gridLayout.addWidget(self.shot_info_update_pushButton, 1, 3, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.verticalLayout_11.addWidget(self.asset_info_groupBox_2)
        self.tabWidget.addTab(self.shots_tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.thumbnail_graphicsView = QtGui.QGraphicsView(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail_graphicsView.sizePolicy().hasHeightForWidth())
        self.thumbnail_graphicsView.setSizePolicy(sizePolicy)
        self.thumbnail_graphicsView.setMinimumSize(QtCore.QSize(320, 180))
        self.thumbnail_graphicsView.setMaximumSize(QtCore.QSize(320, 180))
        self.thumbnail_graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thumbnail_graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.thumbnail_graphicsView.setBackgroundBrush(brush)
        self.thumbnail_graphicsView.setInteractive(False)
        self.thumbnail_graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.thumbnail_graphicsView.setObjectName("thumbnail_graphicsView")
        self.horizontalLayout_8.addWidget(self.thumbnail_graphicsView)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.upload_thumbnail_pushButton = QtGui.QPushButton(self.verticalWidget)
        self.upload_thumbnail_pushButton.setObjectName("upload_thumbnail_pushButton")
        self.horizontalLayout_16.addWidget(self.upload_thumbnail_pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14.addLayout(self.verticalLayout_5)
        self.line_2 = QtGui.QFrame(self.verticalWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_14.addWidget(self.line_2)
        self.new_version_groupBox = QtGui.QGroupBox(self.verticalWidget)
        self.new_version_groupBox.setObjectName("new_version_groupBox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.new_version_groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.takes_label = QtGui.QLabel(self.new_version_groupBox)
        self.takes_label.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.takes_label.setFont(font)
        self.takes_label.setObjectName("takes_label")
        self.gridLayout_3.addWidget(self.takes_label, 1, 0, 1, 1)
        self.note_label = QtGui.QLabel(self.new_version_groupBox)
        self.note_label.setMinimumSize(QtCore.QSize(35, 0))
        self.note_label.setObjectName("note_label")
        self.gridLayout_3.addWidget(self.note_label, 2, 0, 1, 1)
        self.version_types_label = QtGui.QLabel(self.new_version_groupBox)
        self.version_types_label.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.version_types_label.setFont(font)
        self.version_types_label.setObjectName("version_types_label")
        self.gridLayout_3.addWidget(self.version_types_label, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.version_types_listWidget = QtGui.QListWidget(self.new_version_groupBox)
        self.version_types_listWidget.setObjectName("version_types_listWidget")
        self.horizontalLayout_4.addWidget(self.version_types_listWidget)
        self.add_type_toolButton = QtGui.QToolButton(self.new_version_groupBox)
        self.add_type_toolButton.setObjectName("add_type_toolButton")
        self.horizontalLayout_4.addWidget(self.add_type_toolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.takes_listWidget = QtGui.QListWidget(self.new_version_groupBox)
        self.takes_listWidget.setObjectName("takes_listWidget")
        self.horizontalLayout_6.addWidget(self.takes_listWidget)
        self.add_take_toolButton = QtGui.QToolButton(self.new_version_groupBox)
        self.add_take_toolButton.setObjectName("add_take_toolButton")
        self.horizontalLayout_6.addWidget(self.add_take_toolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.note_textEdit = QtGui.QTextEdit(self.new_version_groupBox)
        self.note_textEdit.setEnabled(True)
        self.note_textEdit.setTabChangesFocus(True)
        self.note_textEdit.setObjectName("note_textEdit")
        self.gridLayout_3.addWidget(self.note_textEdit, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.publish_checkBox = QtGui.QCheckBox(self.new_version_groupBox)
        self.publish_checkBox.setObjectName("publish_checkBox")
        self.horizontalLayout_7.addWidget(self.publish_checkBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.export_as_pushButton = QtGui.QPushButton(self.new_version_groupBox)
        self.export_as_pushButton.setObjectName("export_as_pushButton")
        self.horizontalLayout_2.addWidget(self.export_as_pushButton)
        self.save_as_pushButton = QtGui.QPushButton(self.new_version_groupBox)
        self.save_as_pushButton.setDefault(True)
        self.save_as_pushButton.setObjectName("save_as_pushButton")
        self.horizontalLayout_2.addWidget(self.save_as_pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14.addWidget(self.new_version_groupBox)
        self.line = QtGui.QFrame(self.verticalWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_14.addWidget(self.line)
        self.previous_versions_groupBox = QtGui.QGroupBox(self.verticalWidget)
        self.previous_versions_groupBox.setObjectName("previous_versions_groupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.previous_versions_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.show_published_only_checkBox = QtGui.QCheckBox(self.previous_versions_groupBox)
        self.show_published_only_checkBox.setObjectName("show_published_only_checkBox")
        self.horizontalLayout_10.addWidget(self.show_published_only_checkBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.show_only_label = QtGui.QLabel(self.previous_versions_groupBox)
        self.show_only_label.setObjectName("show_only_label")
        self.horizontalLayout_10.addWidget(self.show_only_label)
        self.version_count_spinBox = QtGui.QSpinBox(self.previous_versions_groupBox)
        self.version_count_spinBox.setMaximum(999999)
        self.version_count_spinBox.setProperty("value", 10)
        self.version_count_spinBox.setObjectName("version_count_spinBox")
        self.horizontalLayout_10.addWidget(self.version_count_spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.previous_versions_tableWidget = QtGui.QTableWidget(self.previous_versions_groupBox)
        self.previous_versions_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.previous_versions_tableWidget.setAlternatingRowColors(True)
        self.previous_versions_tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.previous_versions_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.previous_versions_tableWidget.setShowGrid(False)
        self.previous_versions_tableWidget.setColumnCount(5)
        self.previous_versions_tableWidget.setObjectName("previous_versions_tableWidget")
        self.previous_versions_tableWidget.setColumnCount(5)
        self.previous_versions_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(4, item)
        self.previous_versions_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.previous_versions_tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.previous_versions_tableWidget)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.open_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.open_pushButton.setObjectName("open_pushButton")
        self.horizontalLayout_5.addWidget(self.open_pushButton)
        self.reference_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.reference_pushButton.setObjectName("reference_pushButton")
        self.horizontalLayout_5.addWidget(self.reference_pushButton)
        self.import_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.import_pushButton.setObjectName("import_pushButton")
        self.horizontalLayout_5.addWidget(self.import_pushButton)
        self.close_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.close_pushButton.setStyleSheet("")
        self.close_pushButton.setDefault(False)
        self.close_pushButton.setFlat(False)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout_5.addWidget(self.close_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_14.addWidget(self.previous_versions_groupBox)
        self.horizontalLayout_14.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout.addWidget(self.verticalWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.projects_comboBox, self.users_comboBox)
        Dialog.setTabOrder(self.users_comboBox, self.create_asset_pushButton)
        Dialog.setTabOrder(self.create_asset_pushButton, self.assets_listWidget)
        Dialog.setTabOrder(self.assets_listWidget, self.sequences_comboBox)
        Dialog.setTabOrder(self.sequences_comboBox, self.create_shot_pushButton)
        Dialog.setTabOrder(self.create_shot_pushButton, self.shots_listWidget)
        Dialog.setTabOrder(self.shots_listWidget, self.add_type_toolButton)
        Dialog.setTabOrder(self.add_type_toolButton, self.add_take_toolButton)
        Dialog.setTabOrder(self.add_take_toolButton, self.note_textEdit)
        Dialog.setTabOrder(self.note_textEdit, self.export_as_pushButton)
        Dialog.setTabOrder(self.export_as_pushButton, self.save_as_pushButton)
        Dialog.setTabOrder(self.save_as_pushButton, self.previous_versions_tableWidget)
        Dialog.setTabOrder(self.previous_versions_tableWidget, self.open_pushButton)
        Dialog.setTabOrder(self.open_pushButton, self.reference_pushButton)
        Dialog.setTabOrder(self.reference_pushButton, self.import_pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Version Creator - oyProjectManager", None, QtGui.QApplication.UnicodeUTF8))
        self.projects_label.setText(QtGui.QApplication.translate("Dialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.user_label.setText(QtGui.QApplication.translate("Dialog", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Asset Information", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_name_label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.create_asset_pushButton.setText(QtGui.QApplication.translate("Dialog", "Create New Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assets_tab), QtGui.QApplication.translate("Dialog", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.sequences_label.setText(QtGui.QApplication.translate("Dialog", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_info_groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Shot Information", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_name_label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.create_shot_pushButton.setText(QtGui.QApplication.translate("Dialog", "Create New Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_range_label.setText(QtGui.QApplication.translate("Dialog", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.handles_label.setText(QtGui.QApplication.translate("Dialog", "Handles", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_info_update_pushButton.setText(QtGui.QApplication.translate("Dialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shots_tab), QtGui.QApplication.translate("Dialog", "Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.upload_thumbnail_pushButton.setText(QtGui.QApplication.translate("Dialog", "Upload Thumbnail...", None, QtGui.QApplication.UnicodeUTF8))
        self.new_version_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "New Version", None, QtGui.QApplication.UnicodeUTF8))
        self.takes_label.setText(QtGui.QApplication.translate("Dialog", "Take", None, QtGui.QApplication.UnicodeUTF8))
        self.note_label.setText(QtGui.QApplication.translate("Dialog", "Note", None, QtGui.QApplication.UnicodeUTF8))
        self.version_types_label.setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.add_type_toolButton.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.add_take_toolButton.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.note_textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_checkBox.setText(QtGui.QApplication.translate("Dialog", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.export_as_pushButton.setText(QtGui.QApplication.translate("Dialog", "Export Selection As", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as_pushButton.setText(QtGui.QApplication.translate("Dialog", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Previous Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.show_published_only_checkBox.setText(QtGui.QApplication.translate("Dialog", "Show Published Only", None, QtGui.QApplication.UnicodeUTF8))
        self.show_only_label.setText(QtGui.QApplication.translate("Dialog", "Show Only", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "File Size", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "Note", None, QtGui.QApplication.UnicodeUTF8))
        self.open_pushButton.setText(QtGui.QApplication.translate("Dialog", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.reference_pushButton.setText(QtGui.QApplication.translate("Dialog", "Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.import_pushButton.setText(QtGui.QApplication.translate("Dialog", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.close_pushButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

