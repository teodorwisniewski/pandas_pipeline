# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:59:04 2021

@author: tew
"""
import pandas as pd
import glob
import numpy as np
import csv
import itertools
import os




def get_file_info(filename: str):
    """
    allows to extract data from csv file 

    Parameters
    ----------
    filename : str
        DESCRIPTION.

    Returns
    -------
    data_info : TYPE
        DESCRIPTION.
    data_date : TYPE
        DESCRIPTION.

    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for i in range(max([line_data_info, line_date])+1):
            row_value = next(reader)
            row_value = row_value[0] if len(row_value) else ""
            if i == line_data_info:
                data_info = row_value
            elif  i == line_date:
                data_date = row_value
        print(data_info, data_date)
    return data_info, data_date
    

def load_csv_file_and_format_it(filename, data_info, data_date):
    """
    reads a csv file and format it(datatypes, dropping a column)

    Parameters
    ----------
    filename : str
        DESCRIPTION.
    data_info : str
        DESCRIPTION.
    data_date : str
        DESCRIPTION.

    Returns
    -------
    df : pandas Dataframe

    """
    df = pd.read_csv(filename,
                 skiprows=[i for i in range(0,8)],
                 sep= ";", encoding='utf-8',
                dtype={'ID': str})
    df = df.iloc[: , :-1]
    new_colname = data_info + " " + data_date
    df = df.rename(columns={df.columns[2]: new_colname})
    return df

# steps
glob.glob("*.*")

files = ['activity_status_and_employed_persons.csv',
         'activity_status_and_employed_persons_receving_pensions.csv',
         "employed_persons_by_education.csv",
         'population_by_age_averge_age2021.csv']
filename = files[3]
line_data_info = 2
line_date = 4
data_info, data_date = get_file_info(filename)
df = load_csv_file_and_format_it(filename, data_info, data_date)