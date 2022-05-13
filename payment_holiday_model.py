# this model decides applications that should be granted a payment holiday in a data set



import numpy as np
import pandas as pd

df = pd.read_excel(r"C:\Users\Student\Downloads\Task 3 Data.xlsx")

# Case 1
# Get rows with credit score in the 25th percentile
# Among those, get rows with default status = 1
# Among those , get rows with Gross salary that is in the 25th percentile
def case_1(data_frame):
    df = data_frame
    indexNames = df.index[df['Credit_Score'] > -1].tolist()
    credit_stat = df.iloc[indexNames, 10].describe().tolist()
    cred_pcnt25 = credit_stat[4]  # 25th percentile of credit score

    indexNames = df.index[df['Gross_Salary'] > -1].tolist()
    gro_slry_stat = df.iloc[indexNames, 4].describe().tolist()
    gros_pcnt25 = gro_slry_stat[4]  # 25th percentile of gross salary
    # All credit scores, gross salary in the 25th percentile and defaulted clients
    indexNames = df.index[(df['Credit_Score'] < cred_pcnt25) & ((df['Default'] == 1 )&( df['Gross_Salary'] < gros_pcnt25))].tolist()
    return indexNames

# Case 2
# Get rows with salary ratio less than the average
# Among those , get those with default status = 1
def case_2(data_frame):
    df = data_frame
    salRat_stat = df.iloc[df.index[df['Salary_Ratio'] > -1].tolist(), -1].describe().tolist()
    indexNames = df.index[ (df['Salary_Ratio'] < salRat_stat[1]) & (df['Default'] == 1)].tolist()
    return indexNames


# Case 3
# Get rows with MFC
# Among those get default status = 1
# Among those get rows with salary ratio in the 25th percentile
def case_3(data_frame):
    df = data_frame
    products = ['Product_1', 'Product_2', 'Product_3']
    mfcList = []
    for product in products:
        mfcList = df.index[df[product] == "MFC"].tolist()

    for num in mfcList:
        if (num in mfcList):
            mfcList.remove(num)

    salRat = df.iloc[mfcList, -1].describe().tolist()
    salRat25 = salRat[4]  # 25th percentile of gross salary
    indexNames = df.index[(df['Salary_Ratio'] < salRat25) & (df['Default'] == 1)].tolist()
    return indexNames

# Loop case
# Get rows with credit score in the 25th percentile
# Among those get rows with salary ratio in the 25th percentile
def loop_case(data_frame):
    df = data_frame
    indexNames = df.index[df['Credit_Score'] > -1].tolist()
    credit_stat = df.iloc[indexNames, 10].describe().tolist()
    cred_pcnt25 = credit_stat[4]  # 25th percentile of credit score
    salRat_stat = df.iloc[df.index[df['Salary_Ratio'] > -1].tolist(), -1].describe().tolist()
    indexNames = df.index[(df['Salary_Ratio'] < salRat_stat[1]) & (df['Credit_Score'] < cred_pcnt25)].tolist()
    return indexNames


def cost(data_frame):
    df = data_frame
    x = ((len(df.index))/10127)*100
    y = 100 - x
    z = 10127

    credit_risk_denial = y*0.2*z*2500
    credit_risk_approved = x*z*(500+(0.07*2500))
    tot_cost = credit_risk_denial + credit_risk_approved
    boundary = tot_cost * 0.15
    print("Approved Applications: ",len(df.index))
    print("Total Cost: ",tot_cost)

    done = False
    if (credit_risk_approved > credit_risk_denial):
        if ((credit_risk_approved - credit_risk_denial) > boundary):
            done = True
        else:
            done = False

    else:
        done = False

    return done  # If true is returned it means decline more applications


count = 3
while(cost(df)):
    if count == 1:
        df.drop(case_3(df), inplace=True)
        count = count + 1

    elif count == 2:
        df.drop(case_2(df), inplace=True)
        count = count + 1


    elif count == 3:
        df.drop(case_3(df), inplace=True)
        count = count + 1

    else:
        loop_case(df)

    df = df.reset_index();

