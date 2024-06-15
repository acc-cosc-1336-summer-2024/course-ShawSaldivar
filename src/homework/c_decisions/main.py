import decisions

NumbersB = float(input("Please enter a Option number: "))
NumbersO = float(input("Please enter a number for Total: "))

ratio = decisions.get_options_ratio(NumbersB, NumbersO)
rate = decisions.get_faculty_rating(ratio)

print("You rated: ", ratio, "Which is a ", rate)
