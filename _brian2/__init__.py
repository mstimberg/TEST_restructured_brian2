from _brian2.units import *
from _brian2.utils import *
from _brian2.core.preferences import *

# preferences
import _brian2.core.core_preferences as _core_preferences

prefs.load_preferences()
prefs.do_validation()

prefs._backup()

__version__ = 'dummy'