# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger(__name__)

class Config(object):
    """config abstraction
    
    Idea comes from Sphinx config
    
    
    **config.py File**
    
    oyProjectManager uses the ``config.py`` to let one to customize the system
    config.
    
    The ``config.py`` file is searched in a couple of places through the
    system:
        
        * under "~/.oypmrc/" directory
        * under "$OYPROJECTMANAGER_PATH"
    
    The first path is a folder in the users home dir. The second one is a path
    defined by the ``OYPROJECTMANAGER_PATH`` environment variable.
    
    Defining the ``config.py`` by using the environment variable gives the most
    customizable and consistent setup through the studio. You can set
    ``OYPROJECTMANAGER_PATH`` to a shared folder in your fileserver where all
    the users can access.
    
    Because, ``config.py`` is a regular Python code which is executed by
    oyProjectManager, you can do anything you were doing in a normal Python
    script. This is very handy if you have another source of information which
    is reachable by a Python script.
    
    In config.py you can:
      
      * Add new users
      * Customize default project structure
      * Customize file naming convention
      * Customize path naming convention
      * Customize the database file name
      * Customize server paths
      * Customize environments (host programs running oyProjectManager)
      * and many more
    
    If there is no ``OYPROJECTMANAGER_PATH`` variable in your current
    environment or it is not showing an existing path or there is no
    ``config.py`` file the system will use the system defaults and it is
    probably not going to work efficiently.
    
    Sample usage is::
    
        from oyProjectManager import config
        conf = config.Config()
        
        print conf.database_file_name # will return .metadata.db
        
        # print all the user names defined in the config.py
        for user in conf.users:
            print user.name
    
    **About the Users**
    The users in the oyProjectManager is held in the config file as a python
    dictionary. You can add or remove users::
      
      users_data = [{"name": "Erkan Ozgur Yilmaz",
                     "initials":"eoy",
                     "email": "eoyilmaz@company.com"}]
    
    As seen in the above example the ``users_data`` variable is a python list
    holding python dictionary, and the dictionary has keys like name, initials
    and email.
    
    The users are created from the ``config.py`` file for UI, but the user data
    will be hold in the project based database (.metadata.db) if the user
    created a data for that project. So one project can have more users then
    others. ``config.users`` will return a list of
    :class:`~oyProjectManager.core.models.User` instances.
    
    **Config Variables**
    
    TODO: Add explanation of each variable
    
    database_url = "sqlite:///$REPO/.metadata.db"
    shot_number_prefix = "SH"
    shot_number_padding = 3
    
    rev_number_prefix = "r"
    rev_number_padding = 2
    
    ver_number_prefix = "v"
    ver_number_padding = 3
    
    fps = 25
    resolution_width = 1920
    resolution_height = 1080
    resolution_pixel_aspect = 1.0
    
    take_name = "MAIN"
    
    users_data = [{"name": "Administrator", "initials": "adm"}]
    
    repository = [
            {
                "name": "Default Projects Repository"
                "windows_path": "~/Projects",
                "linux_path": "~/Projects",
                "osx_path": "~/Projects"
            }
    ]
    
    environments = [
            {
                "name":"Maya",
                "extensions":["ma", "mb"]
            },
            {
                "name":"Houdini",
                "extensions":["hip"]
            },
            {
                "name":"Nuke",
                "extensions": ["nk"],
            },
            {
                "name":"Photoshop",
                "extensions": ["psd", "pdd"],
                "export_extensions": ["tif", "tga", "bmp", "jpg", "iff"],
            },
            {
                "name":"3DEqualizer",
                "extensions": ["3te"]
            }
        ]
        
    project_structure = 
    
    version_types =  
    """
    
    default_config_values = dict(
        
        database_url = "sqlite:///$REPO/.metadata.db",
        
        shot_number_prefix = "SH",
        shot_number_padding = 3,
        
        rev_number_prefix = "r",
        rev_number_padding = 2,
        
        ver_number_prefix = "v",
        ver_number_padding = 3,
        
        fps = 25,
        resolution_width = 1920,
        resolution_height = 1080,
        resolution_pixel_aspect = 1.0,
        
        default_take_name = "MAIN",
        
        users_data = [{"name": "Administrator", "initials": "adm"}],
        
        # just use one repository for now
        repository_env_key = "REPO",
        
        repository = {
            "name": "Default",
            "windows_path": "~/Projects",
            "linux_path": "~/Projects",
            "osx_path": "~/Projects"
        },
        
        environments = [
            {
                "name":"Maya",
                "extensions":["ma", "mb"]
            },
            {
                "name":"Houdini",
                "extensions":["hip"]
            },
            {
                "name":"Nuke",
                "extensions": ["nk"],
            },
            {
                "name":"Photoshop",
                "extensions": ["psd", "pdd"],
                "export_extensions": ["tif", "tga", "bmp", "jpg", "iff"],
            },
            {
                "name":"3DEqualizer",
                "extensions": ["3te"]
            }
        ],
        
        project_structure = """
        {% for sequence in project.sequences %}
            {% set seq_path = 'Sequences/' + sequence.code %}
            {{seq_path}}/Edit/Offline
            {{seq_path}}/Edit/Sound
            {{seq_path}}/References/Artworks
            {{seq_path}}/References/Text/Scenario
            {{seq_path}}/References/Photos_Images
            {{seq_path}}/References/Videos
            {{seq_path}}/References/Others
            {{seq_path}}/Others
            {{seq_path}}/Others/assets
            {{seq_path}}/Others/clips
            {{seq_path}}/Others/data
            {{seq_path}}/Others/fur
            {{seq_path}}/Others/fur/furAttrMap
            {{seq_path}}/Others/fur/furEqualMap
            {{seq_path}}/Others/fur/furFiles
            {{seq_path}}/Others/fur/furImages
            {{seq_path}}/Others/fur/furShadowMap
            {{seq_path}}/Others/mel
            {{seq_path}}/Others/particles
        {% endfor %}
        """,
        
        version_types = [
            {
                "name": "Animation",
                "code": "ANIM",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name": "Camera",
                "code": "CAMERA",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name": "Composition",
                "code": "COMP",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Nuke"],
                "type_for": "Shot"
            },
            {
                "name": "Edit",
                "code": "EDIT",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Nuke"],
                "type_for": "Shot"
            },
            {
                "name":"FX",
                "code": "FX",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": """{{version.path}}/anim
                        {{version.path}}/cache
                        {{version.path}}/exports
                        {{version.path}}/fx_scenes
                        {{version.path}}/maps
                        {{version.path}}/misc
                        {{version.path}}/obj
                        {{version.path}}/sim_in
                        {{version.path}}/sim_out""",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name":"Model",
                "code": "MODEL",
                "path": "{{project.code}}/Assets/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Asset"
            },
            {
                "name": "Other",
                "code": "OTHER",
                "path": "{{project.code}}/Others/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini", "Nuke"],
                "type_for": "Asset"
            },
            {
                "name": "Previs",
                "code": "PREVIS",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name": "Lighting",
                "code": "LIGHTING",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name": "Rig",
                "code": "RIG",
                "path": "{{project.code}}/Assets/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Asset"
            },
            {
                "name": "Scene Assembly",
                "code": "SCNASS",
                "path":"{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Shot"
            },
            {
                "name": "Matte Paint",
                "code": "MATTE",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/PAINTINGS/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Photoshop"],
                "type_for": "Shot"
            },
            {
                "name": "Texture Paint",
                "code": "TEXTURE",
                "path": "{{project.code}}/Assets/{{version.base_name}}/PAINTINGS/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Photoshop"],
                "type_for": "Asset",
            },
            {
                "name": "Illustration",
                "code": "ILLUSTRATION",
                "path": "{{project.code}}/Assets/{{version.base_name}}/PAINTINGS/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Photoshop"],
                "type_for": "Asset"
            },
            {
                "name": "Shading",
                "code": "SHADING",
                "path": "{{project.code}}/Assets/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["Maya", "Houdini"],
                "type_for": "Asset"
            },
            {
                "name": "Tracking",
                "code": "TRACK",
                "path": "{{project.code}}/Sequences/{{sequence.code}}/Shots/{{version.base_name}}/{{type.code}}",
                "filename": "{{version.base_name}}_{{version.take_name}}_{{type.code}}_v{{'%03d'|format(version.version_number)}}_{{version.created_by.initials}}{{version.extension}}",
                "output_path": "{{version.path}}/OUTPUT/{{version.take_name}}",
                "extra_folders": "",
                "environments": ["3DEqualizer"],
                "type_for": "Shot"
            }
        ]
    )
    
    def __init__(self):
        
        self.config_values = Config.default_config_values.copy()
        self.user_config = {}
        
        # the priority order is
        # oyProjectManager.config
        # config.py under .oyrc directory
        # config.py under $OYPROJECTMANAGER_PATH
        
        self._parse_settings()
    
    def _parse_settings(self):
        # for now just use $OYPROJECTMANAGER_PATH
        ENV_KEY = "OYPROJECTMANAGER_PATH"
        
        # try to get the environment variable
        if not os.environ.has_key(ENV_KEY):
            # don't do anything
            logger.debug("no environment key found for user settings")
        else:
            logger.debug("environment key found")
            
            resolved_path = os.path.expanduser(
                os.path.join(
                    os.environ[ENV_KEY],
                    "config.py"
                )
            )
            
            # using `while` is not safe to expand variables
            # do the expansion for 5 times which is complex enough
            # and I don't (hopefully) expect anybody to use
            # more than 5 level deep environment variables
            resolved_path = os.path.expandvars(
                os.path.expandvars(
                    os.path.expandvars(
                        os.path.expandvars(
                            resolved_path
                        )
                    )
                )
            )
            
            try:
                try:
                    logger.debug("importing user config")
                    execfile(resolved_path, self.user_config)
                except SyntaxError, err:
                    raise RuntimeError("There is a syntax error in your "
                                       "configuration file: " + str(err))
                
                # append the data to the current settings
                logger.debug("updating system config")
                for key in self.user_config:
                    if key in self.config_values:
                        self.config_values[key] = self.user_config[key]
            
            except IOError:
                logger.warning("The $OYPROJETMANAGER_PATH:" + resolved_path + \
                               " doesn't exists! skipping user config")
            
#            # ---------------------------------------------------
#            # create the users
#            from oyProjectManager.core.models import User
#            
#            self.users = []
#            for user_data in self.users_data:
#                name = user_data.get("name")
#                initials = user_data.get("initials")
#                email = user_data.get("email")
#                
#                self.users.append(
#                    User(name, initials, email)
#                )
    
    def __getattr__(self, name):
        return self.config_values[name]
    
    def __getitem__(self, name):
        return getattr(self, name)
    
    def __setitem__(self, name, value):
        return setattr(self, name, value)
    
    def __delitem__(self, name):
        delattr(self, name)
    
    def __contains__(self, name):
        return name in self.config_values
    
    @property
    def last_user_initial(self):
        """returns the last user initial
        
        It is not very much related with the config.py and user settings, but
        it seems the most appropriate place is this one to get information from
        individual users.
        
        This should work fairly fast, because it uses the local filesystem not
        the network thus the fileserver.
        """
        # TODO: This should be replaced with beaker.session
        
        file_name = '.last_user'
        file_path = "~/.oypmrc/"
        file_fullpath = os.path.join(
            file_path, file_name
        )
        
        last_user_initials = None
        
        try:
            last_user_file = open(file_fullpath)
        except IOError:
            pass
        else:
            last_user_initials = last_user_file.readline().strip()
            last_user_file.close()
        
        return last_user_initials
        
    @last_user_initial.setter
    def last_user_initial(self, user_initials):
        """sets the user initials for the last user
        """
        
        file_name = '.last_user'
        file_path = "~/.oypmrc/"
        file_fullpath = os.path.join(
            file_path, file_name
        )
        
        try:
            last_user_file = open(file_fullpath, 'w')
        except IOError:
            pass
        else:
            last_user_file.write(user_initials)
            last_user_file.close()
