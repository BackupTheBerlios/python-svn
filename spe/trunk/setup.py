#/usr/bin/python
from distutils.core import setup

setup(name          = "spe",
      description   = "If you enjoy SPE, consider a (small) donation.",
      author        = "http://pythonide.stani.be",
      author_email  = "spe.stani.be@gmail.com",
      url           = "http://pythonide.stani.be",
      license       = "GPL",
      scripts       = ['spe'],
      packages      = ['', 'dialogs', 'examples', 'plugins', 'shortcuts', 'sidebar',
                       'skins', 'sm', 'tabs', 'view', 'skins.default', 'sm.wxp'],
      package_data  = {'': ['defaults.cfg', 'doc/donate.html', 'doc/about.htm', 
                       'skins/default/*', 'images/*']}
)

