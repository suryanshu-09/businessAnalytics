import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_csv("titanic.csv")

df = sns.load_dataset('titanic')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(df.head(10))
#print(df.tail(10))

#print(df.info())

#print(df.shape)

#print(df.columns)

unique_counts = df.nunique()
#print(unique_counts)

#survived_unique_values = df['survived'].unique()
#print(survived_unique_values)

sex_unique_values = df['sex'].unique()
#print(sex_unique_values)

gender_value_counts = df['sex'].value_counts()
#print(gender_value_counts)


survided_value_counts = df['survived'].value_counts()
#print(survided_value_counts)

grouped_data = df.groupby(['sex', 'survived'])['survived'].count()
#print(grouped_data)

class_survived_counts = df.groupby(['pclass', 'survived'])['survived'].count()
#print(class_survived_counts)

embarked_class_survived_counts = df.groupby(['embark_town', 'pclass', 'survived'])['survived'].count()
#print(embarked_class_survived_counts)

# sns.countplot(x="sex", hue="survived", data = df)
# plt.xlabel("Gender")
# plt.ylabel("Number of passengers")
# plt.title("Survival by Gender")
# plt.show()

# sns.countplot(x="pclass", hue="survived", data = df)
# plt.xlabel("Passenger Class")
# plt.ylabel("Number of passengers")
# plt.title("Survival by Passenger Class")
# plt.show()

# sns.catplot(x = "embark_town", hue = "survived", col = "pclass", data = df, kind = "count", palette = "Set2")
# plt.xlabel("Embarkation town")
# plt.ylabel("Number of passengers")
# plt.suptitle("Survival by Embarkation town and Passenger class")
# plt.show()

#print(df.describe())

#print(df['embark_town'].describe())

#print(df['survived'].value_counts())
#print(df['alive'].value_counts())

df.drop(columns = ['alive'], inplace = True)
#print(df.columns)

#print(df['embarked'].value_counts())
#print(df['embarked_town'].value_counts())

df.drop(columns = ['embarked'], inplace = True)
#print(df.columns)

#print(df['class'].value_counts())
#print(df['pclass'].value_counts())

df.drop(columns = ['class'], inplace = True)
#print(df.columns)

#print(df['adult_male'].value_counts())

#df['adult_male'].replace({True:1, False:0}, inplace = True)

#print(df.isnull().sum())
#df.dropna(subset=['Age'], inplace = True)

# sns.boxplot(y="age", data = df)
# plt.title("Box plot for age column")
# plt.show()

#df['age'] = df['age'].fillna(df['age'].median())

#df['deck'] = df['deck'].fillna(df['deck'].mode()[0])

#df.dropna(subset = ['embark_town'], inplace = True)

#df.rename(columns = {'deck':'cabin'}, inplace = True)

# plt.hist(df['who'], color='skyblue', edgecolor='black')
# plt.xlabel("Passenger type")
# plt.ylabel("Frequence")
# plt.title("Distribution of Passenger types")
# plt.show()

numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='PuBuGn', fmt=".2f")
plt.title('Correlation Matrix of Titanic Dataset')
plt.show()
