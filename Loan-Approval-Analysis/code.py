# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)

categorical_var=bank.select_dtypes(include='object')


print(categorical_var.shape)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)



bank.drop('Loan_ID',inplace=True,axis=1)

banks=pd.DataFrame(bank)
print(banks.shape)
null_val=banks.isnull().sum()
print(null_val)


bank_mode=banks.mode(axis=0,numeric_only=False)
print(bank_mode)


banks.fillna(bank_mode.iloc[0],inplace=True)
print(banks.isnull().sum().values.sum())

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)
se=banks['Self_Employed']=='Yes'
ls=banks['Loan_Status']=='Y'
loan_approved_se=len(banks[(se) & (ls)])
print(loan_approved_se)
nse=banks['Self_Employed']=='No'
loan_approved_nse=len(banks[(nse) & (ls)])
print(loan_approved_nse)

ls_len=len(banks['Loan_Status'])
print(ls_len)

percentage_se=(loan_approved_se/ls_len)*100
print(percentage_se)
percentage_nse=(loan_approved_nse/ls_len)*100
print(percentage_nse)

def mon_to_year(num):
	return num/12
loan_term=banks['Loan_Amount_Term'].apply(lambda x:mon_to_year(x))
print(loan_term)

big_loan_term=0
for i in range(len(loan_term)):
	if(loan_term[i]>=25):
		big_loan_term+=1
print(big_loan_term)
mean_values=banks.groupby(['Loan_Status'])['ApplicantIncome','Credit_History'].agg(np.mean)
print(mean_values.iloc[1])


