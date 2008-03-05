#/usr/bin/python
from distutils.core import setup

setup(name          = "spe",
      description   = """Python IDE with UML, PyChecker Source Code Doctor, WinPdb Debugger, wxGlade and XRCed GUI designers and Blender support.""",
      author        = "www.stani.be",
      author_email  = "spe.stani.be@gmail.com",
      url           = "http://pythonide.stani.be",
      license       = "GPL",
      scripts       = ['_spe/spe'],
      packages      = ['_spe', '_spe.dialogs', '_spe.examples', '_spe.plugins', '_spe.shortcuts', '_spe.sidebar',
                       '_spe.skins', '_spe.sm', '_spe.tabs', '_spe.view', '_spe.skins.default', '_spe.sm.wxp'],
      package_data  = {'': ['_spe/defaults.cfg', '_spe/doc/donate.html', '_spe/doc/about.htm', 
                       '_spe/skins/default/*', '_spe/images/*']}
)

