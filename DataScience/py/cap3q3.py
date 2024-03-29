import pandas as pd
input_data = {
        'Name':['Ram', 'Kaif', 'Aryan', 'Rohit', 'Shikha', 'Shyam', 'Sundar', 'Kareem', 'Noah', 'John'],
        'Marks':[85, 65, 78, 87, 54, 67, 74, 87, 90, 79]
        }
df = pd.DataFrame(input_data)
print(df)
