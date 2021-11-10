import os
import random

dir = 'C:/Users/Silva Tito/Pictures/Adventure Time'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir, filename)
print(filename)
print(path)