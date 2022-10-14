length = input("Length of fish tank in meters?:\n")

height = input("height of fish tank in meters?:\n")

depth = input("depth of fish tank in meters?:\n")

#print(f'You entered {length, height, depth}')

#useing int turns string from cmd input and turns them into an interger that can be calculated.

tank = int(length) * int(height) * int(depth)
output = tank / 1000
print(output, "volume of tank in metersSq")
