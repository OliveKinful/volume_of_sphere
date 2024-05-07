import math

def calculate_volume_sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

print(calculate_volume_sphere(5))
