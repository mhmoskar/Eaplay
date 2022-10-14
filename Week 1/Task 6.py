#Temp converter problem

#subroutine to convert C to F
def CtoF(C):
  return (C * 1.8) + 32
#subroutine
def FtoC(F):
  return (F - 32) / 1.8

#main program
C = 30
F = CtoF(C)

print(C,"degrees C is" ,F,"degrees F")
