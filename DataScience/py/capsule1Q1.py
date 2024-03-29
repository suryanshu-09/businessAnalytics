name = input()
print("Hello " + name)
print("Enter two values:")
x,y = input().split()
print("original x: " + x)
print("original y: " + y)
z = x
x = y
y = z
print("swapped x: " + x)
print("swapped y: " + y)
