import os
import shutil
import sys
from distutils.version import StrictVersion
from logger import log

pgoapi_version = "1.1.7"

oldpgoapiPath = os.path.join(os.path.dirname(__file__), "pogom/pgoapi")
if os.path.isdir(oldpgoapiPath):
    log.info("I found %s, but its no longer used. Going to remove it...", oldpgoapiPath)
    shutil.rmtree(oldpgoapiPath)
    log.info("Done!")

# Assert pgoapi is installed
try:
    import pgoapi
    from pgoapi import utilities as util
except ImportError:
    log.critical("It seems `pgoapi` is not installed. You must run pip install -r requirements.txt again")
    sys.exit(1)

# Assert pgoapi >= pgoapi_version
if not hasattr(pgoapi, "__version__") or StrictVersion(pgoapi.__version__) < StrictVersion(pgoapi_version):
    log.critical("It seems `pgoapi` is not up-to-date. You must run pip install -r requirements.txt again")
    sys.exit(1)
