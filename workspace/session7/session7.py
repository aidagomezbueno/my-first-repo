#%%
import utilities

# %%
import sys
print(sys.path)

# %%

import utilities

print(utilities.add(5, 3))

# %%

from utilities import add
print(add(5, 3))

# %%
from utilities import *
print(add(5, 3))