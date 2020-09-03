# Algorithm: The user types in the length of the sequence, we need to add the last three numbers together and find the sum.
# For example: 1, 2, 3, 6, 11, 20, 37 

n = int(input("Enter the length of the sequence: "))

num_one = 1
num_two = 2
num_three = 3

summa = 0

for i in range(1, n):
    if i == 4:
        break
    print(i, end=" ")

for i in range(1, n-2):
    summa = num_one + num_two + num_three
    num_one = num_two
    num_two = num_three
    num_three = summa

    print(summa, end=" ")