import pandas as pd
input_data = {
        'Employee_Name':['Ram', 'Kaif', 'Aryan', 'Rohit', 'Shikha'],
        'Income':[85000, 65000, 78000, 87000, 54000]
        }
df = pd.DataFrame(input_data, index=['a', 'b', 'c', 'd', 'e'])
print(df)
