print("Enter principal amount, rate and time:")
x, y, z = input().split()
pAmt = float(x)
rate = float(y)
time = float(z)
simple_interest = (pAmt * rate * time)/100
print(simple_interest)
