import os
import nuke
import oyAuxiliaryFunctions as oyAux
from oyProjectManager.dataModels import assetModel, projectModel, abstractClasses



__version__ = "10.3.11"






########################################################################
class NukeEnvironment(abstractClasses.Environment):
    """the nuke environment class
    """
    
    
    
    #----------------------------------------------------------------------
    def __init__(self, asset=None, name='', extensions=None ):
        """nuke spesific init
        """
        # call the supers __init__
        super(NukeEnvironment, self).__init__( asset, name, extensions )
        
        # and add you own modifications to __init__
        # get the root node
        self._root = self.getRootNode()
    
    
    
    #----------------------------------------------------------------------
    def getRootNode(self):
        """returns the root node of the current nuke session
        """
        
        return nuke.toNode("root")
    
    
    
    #----------------------------------------------------------------------
    def save(self):
        """"the save action for nuke environment
        
        uses Nukes own python binding
        """
        
        # set the extension to 'nk'
        self._asset.extension = 'nk'
        
        fullPath = self._asset.fullPath
        fullPath = fullPath.replace('\\','/')
        
        nuke.scriptSaveAs( fullPath )
        
        return True
    
    
    
    #----------------------------------------------------------------------
    def export(self):
        """the export action for nuke environment
        """
        
        # set the extension to 'nk'
        self._asset.extension = 'nk'
        
        fullPath = self._asset.fullPath
        
        # replace \\ with /
        fullPath = fullPath.replace('\\','/')
        
        nuke.nodeCopy( fullPath )
        
        return True
    
    
    
    #----------------------------------------------------------------------
    def open_(self, force=False):
        """the open action for nuke environment
        """
        
        fullPath = self._asset.fullPath
        
        # replace \\ with /
        fullPath = fullPath.replace('\\','/')
        
        nuke.scriptOpen( fullPath )
        return True
    
    
    
    #----------------------------------------------------------------------
    def import_(self):
        """the import action for nuke environment
        """
        
        fullPath = self._asset.fullPath
        
        # replace \\ with /
        fullPath = fullPath.replace('\\','/')
        
        nuke.nodePaste( fullPath )
        return True
    
    
    
    #----------------------------------------------------------------------
    def getPathVariables(self):
        """gets the file name from nuke
        """
        
        fullPath = path = fileName = None
        fullPath = self._root.knob('name').value()
        
        
        if fullPath != None and fullPath != '':
            # for winodws replace the path seperator
            if os.name == 'nt':
                fullPath = fullPath.replace('/','\\')
            
            fileName = os.path.basename( fullPath )
            path = os.path.dirname( fullPath )
        else:
            
            # use the last file from the recent file list
            fullPath = nuke.recentFile(1)
            
            # for winodws replace the path seperator
            if os.name == 'nt':
                fullPath = fullPath.replace('/','\\')
            
            fileName = os.path.basename( fullPath )
            path = os.path.dirname( fullPath )
            
        return fileName, path
    
    
    
    #----------------------------------------------------------------------
    def getFrameRange(self):
        """returns the current frame range
        """
        self._root = self.getRootNode()
        startFrame = int(self._root.knob('first_frame').value())
        endFrame = int(self._root.knob('last_frame').value())
        return startFrame, endFrame
    
    
    
    #----------------------------------------------------------------------
    def setFrameRange(self, startFrame=1, endFrame=100):
        """sets the start and end frame range
        """
        self._root = self.getRootNode()
        self._root.knob('first_frame').setValue(startFrame)
        self._root.knob('last_frame').setValue(endFrame)
    