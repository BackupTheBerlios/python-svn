import _spe.info as info
INFO = info.copy()

from distutils.core import setup

setup(name          = INFO['title'],
      version       = INFO['version'],
      description   = INFO['description'],
      author        = INFO['author'],
      author_email  = INFO['author_email'],
      url           = INFO['url'],
      packages      = ['_spe'],
      license       = INFO['license'],
     )

