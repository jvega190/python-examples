'''
    Program: Magical Calculator
    Author: Tote
    Copyright: 2022
'''


import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

# TODO: this is a TODO comment
def perform_math():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # if user quits -> stop
    if equation == 'quit':
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
