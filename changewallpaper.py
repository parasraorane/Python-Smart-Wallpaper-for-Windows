import ctypes
import numpy as np
import os
fpath=""#add your wallpaper folder here
z=os.listdir(fpath)
path=z[np.random.randint(len(z))]
ctypes.windll.user32.SystemParametersInfoW(20, 0, fpath+path , 0)