# Importing brian2lib as well before or after should not make a difference
import brian2lib
import brian2lib
from brian2 import *

print(3*nA * 10*Mohm)
print(3*nA + 10*Mohm)
