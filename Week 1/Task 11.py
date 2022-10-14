# output raw cost of energy use by:
# previous meter reading
# current reading
# calorific value

CurrentReading = input("Current Reading: ")
PreviousReading = input("Previous Reading: ")
CaloricValue = 39.3

UnitsUsed = int(CurrentReading) - int(PreviousReading)

kWh = UnitsUsed * 1.022 * CaloricValue / 3.6

Energy = kWh * 2.84
# no instruction to create output but made to check for any errors. 
#print(Energy)
