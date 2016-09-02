# Body surface
import math

weight = int(input())
height = int(input())

body_surface = 3.207 * math.pow(10, -4) * math.pow(height, 0.3) * math.pow( 1000 * weight, 0.7285 - 0.0188 * ( 3 + math.log(weight, 10)))

print(body_surface)
