import math
import random

angle = random.randint(0, 360)

radians = math.radians(angle)

print("Angle (degrees):", angle)
print("Sin value:", math.sin(radians))
print("Cos value:", math.cos(radians))
print("Tan value:", math.tan(radians))