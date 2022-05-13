import first as first
import pandas as pd
import numpy as np

# from the forage page
#df = pd.read_excel(r"https://cdn.theforage.com/vinternships/companyassets/DRgqWBDL6Y29qQB8T/npn3yYxywjQbkbKXK/1643367889498/Task%202%20Data.xlsx")

# from my pc
df = pd.read_excel(r"C:\Users\Student\Downloads\Task2Data.xlsx")
print(df)


# delete unwanted column
df = df.drop(["Unnamed: 0"], axis=1)
print("Columns we need")  # not necessary, for validation purposes
print(df.columns)

# Delete rows with age less than 18 and credit score above 705
indexNames = df[df['Age'] < 18].index
indexNames2 = df[df['Credit_Score'] > 705].index
df.drop(indexNames, inplace=True)
df.drop(indexNames2, inplace=True)

print("After CreditScore validation and After age validation")  # not necessary, for validation purposes
print(df)
print()


# Product 1 validation . must not contain integers and longer strings
indexNames3 = df[(df['Product_1'].str.isdigit() == True)].index
df.drop(indexNames3, inplace=True)
indexNames3len = df[(df['Product_1'].str.len() > 3)].index
df.drop(indexNames3len, inplace=True)
print("After removing digit values in product_1 and longer strings")
print(df)

# Product 2 validation . must not contain integers
indexNames4 = df[df['Product_2'].str.isdigit() == True].index
df.drop(indexNames4, inplace=True)
indexNames4len = df[(df['Product_2'].str.len() > 3)].index
df.drop(indexNames4len, inplace=True)
print("After removing digit values in product_2")
print(df)

# Product 3 validation . must not contain integers
indexNames5 = df[df['Product_3'].str.isdigit() == True].index
df.drop(indexNames5, inplace=True)
indexNames5len = df[(df['Product_3'].str.len() > 3)].index
df.drop(indexNames5len, inplace=True)
print("After removing digit values in product_3")
print(df)

itList = ['Product_1', 'Product_2', 'Product_3']
for product in itList:
    df.drop(df[(df[product].str.upper() == "IT")].index, inplace=True)

# Removing empty entries
print("The Data Frame before removing rows with empty cells:")
print(df)
del_miss_values = ['Account_Number', 'Age', 'Gender', 'Gross_Salary', 'Industry',
                   'Num_Products', 'Credit_Score', 'Start_Date', 'End_Date', 'Province',
                   'Balance', 'Installment', 'Default', 'Product_1', 'Salary_Ratio']
for i in del_miss_values:
    df.dropna(subset=[i], inplace=True)
print("The Data Frame after removing rows with empty cells:")
print(df)
print("\n")

# Removing duplicates
print("Duplicated Rows")
duplicateRowsDF = df[df.duplicated(['Account_Number'], keep=False)]
print(duplicateRowsDF)
print("Dropping duplicates>>>>>>>")
df.drop_duplicates(subset='Account_Number', keep=False, inplace=True)
print("Duplicates Droped!")
print(df)

print()
print()
print("Cleaned")
print(df.head())

print(df.describe())

#df.to_excel(r'C:\Users\Student\Downloads\StevenNedbankCleanData.xlsx')
