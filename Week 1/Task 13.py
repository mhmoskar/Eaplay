radius = 1
## radius1 = 0.05
HBP = 0.2
PD = 0.75
VBP = 3.14 * (radius * radius) * HBP
SB =  (4/3) * 3.14 * (radius * radius * radius)
print(VBP, HBP)
BallPit = (VBP / SB) * PD
print(SB)
print(BallPit)


diameter = 2

# rad = int(diameter) / 2
#print("Radius of the Ballpit: ", rad)
#PD = 0.75
#vol = (3.14 * rad * rad * 0.2)
#ball = (3.14 * (4/3) * rad * rad * rad)
#print(vol, ball)
#full = int(ball) / int(vol)
#print(full)

