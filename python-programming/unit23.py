import numpy as np

dirty = np.array([9, 4, 1, -0.01, -0.02, -0.001])
whos_dirty = dirty < 0
print(whos_dirty)

dirty[whos_dirty] = 0
print(dirty)

linear = np.arange(-1, 1.1, 0.2)
(linear <= 0.5) & (linear >= -0.5)
print(linear)