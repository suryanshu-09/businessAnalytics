import matplotlib.pyplot as plt
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]
plt.bar(x, y, color='red')
plt.xlabel("Categories")
plt.ylabel("Frequency")
plt.title('Bar Plot')
plt.show()
