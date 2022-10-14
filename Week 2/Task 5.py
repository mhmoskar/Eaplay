#subroutine
def condition(Water):
  if Water >= 100:
    print("gaseous")
  elif Water > 0 and Water < 100:
    print("liquid")
  elif Water < 1:
    print("solid")


print(condition(37.2))
