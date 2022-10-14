def function(mark):
  if mark < 2:
    print("Grade: U")
  elif mark >= 2 and mark < 4:
    print("Grade: 1")
  elif mark >= 4 and mark < 13:
    print("Grade: 2")
  elif mark >= 13 and mark < 22:
    print("Grade: 3")
  elif mark >= 22 and mark < 31:
    print("Grade: 4")
  elif mark >= 31 and mark < 41:
    print("Grade: 5")
  elif mark >= 41 and mark < 54:
    print("Grade: 6")
  elif mark >= 54 and mark < 67:
    print("Grade: 7")
  elif mark >= 67 and mark < 80:
    print("Grade: 8")
  elif mark >= 80:
    print("Grade: 9")

mark = 80
print(function(mark))
