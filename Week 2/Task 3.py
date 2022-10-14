#using variables and constants

#subroutine to calculate flow rate of the heart
def FlowRate(Volume, Time):
  return Volume / Time

#main program

#  Task: volume / time * 60 = IV
Volume = 100
Time = 30
Heart = (FlowRate(Volume, Time) * 60)
print("The flow rate of the IV heart is", Heart, "ml/hr")

