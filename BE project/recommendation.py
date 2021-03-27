import pandas as pd


#load the csv file in python
filename = 'C:/Users/kenne/Desktop/dcc_final.xlsx'
data = pd.read_excel (filename)
print("############################List of all the day care centres######################################")
print (data)





#get the last column of the excel file in a list
regions = []
regions = data['Region']
#print (regions)

print("#################################PRINTING THE DAY CARE CENTRES IN ANDHERI##############################")
print(data.loc[data['Region'] == "Bandra"])
    
        
