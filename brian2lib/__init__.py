from brian2lib.units import *
from brian2lib.utils import *
from brian2lib.core.preferences import *

# preferences
import brian2lib.core.core_preferences as _core_preferences

prefs.load_preferences()
prefs.do_validation()

prefs._backup()

__version__ = 'dummy'