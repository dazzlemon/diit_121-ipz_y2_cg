import numpy as np

xs0 = np.array([0, 1, 2])
xs1 = np.array([3, 4, 5])
xs2 = np.array([6, 7, 8])

ys0 = np.array([9, 10, 11])
ys1 = np.array([12, 13, 14])
ys2 = np.array([15, 16, 17])

"""
minX = 0
minY = 9
maxX = 8
maxY = 17
"""

ps0 = np.array((xs0, ys0))
ps1 = np.array((xs1, ys1))
ps2 = np.array((xs2, ys2))

fs = np.array([ps0, ps1, ps2])
print(fs)
print()

fs_flat = np.transpose(fs, (1, 0, 2)).reshape((2, -1))
print(fs_flat)
print()

minX = np.min(fs_flat[0])
maxX = np.max(fs_flat[0])
minY = np.min(fs_flat[1])
maxY = np.max(fs_flat[1])
print(minX, maxX, minY, maxY)
