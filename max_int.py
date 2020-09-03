# Algorithm: While user input is > or = to 0 we should propmt the user with an input asking for a intenger.
# If the user inserts a negative number, the program should stop and print out the highest number he typed in
# durring the perriod the program was running.

current_max_int = 0

num_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))

    if num_int > current_max_int:
        current_max_int = num_int

print("The maximum is", current_max_int)