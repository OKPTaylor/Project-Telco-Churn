import scipy.stats as stats
import pandas as pd
import os

import env




#This function returns a url for a mysql database based on the data base name and env credituals
def get_db_url(data_base):
    return (f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{data_base}')

#This function returns a dataframe based on the provided info
def new_sql_data_query(sql_query , url_for_query):
    return pd.read_sql(sql_query , url_for_query)
#Use this call with the above functions to pull back the data and save it: 
# dataframe_name = new_sql_data_query("desired_sql_query" , get_db_url("database_name"))

#This function will either load a csv file if it exist or run a sql query and save it to a csv
def get_sql_data(sql_query, directory, url_for_query, filename):
    
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        print("csv found and loaded")
        return df
    else:
        df = new_sql_data_query(sql_query , url_for_query)

        df.to_csv(filename)
        return df
"""
You must have the following provided for the function to work:

sql_query = "desired query"
directory = os.getcwd()
url_for_query = get_db_url("database_name")
filename = "datbase_name.csv"

"""
#then use this call: dataframe_name = get_sql_data(sql_query, directory, url_for_query, filename)

