print("Enter the count of roses and delivery distance")
x, y = input().split()
count = int(x)
dist = int(y)
if dist in range(0, 5):
    print(count*10 + 25)
elif dist in range(5, 10):
    print(count*10 + 50)
elif dist > 10:
    print(count*10 + 75)
