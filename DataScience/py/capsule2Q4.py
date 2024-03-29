print("input 10 numbers")
numbers = []
for i in range(10):
    numbers.append(int(input()))
print("\noutput:")
for number in numbers:
    if number%2==0:
        print(number**2)
    else:
        print(number**3)
