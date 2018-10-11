# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
import numpy as np
import os
import re
import glob
import csv
import shutil
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory folder of the csv files you want to process
Input_path_A = 'D:/TEST/dataA.csv'
# Can change to xlsx if needed, other changes will be nessesary to code

# Directory folder of the csv files you want to process
Input_path_B = 'D:/TEST/dataB.csv'
# Can change to xlsx if needed, other changes will be nessesary to code

Extension = 'csv'
# Csv files seperator for input and output files..generally (,) or (|)
Delimiter = ','

# Output file path of Result
Output_path_Report = 'D:/TEST/data_Output.csv'

Lst_Columns = ['B','C']

print('Directories loaded...')
#endregion

df_A = pd.read_csv(Input_path_A, sep=Delimiter, dtype=object)
print('Created Dataframe A...')
df_B = pd.read_csv(Input_path_B, sep=Delimiter, dtype=object)
print('Created Dataframe B...')


# Create Lists to Check for duplicates
Lst_Row_Key = []
print(df_A)
for index, row in df_A.iterrows():
    print('x')

'''

#    Str_Row = 'x'
#    for item in Lst_Columns:
#        x = str(row[item])
#        Str_Row.append(x)
#    Lst_Row_Key.append(Str_Row)
#print(Lst_Row_Key)

# Create Array of Rows from List of Rows
Array_Raw_Items_Results = np.array(Lst_Row_Key)

# Decide if there are any exact duplicates    
if len(np.unique(Array_Raw_Items_Results)) != len(Array_Raw_Items_Results):
    Duplicates_In_File = True

# Find the rows where the exact duplicates live
if Duplicates_In_File == True:
    # Create a dictionary of duplicate checker keys vs numvber of duplicates
    unique, counts = np.unique(Array_Raw_Items_Results, return_counts=True)
    Dict_Unique_Counts = dict(zip(unique, counts))
    #Create a list of keys for duplicates only
    List_Duplicate_Keys = ([key for key, val in Dict_Unique_Counts.items() if val > 1])
    # Find which Row Strings are exact duplicates and add their Index to a list
    List_Row_Index_Duplicates = []
    for key in List_Duplicate_Keys:
        # Get the row index's of the duplicate Key
        List_Indexes = [i for i, j in enumerate(Lst_Row_Key) if j == key]
        # Remove Fist Duplicate from List because we let the first one load
        List_Indexes.pop(0)
        # Append the row index's to a list
        List_Row_Index_Duplicates.extend(List_Indexes)
    # Count the number of Duplicates that will be deleted for Report
    Int_Dup_Rows = len(List_Row_Index_Duplicates)
    # Print feedback on Rows that are being deleted
    print('Deleting Duplicate Rows from:', filename)
    print(List_Row_Index_Duplicates)
    # Delete the rows that are duplicates from dataframe df_A
    df_A = df_A.drop(df_A.index[List_Row_Index_Duplicates])
'''