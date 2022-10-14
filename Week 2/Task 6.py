Job = str.lower(input("input profession:"))


def Quote(Job):
    if Job == "engineer":
        print("The engineer has been, and is, a maker of history.")
    elif Job == "developer":
        print(
            "Logical thinking, passion and perseverance is the paint on your palette."
        )
    elif Job == "analyst":
        print("Seeing what other people can't see gives you great vision.")
    else:
        print("I'm sorry. We could not find a quote for your job.")


print(Quote(Job))
