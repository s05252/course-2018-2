import numpy as np

RATE = .0375
TERM = 30
simple = (      RATE  * np.ones(TERM)).cumsum()
compound = ((1 + RATE) * np.ones(TERM)).cumprod() - 1

simple
compound

simple[-1]
compound[-1]

simple[-1] - compound[-1]