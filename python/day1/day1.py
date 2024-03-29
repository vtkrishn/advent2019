# 1st solution - 3323874
# ---------------
import math
s = 0
l = [] # input from the site
for i in l:
    s += math.ceil(i / 3) - 2
print(s)

# 2nd solution - 4982961
# ---------------
def recurse(i, s):
    if i < 0:
        return s
    return recurse(math.floor(i / 3) - 2, s + i)

import math
s = 0
 = [] # input from the site
for i in l:
    s += recurse(math.floor(i / 3) - 2, 0)
print(s)
