# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012, Erkan Ozgur Yilmaz
# 
# This module is part of oyProjectManager and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import sys
import os
import shutil
import tempfile
import unittest

#from PySide import QtCore, QtGui
#from PySide.QtCore import Qt
#from PySide.QtTest import QTest
import sip
import logging
import datetime

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtTest import QTest

from oyProjectManager import config, db
from oyProjectManager.core.models import (Project, Asset, Version, User,
                                          VersionType, Sequence, Shot,
                                          EnvironmentBase)
from oyProjectManager.ui import status_manager

conf = config.Config()

logger = logging.getLogger("oyProjectManager.ui.status_manager")
logger.setLevel(logging.DEBUG)

class StatusViewerTester(unittest.TestCase):
    """tests the oyProjectManager.ui.status_manager class
    """
    
    def setUp(self):
        """setup the test
        """
        
        # -----------------------------------------------------------------
        # start of the setUp
        # create the environment variable and point it to a temp directory
        self.temp_config_folder = tempfile.mkdtemp()
        self.temp_projects_folder = tempfile.mkdtemp()
        
        os.environ["OYPROJECTMANAGER_PATH"] = self.temp_config_folder
        os.environ[conf.repository_env_key] = self.temp_projects_folder
        
        logger.debug('db.url: %s' % self.temp_config_folder)
        
        # for PyQt4
        self.app = QtGui.QApplication(sys.argv)
    
    def tearDown(self):
        """clean up the test
        """
        # set the db.session to None
        db.session = None
        
        # delete the temp folders
        shutil.rmtree(self.temp_config_folder)
        shutil.rmtree(self.temp_projects_folder)
    
    def show_dialog(self, dialog):
        """show the given dialog
        """
        dialog.show()
        self.app.exec_()
        self.app.connect(
            self.app,
            QtCore.SIGNAL("lastWindowClosed()"),
            self.app,
            QtCore.SLOT("quit()")
        )
    
    def test_close_button_closes_ui(self):
        """testing if the close button is closing the ui
        """
        dialog = status_manager.MainDialog()
        dialog.show()

        self.assertEqual(dialog.isVisible(), True)
        
        # now run the UI
        QTest.mouseClick(dialog.close_pushButton, Qt.LeftButton)
        self.assertEqual(dialog.isVisible(), False)
    
    def test_projects_comboBox_no_problem_when_there_is_no_project(self):
        """testing if there will be no problem when there is no project created
        yet
        """
        dialog = status_manager.MainDialog()
    
    def test_assets_tableWidget_horizontal_labels_are_set_properly(self):
        """testing if the assets_tableWidget horizontal labels are filled with
        all the possible VersionTypes for assets
        """
        
        db.setup()
        
        asset_vtypes = db.query(VersionType)\
            .filter(VersionType.type_for=='Asset')\
            .order_by(VersionType.name)\
            .all()
        
        dialog = status_manager.MainDialog()
#        self.show_dialog(dialog)
        
        self.assertEqual(
            dialog.assets_tableWidget.horizontalHeaderItem(0).text(),
            'Type'
        )
        
        self.assertEqual(
            dialog.assets_tableWidget.horizontalHeaderItem(1).text(),
            'Name'
        )
        
        self.assertEqual(
            dialog.assets_tableWidget.columnCount(),
            len(asset_vtypes) + 2
        )
        
        for i, vtype in enumerate(asset_vtypes):
            self.assertEqual(
                dialog.assets_tableWidget.horizontalHeaderItem(i+2).text(),
                vtype.code
            )
    
    def test_assets_tableWidget_is_filled_with_Asset_data(self):
        """testing if the assets_tableWidget is filled with asset data properly
        """
        
        db.setup()
        
        # create a project
        proj1 = Project('Test Project 1')
        proj1.save()
        
        proj2 = Project('Test Project 2')
        proj2.save()
        
        asset_vtypes = db.query(VersionType)\
            .filter(VersionType.type_for=='Asset')\
            .order_by(VersionType.name)\
            .all()
        
        admin = db.query(User).first()
        
        asset1 = Asset(proj1, 'Test Asset 1', type='Char')
        asset1.save()
        
        asset2 = Asset(proj1, 'Test Asset 2', type='Prop')
        asset2.save()
        
        asset3 = Asset(proj1, 'Test Asset 3', type='Environment')
        asset3.save()
        
        asset4 = Asset(proj1, 'Test Asset 4', type='Prop')
        asset4.save()
        
        # versions for asset1
        version1 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[0],
            created_by=admin,
            status=conf.status_list[0]
        )
        version1.save()
        
        version2 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[1],
            created_by=admin,
            status=conf.status_list[1]
        )
        version2.save()
        
        version3 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[2],
            created_by=admin,
            status=conf.status_list[2]
        )
        version3.save()
        
        # version for asset1 with different takes
        version4 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[3],
            created_by=admin,
            status=conf.status_list[3],
        )
        version4.save()
        
        version5 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[4],
            created_by=admin,
            status=conf.status_list[4],
        )
        version5.save()
        
        version6 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[5],
            created_by=admin,
            status=conf.status_list[4],
        )
        version6.save()
        
        version7 = Version(
            version_of=asset1,
            base_name=asset1.code,
            type=asset_vtypes[5],
            created_by=admin,
            status=conf.status_list[4]
        )
        version7.save()
           
        dialog = status_manager.MainDialog()
#        self.show_dialog(dialog)      
        
        # start tests
        
        # set the project to project1
        dialog.projects_comboBox.setCurrentIndex(0)
        
        # asset1's vtypes[0] vtypes[1] vtypes[2] vtypes[3]
        
        
    def test_shots_tableWidget_is_filled_with_Shot_data(self):
        """testing if the shots_tableWidget is filled with shot data properly
        """
        
        db.setup()
        
        # create a project
        proj1 = Project('Test Project 1')
        proj1.save()
        
        proj2 = Project('Test Project 2')
        proj2.save()
        
        shot_vtypes = db.query(VersionType)\
            .filter(VersionType.type_for=='Shot')\
            .order_by(VersionType.name)\
            .all()
        
        admin = db.query(User).first()
        
        # seqs for proj1
        seq1 = Sequence(proj1, 'Test Seq 1')
        seq1.save()
        
        seq2 = Sequence(proj1, 'Test Seq 2')
        seq2.save()
        
        # seqs for proj2
        seq3 = Sequence(proj2, 'Test Seq 3')
        seq3.save()
        
        seq4 = Sequence(proj2, 'Test Seq 4')
        seq4.save()
        
        # shots for seq1
        shot1 = Shot(seq1, 1)
        shot1.save()
        
        shot2 = Shot(seq1, 2)
        shot2.save()
        
        shot3 = Shot(seq1, 3)
        shot3.save()
        
        # shots for seq2
        shot4 = Shot(seq2, 4)
        shot4.save()
        
        shot5 = Shot(seq2, 5)
        shot5.save()
        
        shot6 = Shot(seq2, 6)
        shot6.save()
        
        # shots for seq3
        shot7 = Shot(seq3, 7)
        shot7.save()
        
        shot8 = Shot(seq3, 8)
        shot8.save()
        
        # shots for seq4
        shot9 = Shot(seq4, 9)
        shot9.save()
        
        shot10 = Shot(seq4, 10)
        shot10.save()
        
        # versions for shot1
        version1 = Version(
            version_of=shot1,
            base_name=shot1.code,
            type=shot_vtypes[0],
            created_by=admin,
            status=conf.status_list[0]
        )
        version1.save()
        
        version2 = Version(
            version_of=shot1,
            base_name=shot1.code,
            type=shot_vtypes[1],
            created_by=admin,
            status=conf.status_list[1]
        )
        version2.save()
        
        # versions for shot2
        version3 = Version(
            version_of=shot2,
            base_name=shot2.code,
            type=shot_vtypes[2],
            created_by=admin,
            status=conf.status_list[2]
        )
        version3.save()
        
        version4 = Version(
            version_of=shot2,
            base_name=shot2.code,
            type=shot_vtypes[3],
            created_by=admin,
            status=conf.status_list[3],
        )
        version4.save()
        
        # versions for shot3
        version5 = Version(
            version_of=shot3,
            base_name=shot3.code,
            type=shot_vtypes[4],
            created_by=admin,
            status=conf.status_list[4],
        )
        version5.save()
        
        version6 = Version(
            version_of=shot3,
            base_name=shot3.code,
            type=shot_vtypes[5],
            created_by=admin,
            status=conf.status_list[4],
        )
        version6.save()
        
        # versions for shot4
        version7 = Version(
            version_of=shot4,
            base_name=shot4.code,
            type=shot_vtypes[5],
            created_by=admin,
            status=conf.status_list[4]
        )
        version7.save()
        
        version8 = Version(
            version_of=shot4,
            base_name=shot4.code,
            type=shot_vtypes[5],
            created_by=admin,
            status=conf.status_list[0]
        )
        version8.save()
        
        dialog = status_manager.MainDialog()
#        self.show_dialog(dialog)      
        
        # start tests
        
        # set the project to project1
        dialog.projects_comboBox.setCurrentIndex(0)
        
        # asset1's vtypes[0] vtypes[1] vtypes[2] vtypes[3]
