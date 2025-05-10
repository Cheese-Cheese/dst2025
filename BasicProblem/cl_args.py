import sys

print(sys.argv)
print(sys.argv[0])

numbers = [int(number) for number in sys.argv[1:]]

print(numbers)
print(numbers[1])
print(type(numbers[1]))