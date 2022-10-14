#Selection Commands

#Subroutine to output key stage
def YearGroup(Year):
  if Year >= 7 and Year <11:
    print("Key Stage 3")
  elif Year >=10 and Year <13:
    print("Key Stage 4")
  elif Year >= 1 and Year <3:
    print("Key Stage 1")
  elif Year >=3 and Year <7:
    print("Key Stage 2")
  elif Year >=12 and Year <15:
    print("Sixth Form")
  elif Year == 0:
    print("Reception")
  elif Year < 0:
    print("Error")
  else:
    print("Post-School")
    

#Main program
YearGroup(7)
YearGroup(11)
YearGroup(6)
YearGroup(13)
YearGroup(-1)
YearGroup(0)
YearGroup(2)
YearGroup(23)
