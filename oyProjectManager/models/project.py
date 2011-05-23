# -*- coding: utf-8 -*-



import sys
import os
import shutil
import glob
import re

from beaker import cache

from xml.dom import minidom

import oyAuxiliaryFunctions as oyAux

from oyProjectManager import utils
from oyProjectManager.models import asset, user, repository




# create a cache with the CacheManager
bCache = cache.CacheManager()




########################################################################
class DefaultSettingsParser(object):
    """A parser for the default settings for the sequence.
    
    Parses the given settings xml and fills the attributes of the given
    :class:`~oyProjectManager.models.project.Sequence` class.
    
    :param sequence: a :class:`~oyProjectManager.models.project.Sequence`
      instance. The default is None and this causes a ValueError to be raised.
    
    :type sequence: :class:`~oyProjectManager.models.project.Sequence`
    
    :param str content: the settings content as a string. Default is None
      and this causes a ValueError to be raised.
    
    The version 1 spesification of the default settings consists of the
    following nodes:
      
       * root: The root node
         
          * sequenceData node:
            
            Attributes:
              
               * shotPrefix: default is "SH", it is the prefix to be added
                 before the shot number
              
               * shotPadding: default is 3, it is the number of padding going
                 to be applied to find the string representation of the shot
                 number. If the shot number is 5 and the shotPadding is set to
                 3 and the shotPrefix is "SH" then the final shot name will be
                 SH005
               
               * revPrefix: default is "r", it is the revision variable prefix
              
               * revpadding: default is 2, it is the revision number padding,
                 for revision 3 the default values will output a string of
                 "r03" for the revision string variable
              
               * verPrefix: default is "v", it is the version varaible prefix
              
               * verPadding: default is 3, it is the version number padding for
                 default values a file version of 14 will outpu a string of
                 "v014" for the version string variable.
              
               * timeUnit: default is pal, it is the time unit for the project,
                 possible values are "pal, film, ntsc, game". This variable
                 follows the Maya's time unit format.
            
            Child elements:
              
               * structure: it is the child of sequenceData. Structure element
                 holds the project structure information. Every project will be
                 created by using this project structure.
                 
                 Child elements:
                   
                    * shotDependent: show the shot dependent folders. A shot
                      dependent folder will contain shot folders. For example
                      a folder called ANIMATION could be defined under
                      shotDependent folders, then oyProjectManager will
                      automatically place folders for every shot of the project.
                      So if the project has three shots with shot numbers 10,
                      14, 21 then the structure of the ANIMATION folder will be
                      like:
                        
                        ANIMATION/
                        ANIMATION/SH010/
                        ANIMATION/SH013/
                        ANIMATION/SH021/
                   
                    * shotIndependent: show the shot independent folder, or the
                      rest of the project structure. So any other folder which
                      doesn't have a direct relation with shots can be placed
                      here. For example you can place folders for MODELS, RIGS,
                      OUTGOING_FILES etc.
                   
               * assetTypes: This element contains information about asset
                 types.
                 
                 Attributes: None
                 
                 Child elements:
                   
                    * type: this is an asset type
                      
                      Attributes:
                        
                         * name: the name of the type
                         
                         * path: the project relative path for the asset files
                           in this type.
                        
                         * shotDependent: it is a boolean value that specifies
                           if this asset type is shot dependent.
                        
                         * environments: this attribute lists the environment
                           names where this asset type is valid through. It
                           should list the environment names in a comma
                           separated value (CSV) format
                        
                         * output_path: shows the output folder of this asset
                           type. For example you can set the render output
                           folder by setting the output folder of the RENDER
                           asset type to a spesific folder relative to the
                           project root.
              
              
               * shotData: This is the element that shows the current projects
                 shot information.
                 
                 Child Elements:
                   
                    * shot: The shot it self
                      
                      Attributes:
                        
                         * name: this is the name of the shot, it just shows
                           the number and alternate letter part of the shot
                           name, so for a shot named "SH001A" the name
                           attribute is "1A"
                        
                         * start: this is the global start frame of the shot
                        
                         * end: this is the global end frame of the shot
                        
                      Child Elements:
                        
                         * description: This is the text element that has the
                           description of the current shot. You can place any
                           amount of text inside this text element.
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self):
        pass
        
    
    



########################################################################
class Project(object):
    """Manages project related data.
    
    A Project is simply a holder for Assets and Sequences.
    
    :param name: The name of the project. Should be a string or unicode. Name
      can not be None, a ValueError will be raised when it is given as None.
      The default value is None, so it will raise a ValueError.
      
      The given project name is validated against the following rules:
        
        * The name can only have A-Z and 0-9 and "_" characters, all the other
          chars are going to be filtered out.
        
        * The name can only start with literals, no spaces, no numbers or any
          other character is not allowed.
        
        * Numbers and underscores are only allowed if they are not the first
          letter.
        
        * All the letters should be upper case.
        
        * All the "-" (minus) signs are converted to "_" (under score)
        
        * All the CamelCase formattings are expanded to underscore (Camel_Case)
    
    Creating a Project instance is not enough to phsyically create the project
    folder. To make it hapen the
    :meth:`~oyProjectManager.models.project.Project.create` should be called
    to finish the creation process, which in fact is only a folder.
    
    A Project can not be created without a name or with a name which is None. A
    Project can not be created with an invalid name. For example, a project
    with name "'^+'^" can not be craeated because the name will become an empty
    string after the name validation process.
    
    
    .. versionadded:: 0.1.2
       Project Settings
       
    Projects have a file called ".settings.xml" in their root. This settings
    file holds information about:
    
       * The placement of the asset files.
    
       * The placement of the shot files.
    
       * The general folder structure of the project.
    
       * etc.
    
    Every project has its own settings file to hold the different and evolving
    directory structure of the projects.
    
    Even though it is not recommended the file can be edited by a text editor
    to change the project settings. But care must be taken while doing so.
    
    
    
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self, name=None):
        
        self._repository = repository.Repository()
        
        self._name = ""
        self._path = ""
        self._fullPath = ""
        
        self.name = self._validate_name(name)
        
        self._sequenceList = []
        
        self._exists = None
    
    
    
    #----------------------------------------------------------------------
    def __str__(self):
        """the string representation of the project
        """
        return self.name
    
    
    
    #----------------------------------------------------------------------
    def _validate_name(self, name_in):
        """validates the given name_in value
        """
        
        if name_in is None:
            raise ValueError("The name can not be None")
        
        if name_in is "":
            raise ValueError("The name can not be an empty string")
        
        # strip the name
        name_in = name_in.strip()
        
        # convert all the "-" signs to "_"
        name_in = name_in.replace("-", "_")
        
        # replace camel case letters
        name_in = re.sub(r"(.+?[a-z]+)([A-Z])", r"\1_\2", name_in)
        
        # remove unnecesary characters from the string
        name_in = re.sub("([^a-zA-Z0-9\s_]+)", r"", name_in)
        
        # remove all the characters from the begining which are not alpabetic
        name_in = re.sub("(^[^a-zA-Z]+)", r"", name_in)
        
        # substitude all spaces with "_" characters
        name_in = re.sub("([\s])+", "_", name_in)
        
        # convert it to upper case
        name_in = name_in.upper()
        
        # check if the name became empty string after validation
        if name_in is "":
            raise ValueError("The name is not valid after validation")
        
        return name_in
    
    
    
    #----------------------------------------------------------------------
    def _initPathVariables(self):
        
        self._path = self._repository.server_path
        if self._name != '' or self._name is not None:
            self._fullPath = os.path.join( self._path, self._name)
    
    
    
    #----------------------------------------------------------------------
    def create(self):
        """Creates the project directory in the repository.
        """
        
        # check if the project object has a name
        if self._name is None:
            raise RuntimeError("Please give a proper name to the project")
        
        # check if the folder allready exists
        #self._exists = not oyAux.createFolder(self._fullPath)
        utils.mkdir(self._fullPath)
        self._exists = 1
    
    
    
    #----------------------------------------------------------------------
    def createSequence(self, sequenceName, shots):
        """creates a sequence and returns the sequence object
        """
        newSequence = Sequence(self, sequenceName)
        newSequence.addShots(shots)
        newSequence.create()
        
        return newSequence
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache(expire=60)
    def sequenceNames(self):
        """returns the sequence names of that project
        """
        self.updateSequenceList()
        return self._sequenceList
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache(expire=60)
    def sequences(self):
        """Returns the sequences of the project as sequence objects.
        
        It utilizes the caching system.
        """
        
        self.updateSequenceList()
        sequences = [] * 0
        
        for sequenceName in self._sequenceList:
            sequences.append(Sequence( self, sequenceName))
        
        return sequences
    
    
    
    #----------------------------------------------------------------------
    def updateSequenceList(self):
        """updates the sequenceList variable
        """
        #self._sequenceList = os.listdir( self._fullPath )
        
        # filter other folders like .DS_Store
        for folder in os.listdir( self._fullPath ):
            filtered_folder_name = re.sub(
                r".*?(^[^A-Z_]+)([A-Z0-9_]+)",
                r"\2",
                folder
            )
            if filtered_folder_name == folder:
                self._sequenceList.append(folder)
        
        self._sequenceList.sort()
    
    
    
    #----------------------------------------------------------------------
    @property
    def fullPath(self):
        """reutrns the fullPath
        """
        return self._fullPath
    
    
    
    #----------------------------------------------------------------------
    @property
    def path(self):
        """returns the path
        """
        return self._path
    
    
    
    #----------------------------------------------------------------------
    def name():
        """the name property
        """
        
        def fget(self):
            return self._name
        
        def fset(self, name_in):
            self._name = self._validate_name(name_in)
            self._initPathVariables()
        
        return locals()
    
    name = property( **name() )
    
    
    
    #----------------------------------------------------------------------
    def repository():
        doc = "the repository object"
        
        def fget(self):
            return self._repository
        
        def fset(self, repo):
            self._repository = repo
        
        return locals()
    
    repository = property( **repository() )
    
    
    
    #----------------------------------------------------------------------
    @property
    def exists(self):
        """returns True if the project folder exists
        """
        if self._exists is None:
            self._exists = os.path.exists( self._fullPath )
        
        return self._exists






########################################################################
class Sequence(object):
    """Sequence object to help manage sequence data.
    
    By definition a Sequence is a group of
    :class:`~oyProjectManager.models.project.Shot`\ s.
    
    The class should be initialized with a
    :class:`~oyProjectManager.models.project.Project` instance and a
    sequenceName.
    
    Two sequences are considered the same if their name and their project
    names are matching.
    
    :param project: The owner
      :class:`~oyProjectManager.models.project.Project`. A sequence can not be
      created without a proper
      :class:`~oyProjectManager.models.project.Project`.
    
    :type project: :class:`~oyProjectManager.models.project.Project`
    
    :param str name: The name of the sequence. It is heavily formatted. Follows
      the same naming rules with the
      :class:`~oyProjectManager.models.project.Project`.
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self, project, name):
        # create the parent project with projectName
        
        
        assert(isinstance(project, Project))
        
        self._project = project
        self._repository = self._project.repository
        
        self._name = oyAux.stringConditioner(name, False, True, False, True, True, False )
        
        self._path = self._project.fullPath
        self._fullPath = os.path.join(self._path, self._name)
        
        self._settingsFile = ".settings.xml"
        self._settings_file_path = self._fullPath
        self._settings_file_full_path = os.path.join(self._settings_file_path,
                                                     self._settingsFile)
        self._settingsFileExists = False
        self._settings_dirty = False

        #print self._settings_file_full_path
        
        self._structure = Structure()
        self._assetTypes = [ asset.AssetType() ] * 0
        self._shotList = [] * 0 # should be a string
        self._shots = [] # the new shot objects
        
        self._shotPrefix = 'SH'
        self._shotPadding = 3
        self._revPrefix = 'r' # revision number prefix
        self._revPadding = 2
        self._verPrefix = 'v' # version number prefix
        self._verPadding = 3
        
        #self._extensionsToIgnore = [] * 0
        self._noSubNameField = False # to support the old types of projects
        
        self._timeUnit = 'pal' # by default set it to pal - ugly default settings
        
        self._environment = None # the working environment
        
        self._exists = False
        
        self.readSettings()
    
    
    
    #----------------------------------------------------------------------
    def readSettings(self):
        """reads the settingsFile
        """
        
        # check if there is a settings file
        if not os.path.exists(self._settings_file_full_path):
            #print "ERROR: no settings file in the sequence..."
            # TODO: assume that it is an old project and try to get
            # the data (just shot list) from the folders
            return
        else:
            self._settingsFileExists = True
            self._exists = True
        
        #print (self._settings_file_full_path)
        settingsAsXML = minidom.parse(self._settings_file_full_path)
        
        rootNode = settingsAsXML.childNodes[0]
        
        # -----------------------------------------------------
        # get main nodes
        
        # remove databaseData if exists
        doRemoveDatabaseDataNode = False
        databaseDataNode = rootNode.getElementsByTagName('databaseData')
        
        if len(databaseDataNode) > 0:
            # there should be a databaseData node
            doRemoveDatabaseDataNode = True
            
            # parse the databaseData nodes attributes as if it is a
            # sequenceDataNode
            self._parseSequenceDataNode( databaseDataNode[0] )
        
        sequenceDataNode = rootNode.getElementsByTagName('sequenceData')[0]
        
        if not doRemoveDatabaseDataNode:
            self._parseSequenceDataNode( sequenceDataNode ) 
        
        # -----------------------------------------------------
        # get sequence nodes
        structureNode = sequenceDataNode.getElementsByTagName('structure')[0]
        assetTypesNode = sequenceDataNode.getElementsByTagName('assetTypes')[0]
        shotDataNodes = sequenceDataNode.getElementsByTagName('shotData')
        
        doConvertionToShotData = False
        
        if len(shotDataNodes) == 0:
            doConvertionToShotData = True
        
        # parse all nodes
        self._parseAssetTypesNode(assetTypesNode)
        self._parseStructureNode(structureNode)
        
        if doConvertionToShotData:
            # 
            # it should be an old type of settings file
            # convert it to the new shotData concept
            # 
            shotListNode = sequenceDataNode.getElementsByTagName('shotList')[0]
            #print "converting to shotData concept !!!"
            
            # read the shot numbers from the shotList node and create appropriate
            # shot data nodes
            
            # parse the shotListNode to get the shot list
            self._parseShotListNode( shotListNode )
            
            self._convertShotListToShotData()
            
            # update the settings file
            #self.saveSettings()
            self._settings_dirty = True
        else:
            self._parseShotDataNode( shotDataNodes[0] )
        
        if doRemoveDatabaseDataNode:
            # just save the settings over it self, it should be fine
            #self.saveSettings()
            self._settings_dirty
        
        if self._settings_dirty:
            self.saveSettings()
    
    
    
    #----------------------------------------------------------------------
    def _parseSequenceDataNode(self, sequenceDataNode ):
        """parses sequenceDataNode nodes attributes
        """
        
        #assert( isinstance( sequenceDataNode, minidom.Element) )
        
        self._shotPrefix = sequenceDataNode.getAttribute('shotPrefix')
        self._shotPadding = int( sequenceDataNode.getAttribute('shotPadding') )
        self._revPrefix = sequenceDataNode.getAttribute('revPrefix')
        self._revPadding = sequenceDataNode.getAttribute('revPadding')
        self._verPrefix = sequenceDataNode.getAttribute('verPrefix')
        self._verPadding = sequenceDataNode.getAttribute('verPadding')
        
        #if sequenceDataNode.hasAttribute('extensionsToIgnore'):
            #self._extensionsToIgnore = sequenceDataNode.getAttribute('extensionsToIgnore').split(',')
        
        if sequenceDataNode.hasAttribute('noSubNameField'):
            self._noSubNameField = bool( eval( sequenceDataNode.getAttribute('noSubNameField') ) )
        
        if sequenceDataNode.hasAttribute('timeUnit'):
            self._timeUnit = sequenceDataNode.getAttribute('timeUnit')
    
    
    
    #----------------------------------------------------------------------
    def _parseStructureNode(self, structureNode):
        """parses structure node from the XML file
        """
        
        #assert( isinstance( structureNode, minidom.Element ) )
        
        # -----------------------------------------------------
        # get shot dependent/independent folders
        shotDependentFoldersNode = structureNode.getElementsByTagName('shotDependent')[0]
        shotDependentFoldersList = shotDependentFoldersNode.childNodes[0].wholeText.split('\n')
        
        shotIndependentFoldersNode = structureNode.getElementsByTagName('shotIndependent')[0]
        shotIndependentFoldersList = shotIndependentFoldersNode.childNodes[0].wholeText.split('\n')
        
        # strip the elements and remove empty elements
        shotDependentFoldersList = [ folder.strip() for folder in shotDependentFoldersList if folder.strip() != ""  ]
        shotIndependentFoldersList = [ folder.strip() for folder in shotIndependentFoldersList if folder.strip() != ""  ]
        
        # fix path issues for windows
        osName = os.name
        
        if osName=='nt':
            shotDependentFoldersList = [ oyAux.fixWindowsPath(path) for path in shotDependentFoldersList]
            shotIndependentFoldersList = [ oyAux.fixWindowsPath(path) for path in shotIndependentFoldersList]
        
        # set the structure
        self._structure.shotDependentFolders = shotDependentFoldersList
        self._structure.shotIndependentFolders = shotIndependentFoldersList
        
        
        try:
            # --------------------------------------------------------------------
            # THIS PART BELOW IS DEPRECATED REMOVE IT IN THE NEXT RELEASE
            # --------------------------------------------------------------------
            # read the output folders node
            outputFoldersNode = \
                structureNode.getElementsByTagName('outputFolders')[0]
            
            outputNodes = outputFoldersNode.getElementsByTagName('output')
            
            for outputNode in outputNodes:
                #assert(isinstance(outpuNode, minidom.Element))
                name = outputNode.getAttribute('name')
                path = outputNode.getAttribute('path')
                
                # fixe path issues for windows
                if osName == 'nt':
                    path = oyAux.fixWindowsPath( path )
                
                # instead add the output folder to the asset types
                # get the asset type by name and append the path to the
                # output folder of the found asset type
                aType = self.getAssetTypeWithName(name)
                try:
                    aType.output_path = path
                except AttributeError:
                    # it means there is no asset type with the given name
                    pass
                
            # do a saveSettings to save the settings in new format
            #self.saveSettings()
            self._settings_dirty = True
        
        except IndexError:
            # there is no output_folder in this project so don't parse it in
            # this way
            pass
    
    
    
    #----------------------------------------------------------------------
    def _parseAssetTypesNode(self, assetTypesNode):
        """parses assetTypes node from the XML file
        """
        
        #assert( isinstance( assetTypesNode, minidom.Element) )
        
        # -----------------------------------------------------
        # read asset types
        self._assetTypes = [] * 0
        for node in assetTypesNode.getElementsByTagName('type'):
            #assert( isinstance( node, minidom.Element) )
            
            name = node.getAttribute('name')
            path = node.getAttribute('path')
            shotDependency = bool(int(node.getAttribute('shotDependent')))
            environments = node.getAttribute('environments').split(",")
            output_path = node.getAttribute("output_path")
            
            # fix path issues for windows
            if os.name == 'nt':
                path = oyAux.fixWindowsPath(path)
            
            self._assetTypes.append(
                asset.AssetType(name, path, shotDependency, environments,
                                output_path)
            )
    
    
    
    #----------------------------------------------------------------------
    def _parseShotListNode(self, shotListNode):
        """parses shotList node from the XML file
        """
        
        #assert( isinstance( shotListNode, minidom.Element) )
        
        # -----------------------------------------------------
        # get shot list only if the current shot list is empty
        if len(self._shotList) == 0:
            if len(shotListNode.childNodes):
                self._shotList  = [ shot.strip() for shot in shotListNode.childNodes[0].wholeText.split('\n') if shot.strip() != "" ]
        
        # sort the shot list
        self._shotList = utils.sort_string_numbers( self._shotList )
    
    
    
    #----------------------------------------------------------------------
    def _parseShotDataNode(self, shotDataNode):
        """parses shotData node from the XML file
        """
        
        #assert( isinstance( shotDataNode, minidom.Element) )
        
        for shotNode in shotDataNode.getElementsByTagName('shot'):
            #assert( isinstance( shotNode, minidom.Element ) )
            
            startFrame = shotNode.getAttribute( 'startFrame' )
            endFrame = shotNode.getAttribute( 'endFrame' )
            name = shotNode.getAttribute( 'name' )
            description = shotNode.getElementsByTagName('description')[0].childNodes[0].wholeText.strip()
            
            if startFrame != '':
                startFrame = int(startFrame)
            else:
                startFrame = 0
            
            if endFrame != '':
                endFrame = int(endFrame)
            else:
                endFrame = 0
            
            # create shot objects with the data
            newShot = Shot( name, self, startFrame, endFrame,  description )
            #newShot.startFrame = startFrame
            #newShot.endFrame = endFrame
            #newShot.name = name
            #newShot.description = description
            
            # append the shot to the self._shots
            self._shots.append( newShot )
            
            # also append the name to the shotList
            self._shotList.append( name )
        
        # sort the shot list
        self._sortShots()
        
    
    
    #----------------------------------------------------------------------
    def _convertShotListToShotData(self):
        """converts the shot list node in the settings to shotData node
        """
        
        # now we should have the self._shotList filled
        # create the shot objects with default values and the shot names from
        # the shotList
        
        for shotName in self._shotList:
            newShot = Shot( shotName, self )
            #newShot.name = shotName
            self._shots.append( newShot )
    
    
    
    #----------------------------------------------------------------------
    def saveSettings(self):
        """saves the settings as XML
        """
        
        # create nodes
        rootNode = minidom.Element('root')
        sequenceDataNode = minidom.Element('sequenceData')
        structureNode = minidom.Element('structure')
        shotDependentNode = minidom.Element('shotDependent')
        shotDependentNodeText = minidom.Text()
        shotIndependentNode = minidom.Element('shotIndependent')
        shotIndependentNodeText = minidom.Text()
        assetTypesNode = minidom.Element('assetTypes')
        typeNode = minidom.Element('type')
        
        #shotListNode = minidom.Element('shotList')
        #shotListNodeText = minidom.Text()
        
        shotDataNode = minidom.Element('shotData')
        
        
        
        #----------------------------------------------------------------------
        # SEQUENCE DATA and children
        #----------------------------------------------------------------------
        # set repository node attributes
        sequenceDataNode.setAttribute('shotPrefix', self._shotPrefix)
        sequenceDataNode.setAttribute('shotPadding', unicode( self._shotPadding ) )
        sequenceDataNode.setAttribute('revPrefix', self._revPrefix)
        sequenceDataNode.setAttribute('revPadding', unicode( self._revPadding ) )
        sequenceDataNode.setAttribute('verPrefix', self._verPrefix)
        sequenceDataNode.setAttribute('verPadding', unicode( self._verPadding ) )
        sequenceDataNode.setAttribute('timeUnit', self._timeUnit )
        
        if self._noSubNameField:
            sequenceDataNode.setAttribute('noSubNameField', unicode( self._noSubNameField ) )
        #----------------------------------------------------------------------
        
        
        
        
        #----------------------------------------------------------------------
        # SHOT DEPENDENT / INDEPENDENT FOLDERS
        #----------------------------------------------------------------------
        # create shot dependent/independent folders
        shotDependentNodeText.data = '\n'.join( self._structure.shotDependentFolders ).replace('\\','/')
        shotIndependentNodeText.data = '\n'.join( self._structure.shotIndependentFolders ).replace('\\','/')
        #----------------------------------------------------------------------
        
        
        
        #----------------------------------------------------------------------
        # SHOT DATA
        #----------------------------------------------------------------------
        
        # sort the list before saving
        self._sortShots()
        
        # create the new type of shotData nodes
        for shot in self._shots:
            # create a shot node
            #assert(isinstance(shot,Shot))
            shotNode = minidom.Element('shot')
            shotNode.setAttribute('startFrame', str(shot.startFrame) )
            shotNode.setAttribute('endFrame', str(shot.endFrame) )
            shotNode.setAttribute('name', shot.name)
            
            # create a description node and store the shot description as the node text
            descriptionNode = minidom.Element('description')
            
            # create the text node
            descriptionText = minidom.Text()
            descriptionText.data = shot.description
            
            # append the nodes to appropriate parents
            descriptionNode.appendChild( descriptionText )
            shotNode.appendChild( descriptionNode )
            shotDataNode.appendChild( shotNode )
        #----------------------------------------------------------------------
        
        
        
        #----------------------------------------------------------------------
        # ASSET TYPE
        #----------------------------------------------------------------------
        
        # create asset types
        for aType in self._assetTypes:
            #assert( isinstance( aType, asset.AssetType ) )
            typeNode = minidom.Element('type')
            typeNode.setAttribute("name", aType.name )
            typeNode.setAttribute("path", aType.path.replace("\\","/"))
            
            typeNode.setAttribute("shotDependent",
                                  unicode(int(aType.isShotDependent)))
            
            typeNode.setAttribute("environments", ",".join(aType.environments))
            typeNode.setAttribute("output_path",
                                  aType.output_path.replace("\\", "/"))
            
            assetTypesNode.appendChild( typeNode )
        #----------------------------------------------------------------------
        
        
        
        # append children
        rootNode.appendChild(sequenceDataNode)
        
        sequenceDataNode.appendChild(structureNode)
        sequenceDataNode.appendChild(assetTypesNode)
        sequenceDataNode.appendChild(shotDataNode)
        
        structureNode.appendChild(shotDependentNode)
        structureNode.appendChild(shotIndependentNode)
        
        shotDependentNode.appendChild(shotDependentNodeText)
        shotIndependentNode.appendChild(shotIndependentNodeText)
        
        # create XML file
        settingsXML = minidom.Document()
        settingsXML.appendChild(rootNode)
        
        try:
            # if there is a settings file backit up
            # keep maximum of 5 backups
            oyAux.backupFile(self._settings_file_full_path, 5)
            #print "settingsFileFullPath: ", self._settings_file_full_path
            settingsFile = open(self._settings_file_full_path, "w")
            #os.chmod
        except IOError:
            #print "couldn't open the settings file"
            pass
        finally:
            settingsXML.writexml(settingsFile, "\t", "\t", "\n")
            settingsFile.close()
            self._settingsFileExists = True
            self._settings_dirty = False
        
        return
    
    
    
    #----------------------------------------------------------------------
    @property
    def shotPadding(self):
        """returns teh shotPadding
        """
        return self._shotPadding
    
    
    
    #----------------------------------------------------------------------
    @property
    def shotPrefix(self):
        """returns the shotPrefix
        """
        return self._shotPrefix
    
    
    
    #----------------------------------------------------------------------
    def create(self):
        """creates the sequence
        """
        
        # if the sequence doesn't exist create the folder
        
        if not self._exists:
            # create a folder with sequenceName
            utils.mkdir(self._fullPath)
            
            # copy the settings file to the root of the sequence
            shutil.copy(self._repository.default_settings_file_full_path,
                        self._settings_file_full_path)
        
        # just read the structure from the XML
        self.readSettings()
        
        # tell the sequence to create its own structure
        self.createStructure()
        
        # and create the shots
        self.createShots()
        
        # copy any file to the sequence
        # (like workspace.mel)
        
        for _fileInfo in self._repository.defaultFiles:
            sourcePath = os.path.join( _fileInfo[2], _fileInfo[0] )
            targetPath = os.path.join( self._fullPath, _fileInfo[1], _fileInfo[0] )
            
            shutil.copy( sourcePath, targetPath )
    
    
    
    #----------------------------------------------------------------------
    def addShots(self, shots ):
        """adds new shots to the sequence
        
        shots should be a range in on of the following format:
        #
        #,#
        #-#
        #,#-#
        #,#-#,#
        #-#,#
        etc.
        
        you need to invoke self.createShots to make the changes permenant
        """
        
        # for now consider the shots as a string of range
        # do the hard work later
        
        newShotsList = utils.convertRangeToList( shots )
        
        # convert the list to strings
        newShotsList = map(str, newShotsList)
        
        # add the shotList to the current _shotList
        self._shotList.extend(newShotsList)
        self._shotList = utils.unique(self._shotList)
        
        # sort the shotList
        self._shotList = utils.sort_string_numbers(self._shotList)
        
        # just create shot objects with shot name and leave the start and end frame and
        # description empty, it will be edited later
        newShotObjects = []
        
        
        # create a shot names buffer
        shotNamesBuffer = [shot.name for shot in self.shots]
        
        for shotName in newShotsList:
            # check if the shot allready exists
            if shotName not in shotNamesBuffer:
                shot = Shot( shotName, self )
                newShotObjects.append( shot )
        
        # add the new shot objects to the existing ones
        self._shots.extend(newShotObjects)
        
        # sort the shot objects
        self._shots = utils.sort_string_numbers( self._shots )
    
    
    
    #----------------------------------------------------------------------
    def addAlternativeShot(self, shotNumber):
        """adds a new alternative to the given shot
        
        you need to invoke self.createShots to make the changes permanent
        
        returns the alternative shot number
        """
        
        # shotNumber could be an int convert it to str
        shotNumberAsString = str(shotNumber)
        
        # get the first integer as int in the string
        shotNumber = oyAux.embedded_numbers( shotNumberAsString )[1]
        
        # get the next available alternative shot number for that shot
        alternativeShotName = self.getNextAlternateShotName( shotNumber )
        
        # add that alternative shot to the shot list
        if alternativeShotName != None:
            self._shotList.append( alternativeShotName )
            
            # create a new shot object
            alternativeShot = Shot( alternativeShotName, self )
            self._shots.append( alternativeShot )
            
        return alternativeShotName
    
    
    
    #----------------------------------------------------------------------
    def getNextAlternateShotName(self, shot):
        """returns the next alternate shot number for the given shot number
        """
        
        # get the shot list
        shotList = self.shotList
        alternateLetters = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
        
        for letter in alternateLetters:
            #check if the alternate is in the list
            
            newShotNumber = str(shot) + letter
            
            if not newShotNumber in shotList:
                return newShotNumber
        
        return None
    
    
    
    #----------------------------------------------------------------------
    def createShots(self):
        """creates the shot folders in the structure
        """
        if not self._exists:
            return
        
        #for folder in self._shotFolders:
        for folder in self._structure.shotDependentFolders:
            for shotNumber in self._shotList:
                # get a shotString for that number
                shotString = self.convertToShotString( shotNumber )
                
                # create the folder with that name
                shotFullPath = os.path.join ( self._fullPath, folder, shotString )
                
                oyAux.createFolder( shotFullPath )
    
    
    
    ##----------------------------------------------------------------------
    #@property
    #def shotFolders(self):
        #"""returns the shot folder paths
        #"""
        #if not self._exists:
            #return
        
        #return self._structure.shotDependentFolders
    
    
    
    #----------------------------------------------------------------------
    @property
    def shots(self):
        """returns the shot objects as a list
        """
        return self._shots
    
    
    
    #----------------------------------------------------------------------
    def _sortShots(self):
        """sorts the internal shot list
        """
        self._shots = sorted( self._shots, key = oyAux.embedded_numbers )
    
    
    
    #----------------------------------------------------------------------
    def getShot(self, shotNumber):
        """returns the shot with given shotNumber
        """
        
        for shot in self._shots:
            assert(isinstance(shot, Shot))
            if shot.name == shotNumber:
                return shot
        
        return None
    
    
    
    #----------------------------------------------------------------------
    @property
    def shotList(self):
        """returns the shot list object
        """
        return self._shotList
    
    
    
    #----------------------------------------------------------------------
    @property
    def structure(self):
        """returns the structure object
        """
        return self._structure
    
    
    
    #----------------------------------------------------------------------
    def createStructure(self):
        """creates the folders defined by the structure
        """
        if not self._exists:
            return
        
        createFolder = oyAux.createFolder
        
        # create the structure
        for folder in self._structure.shotDependentFolders:
            createFolder( os.path.join( self._fullPath, folder ) )
        
        for folder in self._structure.shotIndependentFolders:
            createFolder( os.path.join( self._fullPath, folder ) )
    
    
    
    #----------------------------------------------------------------------
    def convertToShotString(self, shotNumber ):
        """ converts the input shot number to a padded shot string
        
        for example it converts:
        1   --> SH001
        10  --> SH010
        
        if there is an alternate letter it will add it to the end of the
        shot string, like:
        1a  --> SH001A
        10S --> SH010S
        
        it also properly converts inputs like this
        abc92a --> SH092A
        abc323d432e --> SH323D
        abc001d --> SH001D
        
        if the shotNumber argument is None it will return None
        
        for now it can't convert properly if there is more than one letter at the end like:
        abc23defg --> SH023DEFG
        """
        
        pieces = oyAux.embedded_numbers( unicode(shotNumber) )
        
        if len(pieces) <= 1:
            return None
        
        number = pieces[1]
        alternateLetter = pieces[2]
        
        return self._shotPrefix + oyAux.padNumber( number, self._shotPadding ) + alternateLetter.upper()
    
    
    
    #----------------------------------------------------------------------
    def convertToRevString(self, revNumber):
        """converts the input revision number to a padded revision string
        
        for example it converts:
        1  --> r01
        10 --> r10
        """
        return self._revPrefix + oyAux.padNumber( revNumber, self._revPadding )
    
    
    
    #----------------------------------------------------------------------
    def convertToVerString(self, verNumber):
        """converts the input version number to a padded version string
        
        for example it converts:
        1  --> v001
        10 --> v010
        """
        return self._verPrefix + oyAux.padNumber( verNumber, self._verPadding )
    
    
    
    #----------------------------------------------------------------------
    def convertToShotNumber(self, shotString):
        """beware that it returns a string, it returns the number plus the alternative
        letter (if exists) as a string
        
        for example it converts:
        
        SH001 --> 1
        SH041a --> 41a
        etc.
        """
        
        # remove the shot prefix
        remainder = shotString[ len(self._shotPrefix) : len(shotString) ]
        
        # get the integer part
        matchObj = re.match('[0-9]+',remainder)
        
        if matchObj:
            numberAsStr = matchObj.group()
        else:
            return None
        
        alternateLetter = ''
        if len(numberAsStr) < len(remainder):
            alternateLetter = remainder[len(numberAsStr):len(remainder)]
        
        # convert the numberAsStr to a number then to a string then add the alternate letter
        return unicode(int(numberAsStr)) + alternateLetter
    
    
    
    #----------------------------------------------------------------------
    def convertToRevNumber(self, revString):
        """converts the input revision string to a revision number
        
        for example it converts:
        r01 --> 1
        r10 --> 10
        """
        return int(revString[len(self._revPrefix):len(revString)])
    
    
    
    #----------------------------------------------------------------------
    def convertToVerNumber(self, verString):
        """converts the input version string to a version number
        
        for example it converts:
        v001 --> 1
        v010 --> 10
        """
        return int(verString[len(self._verPrefix):len(verString)])
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def getAssetTypes(self, environment):
        """returns a list of AssetType objects that this project has
        
        if the environment is set something other then None only the assetTypes
        for that environment is returned
        """
        
        if environment==None:
            return self._assetTypes
        else:
            aTypesList = [] * 0
            
            for aType in self._assetTypes:
                #assert(isinstance(aType, asset.AssetType) )
                if environment in aType.environments:
                    aTypesList.append( aType )
            
            return aTypesList
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def getAssetTypeWithName(self, typeName):
        """returns the assetType object that has the name typeName.
        if it can't find any assetType that has the name typeName it returns None
        """
        
        for aType in self._assetTypes:
            if aType.name == typeName:
                return aType
        
        return None
    
    
    
    #----------------------------------------------------------------------
    @property
    def path(self):
        """returns the path of the sequence
        """
        return self._path
    
    
    
    #----------------------------------------------------------------------
    @property
    def fullPath(self):
        """returns the full path of the sequence
        """
        return self._fullPath
    
    
    
    #----------------------------------------------------------------------
    @property
    def project(self):
        """returns the parent project
        """
        return self._project
    
    
    
    #----------------------------------------------------------------------
    @property
    def projectName(self):
        """returns the parent projects name
        """
        return self._project.name
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache(expire=60)
    def getAssetFolders(self):
        """returns all asset folders
        """
        
        # look at the assetType folders
        assetFolders = [] * 0
        
        for aType in self._assetTypes:
            #assert(isinstance(aType, AssetType))
            assetFolders.append( aType.path )
        
        return assetFolders
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache(expire=60)
    def getAllAssets(self):
        """returns Asset objects for all the assets of the sequence
        beware that this method uses a very simple caching algorithm, so it
        tries to reduce file system overhead
        """
        
        # get asset folders
        # look at the child folders
        # and then look at the files under the child folders
        # if a file starts with the folder name
        # mark it as an asset
        
        assets = [] * 0
        
        # get the asset folders
        assetFolders = self.getAssetFolders()
        
        
        # optimization variables
        osPathJoin = os.path.join
        oyAuxGetChildFolders = oyAux.getChildFolders
        osPathBaseName = os.path.basename
        osPathIsDir = os.path.isdir
        globGlob = glob.glob
        assetAsset = asset.Asset
        assetsAppend = assets.append
        selfFullPath = self._fullPath
        selfProject = self.project
        
        # for each folder search child folders
        for folder in assetFolders:
            fullPath = osPathJoin( selfFullPath, folder)
            
            # 
            # skip if the folder doesn't exists
            # 
            # it is a big problem in terms of management but some old type projects
            # has missing folders, because the folders will be created whenever somebody
            # uses that folder while saving an asset, we don't care about its non existancy
            #
            #if not os.path.exists( fullPath ):
##            if not osPathExists( fullPath ):
##                continue
            
            # use glob instead of doing it by hand
            childFolders = oyAuxGetChildFolders( fullPath, True )
            
            for folder in childFolders:
                # get possible asset files directly by using glob
                pattern = osPathBaseName( folder ) + '*'
                
                # files are in fullpath format
                matchedFiles = [ file_ for file_ in globGlob( osPathJoin( folder, pattern ) ) if not osPathIsDir(file_) ]
                
                matchedFileCount = len(matchedFiles)
                
                if matchedFileCount > 0:
                    # there should be some files matching the pattern
                    # check if they are valid assets
                    
                    matchedAssets = map( assetAsset, [selfProject] * matchedFileCount, [self] * matchedFileCount, map(osPathBaseName, matchedFiles) )
                    
                    # append them to the main assets list
                    [ assetsAppend(matchedAsset) for matchedAsset in matchedAssets if matchedAsset.isValidAsset ]
        
        return assets
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def getAllAssetsForType(self, typeName):
        """returns Asset objects for just the given type of the sequence
        """
        
        # get asset folders
        # look at the child folders
        # and then look at the files under the child folders
        # if a file starts with the folder name
        # mark it as an asset
        
        assets = [] * 0
        
        # get the asset folders
        #assetFolders = self.getAssetFolders()
        
        aType = self.getAssetTypeWithName( typeName )
        
        #assert(isinstance(aType,asset.AssetType))
        assetFolder = aType.path
        
        # optimization variables
        osPathExists = os.path.exists
        osPathJoin = os.path.join
        osPathIsDir = os.path.isdir
        oyAuxGetChildFolders = oyAux.getChildFolders
        osPathBaseName = os.path.basename
        globGlob = glob.glob
        assetAsset = asset.Asset
        assetsAppend = assets.append
        selfFullPath = self._fullPath
        selfProject = self.project
        
        fullPath = osPathJoin( selfFullPath, assetFolder)
        
        # 
        # skip if the folder doesn't exists
        # 
        # it is a big problem in terms of management but some old type projects
        # has missing folder, because the folders will be created whenever somebody
        # uses that folder while saving an asset, we don't care about its non existancy
        #
        #if not os.path.exists( fullPath ):
        if not osPathExists( fullPath ):
            return []
        
        # use glob instead of doing it by hand
        childFolders = oyAuxGetChildFolders( fullPath, True )
        
        for folder in childFolders:
            # get possible asset files directly by using glob
            pattern = osPathBaseName( folder ) + '*'
            
            # files are in fullpath format
            matchedFiles = [ file_ for file_ in globGlob( osPathJoin( folder, pattern ) ) if not osPathIsDir(file_)]
            
            matchedFileCount = len(matchedFiles)
            
            if matchedFileCount > 0:
                # there should be some files matching the pattern
                # check if they are valid assets
                
                matchedAssets = map( assetAsset, [selfProject] * matchedFileCount, [self] * matchedFileCount, map(osPathBaseName, matchedFiles) )
                
                # append them to the main assets list
                [ assetsAppend(matchedAsset) for matchedAsset in matchedAssets if matchedAsset.isValidAsset ]
        return assets
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def getAllAssetFileNamesForType(self, typeName):
        """returns Asset objects for just the given type of the sequence
        """
        
        # get asset folders
        # look at the child folders
        # and then look at the files under the child folders
        # if a file starts with the folder name
        # mark it as an asset
        
        assetFiles = []
        
        # get the asset folders
        aType = self.getAssetTypeWithName( typeName )
        
        #assert(isinstance(aType,asset.AssetType))
        assetFolder = aType.path
        
        # optimization variables
        osPathExists = os.path.exists
        osPathJoin = os.path.join
        osPathBaseName = os.path.basename
        osPathIsDir = os.path.isdir
        globGlob = glob.glob
        assetFilesAppend = assetFiles.append
        selfFullPath = self._fullPath
        selfProject = self.project
        
        fullPath = osPathJoin( selfFullPath, assetFolder)
        
        # 
        # skip if the folder doesn't exists
        # 
        # it is a big problem in terms of management but some old type projects
        # has missing folder, because the folders will be created whenever somebody
        # uses that folder while saving an asset, we don't care about its non existancy
        #
        #if not os.path.exists( fullPath ):
        if not osPathExists( fullPath ):
            return []
        
        childFolders = oyAux.getChildFolders( fullPath, True )
        
        for folder in childFolders:
            pattern = osPathBaseName( folder ) + '_*'
            
            matchedFiles = [ file_ for file_ in globGlob( osPathJoin( folder, pattern ) ) if not osPathIsDir(file_) ]
            
            matchedFileCount = len( matchedFiles )
            
            if matchedFileCount > 0:
                #[ assetFilesAppend(matchedFile) for matchedFile in matchedFiles if self.isValidExtension( os.path.splitext(matchedFile)[1].split('.')[1] ) ]
                #map( assetFilesAppend, matchedFiles )
                assetFiles.extend( matchedFiles )
        
        assetFiles = map( os.path.basename, assetFiles )
        
        return assetFiles
    
    
    
    #----------------------------------------------------------------------
    def getAssetBaseNamesForType(self, typeName):
        """returns all asset baseNames for the given type
        """
        
        # get the asset files of that type
        allAssetFileNames = self.getAllAssetFileNamesForType( typeName )
        
        # filter for base name
        sGFIV = self.generateFakeInfoVariables
        baseNamesList = [ sGFIV(assetFileName)['baseName'] for assetFileName in allAssetFileNames ]
        
        # remove duplicates
        baseNamesList = oyAux.unique( baseNamesList )
        
        return baseNamesList
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def getAllAssetsForTypeAndBaseName(self, typeName, baseName):
        """returns Asset objects of the sequence for just the given type and basename
        """
        
        # get asset folders
        # look at the child folders
        # and then look at the files under the child folders
        # if a file starts with the folder name
        # mark it as an asset
        
        assets = [] * 0
        
        # get the asset folder
        aType = self.getAssetTypeWithName( typeName )
        assetFolder = aType.path
        
        # optimization variables
        osPathJoin = os.path.join
        osPathExists = os.path.exists
        osPathIsDir = os.path.isdir
        selfFullPath = self._fullPath
        assetAsset = asset.Asset
        selfProject = self._project
        assetsAppend = assets.append
        
        osPathBaseName = os.path.basename
        globGlob = glob.glob
        
        fullPath = osPathJoin( selfFullPath, assetFolder)
        
        # 
        # skip if the folder doesn't exists
        # 
        # it is a big problem in terms of management but some old type projects
        # has missing folder, because the folders will be created whenever somebody
        # uses that folder while saving an asset, we don't care about its non existancy
        #
        if not osPathExists( fullPath ):
            return []
        
        childFolder = baseName
        childFolderFullPath = osPathJoin( fullPath, childFolder )
        
        # use glob instead of doing it by hand
        
        # get possible asset files directly by using glob
        pattern = osPathBaseName( baseName ) + '_*'
        
        # files are in fullpath format
        matchedFiles = [ file_ for file_ in globGlob( osPathJoin( childFolderFullPath, pattern ) ) if not osPathIsDir(file_) ]
        
        matchedFileCount = len(matchedFiles)
        
        if matchedFileCount > 0:
            # there should be some files matching the pattern
            # check if they are valid assets
            
            matchedAssets = map( assetAsset, [selfProject] * matchedFileCount, [self] * matchedFileCount, map(osPathBaseName, matchedFiles) )
            
            # append them to the main assets list
            [ assetsAppend(matchedAsset) for matchedAsset in matchedAssets if matchedAsset.isValidAsset ]
        
        return assets
    
    
    
    ##----------------------------------------------------------------------
    #def getAllBaseNamesForType(self, typeName):
        #"""
        #"""
        
        #aType = self.getAssetTypeWithName( typeName )
        
        ##assert(isinstance(aType,asset.AssetType))
        
        #typeFolder = aType.path
        
        #os.listdir( typeFolder )
    
    
    
    #----------------------------------------------------------------------
    def filterAssets(self, assetList, **kwargs):
        """filters the given asset list with the key word arguments
        
        the kwargs should have at least on of these keywords:
        
        baseName
        subName
        typeName
        rev
        revString
        ver
        verString
        userInitials
        notes
        fileName
        """
        
        newKwargs = dict()
        
        # remove empty keywords
        for k in kwargs:
            if kwargs[k] != '':
                newKwargs[k] = kwargs[k]
        
        # get all the info variables of the assets
        assetInfos = map( asset.Asset.infoVariables, assetList )
        
        filteredAssetInfos = self.aFilter( assetInfos, **kwargs)
        
        # recreate assets and return
        # TODO: return without recreating the assets
        return [ asset.Asset(self._project, self, x['fileName']) for x in filteredAssetInfos ]
    
    
    
    #----------------------------------------------------------------------
    def filterAssetNames(self, assetFileNames, **kwargs):
        """a fake filter for quick retrieval of infos from asset file names
        
        use filterAsset for filtering with asset objects as input
        
        the kwargs should have at least on of these keywords:
        
        baseName
        subName
        typeName
        """
        
        # generate dictionaries
        assetInfos = map( self.generateFakeInfoVariables, assetFileNames )
        
        filteredAssetFileNames = self.aFilter( assetInfos, **kwargs )
        
        return [ info['fileName'] for info in filteredAssetFileNames ]
    
    
    
    #----------------------------------------------------------------------
    def timeUnit():
        
        doc = "the time unit of the sequence"
        
        def fget(self):
            return self._timeUnit
        
        def fset(self, timeUnit):
            self._timeUnit = timeUnit
        
        return locals()
    
    timeUnit = property( **timeUnit() )
    
    
    
    #----------------------------------------------------------------------
    @bCache.cache()
    def generateFakeInfoVariables(self, assetFileName):
        """generates fake info variables from assetFileNames by splitting the file name
        from '_' characters and trying to get information from those splits
        """
        #assert(isinstance(assetFileName, str))
        splits = assetFileName.split('_') # replace it with data seperator
        
        infoVars = dict()
        
        infoVars['fileName'] = assetFileName
        infoVars['baseName'] = ''
        infoVars['subName'] = ''
        infoVars['typeName'] = ''
        
        if not self._noSubNameField:
            if len(splits) > 3:
                infoVars['baseName'] = splits[0]
                infoVars['subName'] = splits[1]
                infoVars['typeName'] = splits[2]
        else:
            if len(splits) > 2:
                infoVars['baseName'] = splits[0]
                infoVars['subName'] = ''
                infoVars['typeName'] = splits[1]
        
        return infoVars
    
    
    
    #----------------------------------------------------------------------
    def aFilter(self, dicts, **kwargs):
        """filters dictionaries for criteria
        dicts is a list of dictionaries
        the function returns the dictionaries that has all the kwargs
        """
        return [ d for d in dicts if all(d.get(k) == kwargs[k] for k in kwargs)]
    
    
    
    ##----------------------------------------------------------------------
    #@property
    #def invalidExtensions(self):
        #"""returns invalid extensions for the sequence
        #"""
        #return self._extensionsToIgnore
    
    
    
    ##----------------------------------------------------------------------
    #@bCache.cache()
    #def isValidExtension(self, extensionString):
        #"""checks if the given extension is in extensionsToIgnore list
        #"""
        
        #if len(self._extensionsToIgnore) == 0 :
            ## no extensions to ignore
            #return True
        
        ##assert(isinstance(extensionString,str))
        
        #if extensionString.lower() in self._extensionsToIgnore:
            #return False
        
        #return True
    
    
    #----------------------------------------------------------------------
    def isValid(self):
        """checks if the sequence is valid
        """
        
        # a valid should:
        # - be exist
        # - have a .settings.xml file inside it
        
        if self._exists and self._settingsFileExists:
            return True
        
        return False
    
    
    
    ##----------------------------------------------------------------------
    #def addExtensionToIgnoreList(self, extension):
        #"""adds new extension to ignore list
        
        #you need to invoke self.saveSettings to make the changes permenant
        #"""
        #self._extensionsToIgnore.append( extension )
    
    
    
    ##----------------------------------------------------------------------
    #def removeExtensionFromIgnoreList(self, extension):
        #"""remove the extension from the ignroe list
        
        #you need to invoke self.saveSettings to make the changes permenant
        #"""
        
        #if extension in self._extensionsToIgnore:
            #self._extensionsToIgnore.remove( extension )
    
    
    
    #----------------------------------------------------------------------
    @property
    def revPadding(self):
        """returns the revPadding
        """
        return self._revPadding
    
    
    
    #----------------------------------------------------------------------
    @property
    def revPrefix(self):
        """returns the revPrefix
        """
        return self._revPrefix
    
    
    
    #----------------------------------------------------------------------
    def addNewAssetType(self, name='', path='', shotDependent=False,
                        environments=None, output_path=""):
        """adds a new asset type to the sequence
        
        you need to invoke self.saveSettings to make the changes permenant
        """
        
        assert(isinstance(environments, list))
        
        # check if there is allready an assetType with the same name
        
        # get the names of the asset types and convert them to upper case
        assetTypeName = [assetType.name.upper()
                         for assetType in self._assetTypes]
        
        if name.upper() not in assetTypeName:
            # create the assetType object with the input
            newAType = asset.AssetType(name, path, shotDependent, environments)
            
            # add it to the list
            self._assetTypes.append(newAType)
    
    
    
    #----------------------------------------------------------------------
    @property
    def exists(self):
        """returns True if the sequence itself exists, False otherwise
        """
        return self._exists
    
    
    
    #----------------------------------------------------------------------
    @property
    def name(self):
        """returns the sequence name
        """
        return self._name
        
    
    
    #----------------------------------------------------------------------
    @property
    def noSubNameField(self):
        """returns True if the sequence doesn't support subName fields (old-style)
        """
        return self._noSubNameField
    
    
    
    #----------------------------------------------------------------------
    @property
    def verPadding(self):
        """rerturns the verPadding
        """
        return self._verPadding
    
    
    
    #----------------------------------------------------------------------
    @property
    def verPrefix(self):
        """returns the verPrefix
        """
        return self._verPrefix
        
    
    
    #----------------------------------------------------------------------
    def undoChange(self):
        """undos the last change to the .settings.xml file if there is a
        backup of the .settings.xml file
        """
        
        # get the backup files of the .settings.xml
        backupFiles = oyAux.getBackupFiles(self._settings_file_full_path)
        
        if len(backupFiles) > 0 :
            #print backupFiles
            # there is at least one backup file
            # delete the current .settings.xml
            # and rename the last backup to .settings.xml
            
            print "replacing with : ", os.path.basename( backupFiles[-1] )
            
            shutil.copy(backupFiles[-1], self._settings_file_full_path)
            os.remove(backupFiles[-1])
    
    
    
    #----------------------------------------------------------------------
    def __eq__(self, other):
        """The equality operator
        """
        
        return isinstance(other, Sequence) and other.name == self.name and \
               other.projectName == self.projectName
    
    
    
    #----------------------------------------------------------------------
    def __ne__(self, other):
        """The in equality operator
        """
        
        return not self.__eq__(other)






########################################################################
class Structure(object):
    """The class that helps to hold data about structures in a sequence.
    
    Structure holds data about shot dependent and shot independent folders.
    Shot dependent folders has shot folders, and the others not.
    
    This class is going to change a lot in the future releases and it is going
    to handle all the `project folder template` by using Jinja2 templates.
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self, shotDependentFolders=None, shotIndependentFolders=None):
        
        self._shotDependentFolders = shotDependentFolders # should be a list of str or unicode
        self._shotIndependentFolders = shotIndependentFolders # should be a list of str or unicode
    
    
    
    #----------------------------------------------------------------------
    def addShotDependentFolder(self, folderPath):
        """adds new shot dependent folder
        
        folderPath should be relative to sequence root
        """
        if folderPath not in self._shotDependentFolders:
            self._shotDependentFolders.append( folderPath )
            self._shotDependentFolders = sorted( self._shotDependentFolders )
    
    
    
    #----------------------------------------------------------------------
    def addShotIndependentFolder(self, folderPath):
        """adds new shot independent folder
        
        folderPath should be relative to sequence root
        """
        
        if folderPath not in self._shotIndependentFolders:
            self._shotIndependentFolders.append( folderPath )
            self._shotIndependentFolders = sorted( self._shotIndependentFolders )
    
    
    
    #----------------------------------------------------------------------
    def shotDependentFolders():
        
        doc = "the shot dependent folders"
        
        def fget(self):
            return self._shotDependentFolders
        
        def fset(self, shotDependentFolders):
            self._shotDependentFolders = shotDependentFolders
        
        return locals()
    
    shotDependentFolders = property( **shotDependentFolders() )
    
    
    
    #----------------------------------------------------------------------
    def shotIndependentFolders():
        
        doc = "shot independent folders"
        
        def fget(self):
            return self._shotIndependentFolders
        
        def fset(self, folders):
            self._shotIndependentFolders = folders
        
        return locals()
    
    shotIndependentFolders = property( **shotIndependentFolders() )
    
    
    
    #----------------------------------------------------------------------
    def removeShotDependentFolder(self, folderPath):
        """removes the shot dependent folder from the structure
        
        beware that if the parent sequence uses that folder as a assetType folder
        you introduce an error to the sequence
        """
        
        self._shotDependentFolders.remove( folderPath )
    
    
    
    #----------------------------------------------------------------------
    def removeShotIndependentFolder(self, folderPath):
        """removes the shot independent folder from the structure
        
        beware that if the parent sequence uses that folder as a assetType folder
        you introduce an error to the sequence
        """
        
        self._shotIndependentFolders.remove( folderPath )
    
    
    
    #----------------------------------------------------------------------
    def fixPathIssues(self):
        """fixes path issues in the folder data variables
        """
        
        # replaces "\" with "/"
        for i,folder in enumerate(self._shotDependentFolders):
            self._shotDependentFolders[i] = folder.replace('\\','/')
        
        for i,folder in enumerate(self._shotIndependentFolders):
            self._shotIndependentFolders[i] = folder.replace('\\','/')
    
    
    
    #----------------------------------------------------------------------
    def removeDuplicate(self):
        """removes any duplicate entry
        """
        
        # remove any duplicates
        self._shotDependentFolders = sorted(oyAux.unique(self._shotDependentFolders))
        self._shotIndependentFolders = sorted(oyAux.unique(self._shotIndependentFolders))






########################################################################
class Shot(object):
    """The class that enables the system to manage shot data.
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self, name , sequence=None, startFrame=1, endFrame=1, description=''):
        self._name = name
        self._duration = 1
        self._startFrame = startFrame
        self._endFrame = endFrame
        self._description = description
        self._sequence = sequence
        #self._cutSummary = ''
    
    
    
    #----------------------------------------------------------------------
    def __str__(self):
        """returns the string representation of the object
        """
        return self._name
    
    
    
    #def __repr__(self):
        #"""returns the representation of the class
        #"""
        #return "< oyProjectManager.models.project.Shot object: " + self._name + ">"
    
    
    
    #----------------------------------------------------------------------
    def startFrame():
        
        doc = "the start frame of the shot"
        
        def fget(self):
            return self._startFrame
        
        def fset(self, frame):
            self._startFrame = frame
            # update the duration
            self._updateDuration()
        
        return locals()
    
    startFrame = property( **startFrame() )
    
    
    
    #----------------------------------------------------------------------
    def endFrame():
        
        doc = "the end frame of the shot"
        
        def fget(self):
            return self._endFrame
        
        def fset(self, frame):
            self._endFrame = frame
            # update the duration
            self._updateDuration()
        
        return locals()
    
    endFrame = property( **endFrame() )
    
    
    
    #----------------------------------------------------------------------
    def _updateDuration(self):
        """updates the duration
        """
        self._duration = self._endFrame - self._startFrame + 1
    
    
    
    #----------------------------------------------------------------------
    def description():
        
        doc = "the shots description"
        
        def fget(self):
            return self._description
        
        def fset(self, description):
            self._description = description
        
        return locals()
    
    description = property( **description() )
    
    
    
    #----------------------------------------------------------------------
    def sequence():
        
        def fget(self):
            return self._sequence
        
        def fset(self, seq):
            self._sequence = seq
        
        return locals()
    
    sequence = property( **sequence() )
    
    
    
    #----------------------------------------------------------------------
    def name():
        
        def fget(self):
            return self._name
        
        def fset(self, name):
            self._name = name
        
        return locals()
    
    name = property( **name() )
    
    
    
    #----------------------------------------------------------------------
    @property
    def duration(self):
        """the duration
        """
        return self._duration