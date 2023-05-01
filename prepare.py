
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
from sklearn.model_selection import train_test_split

def prep_telco(telco_df): #make this generic
    telco_df = telco_df.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])

    telco_df['gender_encoded'] = telco_df.gender.map({'Female': 1, 'Male': 0})
    telco_df['partner_encoded'] = telco_df.partner.map({'Yes': 1, 'No': 0})
    telco_df['dependents_encoded'] = telco_df.dependents.map({'Yes': 1, 'No': 0})
    telco_df['phone_service_encoded'] = telco_df.phone_service.map({'Yes': 1, 'No': 0})
    telco_df['paperless_billing_encoded'] = telco_df.paperless_billing.map({'Yes': 1, 'No': 0})
    telco_df['churn_encoded'] = telco_df.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(telco_df[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'payment_type']],
                                  drop_first=True)
    
    telco_df = pd.concat( [telco_df, dummy_df], axis=1 )
    
    telco_df.total_charges = telco_df.total_charges.str.replace(' ', '0').astype(float)

    return telco_df

#removes all columns with more than 5% nulls, NaNs, Na, Nones
def null_remove(df_name):
    for col in df_name.columns:
        if df_name[col].isna().value_counts("False")[0] < 0.95: #tests if a row cotains more than 5% nulls, NaNs, ect. 
            df_name.drop(columns=[col], inplace=True)
            print(f"Column {col} has been dropped because it contains more than 5% nulls")   
#call should be: prep.null_remove(df_name)           

#brings back all the columns that may be duplicates
def col_dup(df_name):
    for col1 in df_name.columns:
        for col in df_name.columns:
            temp_crosstab=pd.crosstab(df_name[col] , df_name[col1])
            if temp_crosstab.iloc[0,0] != 0 and temp_crosstab.iloc[0,1] == 0 and temp_crosstab.iloc[1,0] == 0 and temp_crosstab.iloc[1,1] !=0:
                if col1 != col:
                    print(f"\n{col1} and {col} may be the duplicates\n")
                    
                    print(temp_crosstab.iloc[0:3,0:3])
                    print("--------------------------------------------")
       
#call should look like: prep.col_dup(df_name)


#this is a function to split your data into train, validate, and test sets

def split_function(df_name, target_varible_column_name):
    train, test = train_test_split(df_name,
                                   random_state=123, #can be whatever you want
                                   test_size=.20,
                                   stratify= df_name[target_varible_column_name])
    
    train, validate = train_test_split(train,
                                   random_state=123,
                                   test_size=.25,
                                   stratify= train[target_varible_column_name])
    return train, validate, test

#call should look like: 
#train_df_name, validate_df_name, test_df_name = prep.split_function(df_name, 'target_varible_column_name')

#This makes two lists containing all the categorical and continuous variables
def cat_and_num_lists(df_train_name):
    col_cat = [] #this is for my categorical varibles
    col_num = [] #this is for my numeric varibles

    for col in df_train_name.columns[1:21]:
        print(col)
        if df_train_name[col].dtype == 'O':
            col_cat.append(col)
        else:
            if len(df_train_name[col].unique()) < 4: #making anything with less than 4 unique values a catergorical value
                col_cat.append(col)
            else:
                col_num.append(col)
    return col_cat , col_num           
#the call for this should be: prep.cat_and_num_lists(df_train_name)


#This function is for running through catagorical on catagorical features graphing and running the chi2 test on them (by Alexia)
def cat_on_cat_graph_loop(dataframe_train_name, col_cat, target_ver, target_ver_column_name):
    for col in col_cat:
        print()
        print(col.upper())
        print(dataframe_train_name[col].value_counts())
        print(dataframe_train_name[col].value_counts(normalize=True))
        dataframe_train_name[col].value_counts().plot.bar()
        plt.show()
        print()
        print()
        print(f'HYPOTHESIZE')
        print(f"H_0: {col.lower().replace('_',' ')} does not affect {target_ver}")
        print(f"H_a: {col.lower().replace('_',' ')} affects {target_ver}]")
        print()
        print(f'VISUALIZE')
        sns.barplot(x=dataframe_train_name[col], y=dataframe_train_name[target_ver_column_name])
        plt.title(f"{col.lower().replace('_',' ')} vs {target_ver}")
        plt.show()
        print()
        print('ANALYZE and SUMMARIZE')
        observed = pd.crosstab(dataframe_train_name[col], dataframe_train_name[target_ver_column_name])
        chi2Test(observed)
        print()
        print()
#the call should be: prep.cat_on_cat_graph_loop(dataframe_train_name, col_cat, "target_ver", "target_ver_column_name")        

#this funciton works in this module to run the chi2 test with the above function
def chi2Test(observed):
    alpha = 0.05
    chi2, pval, degf, expected = stats.chi2_contingency(observed)
    print('Observed')
    print(observed.values)
    print('\nExpected')
    print(expected.astype(int))
    print('\n----')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p-value = {pval:.4f}')
    print('----')
    if pval < alpha:
        print ('We reject the null hypothesis.')
    else:
        print ("We fail to reject the null hypothesis.")
# prep.chi2Test(observed) is the call 