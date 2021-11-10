import os
import random

dir = 'C:\\'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir, filename)
print(filename)
print(path)