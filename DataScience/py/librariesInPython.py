#import numpy as np
#1D Numpy array
#my_list = [1, 2, 3, 4, 5]
#my_1D_array = np.array(my_list)
#print(my_1D_array)

#arr1D = np.array([1, 2, 3, 4, 5])
#print(arr1D)

#2D array
#my_2D_array = np.array([[1, 2, 3], [4, 5, 6]])
#print(my_2D_array)

#3D array
#my_3D_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#print(my_3D_array[1, :, 0])

#np.zeros()
#zeros_2D_array = np.zeros((3, 4))
#print(zeros_2D_array)

#np.ones()
#ones_2D_array = np.ones((3, 4))
#print(ones_2D_array)

#arr1 = np.array([1, 2, 3, 4, 5])
#result = arr1 * 10 #multiply each element by 10
#print(result)

#import pandas as pd
#data = [1, 2, 3, 4, 5]
#my_series = pd.Series(data)
#print(my_series)

#my_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
#print(my_series)

#data = {
#        'Name':['Alice', 'Bob', 'Charlie'],
#        'Age':[25, 30, 35],
#        'City':['New york', 'Los Angeles', 'Chicago']
#        }
#df = pd.DataFrame(data, index=['a', 'b', 'c']) #CSV files, excel, db etc.
#print(df)

#import matplotlib.pyplot as plt

#Sample data
#x = [1, 2, 3, 4, 5]
#y = [10, 12, 5, 8, 6]

#Create a line plot
#plt.plot(x, y)

#To add labels to the plot
#plt.xlabel("X-axis Label")
#plt.ylabel("Y-axis Label")

#Bar Plot
#categories = ['A', 'B', 'C', 'D', 'E']
#values = [10, 15, 5, 8, 6]
#plt.bar(categories, values, color = 'green')
#plt.xlabel("Categories")
#plt.ylabel("Values")
#plt.title('Bar Plot')

#Histogram
#data = [10, 12, 5, 8, 6 ,15, 18, 20, 22, 30, 35, 40]
#plt.hist(data, bins = 5, color = 'purple', edgecolor = 'black')
#plt.xlabel("Value")
#plt.xlabel("Frequency")
#plt.title('Histogram')

#Seaborn
#Show output of the plot
plt.show()
