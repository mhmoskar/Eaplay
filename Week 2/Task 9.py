days = [
    ['Monday', 'Mon', 'M', 1],
    ['Tuesday', 'Tue', 'Tu', 2],
    ['Wednesday', 'Wed', 'W', 3],
    ['Thursday', 'Thu', 'Th', 4],
    ['Friday', 'Fri', 'F', 5],
    ['Saturday', 'Sat', 'Sa', 6],
    ['Sunday', 'Sun', 'S', 7],
]
Day = int(input("Number for day: "))
Sub = str.lower(input("What Format:\nDay\nShortday\nChar\nEnter:"))


def DayFormat(Day):
    if Day > 7:
        print("Invalid Number of Day")
    else:
        Day = Day - 1
        if Sub == "day":
            print(days[Day][0])
        elif Sub == "shortday":
            print(days[Day][1])
        elif Sub == "char":
            print(days[Day][2])
        else:
            print(
                "There is an error.\nCheck if you have inputed the right parameters."
            )


print(DayFormat(Day))
#def DayFormat(Day):
#  if Day == 1:
#    if Sub == 'full':
#      print(days[0][0])
#    elif Sub ==
