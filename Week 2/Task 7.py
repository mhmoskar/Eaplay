def function(Dose):
  if int(Dose) > 10:
    return(3)
  else:
    if int(Dose) > 2.5:
      return(2)
    else:
      if int(Dose) > 1:
        return(1)
      else:
        return(0.5)

#main program
Dose = input("Dose:")

print("For", Dose, "nitrate dose", function(Dose), "ml")
