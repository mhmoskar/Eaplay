#subroutuine - output coszt of fitting a carpet using 3 paramenters

# width of room
# length of room
# price per m^2
# + £3 per m^2
# grippers = £1/m = width * 2 + length * 2
# fitting fee = £50



# Test prices

width = 7
length = 6
meters = width * length
carpet = 17
underlay = meters * 3
FittingFee = 50
main = width * length * carpet
grippers = (width * 2) + (length * 2)

cost = grippers + FittingFee + underlay + main

print("£17 carpet = ", underlay, "+",FittingFee, "+", grippers, "+", main, "= £", cost)

