# Read integers from the file
with open("indata.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# Calculate the sum
sum_numbers = sum(numbers)

# Print the sum with comma separators and two decimal places
formatted_sum = "{:,.2f}".format(sum_numbers)
print(formatted_sum)
