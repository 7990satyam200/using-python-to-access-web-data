import re

sum = 0

file = open('regex_sum_207216.rtf', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    print(numbers)
    for number in numbers:
            sum += int(number)

print(sum)
