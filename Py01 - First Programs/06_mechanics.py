import math
angle = int(input())*math.pi/180
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
dist = (2 * 18 ** 2 * cos_angle * sin_angle) / 10
print(round(dist))
