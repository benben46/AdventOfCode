#Day 1: Trebuchet?!

sum = 0;
#with open("test1.txt", "r") as f:
with open("input.txt", "r") as f:
    for line in f:
        # list comprehension to get only digits
        num_values_only = [int(i) for i in list(line) if i.isdigit()]
        # take the first and last digits in the list and add to sum
        sum += num_values_only[0]*10 + num_values_only[-1]

print("The sum is:", sum)


