'''
    AUTHOR: Jacob L. Miller
    DATE: Thursday, October 12, 2023
    PROJECT: Census Variables (Data Cleaning)
'''


# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.dtypes)

'''
    Dictionary used to set the datatypes of each of the columns in the dataframe.
    Each key in the dictionary has an array value, with the first element in the 
    array specifying the datatype and the second element specifying the
    categorical order of the column's input values if necessary.
    Note: columns that don't need to be reset as a different type are 
          not listed in the dictionary.
'''
datatype_dict = {
                    'first_name': ['string'],
                    'last_name': ['string'],
                    'birth_year': ['int32'],
                    'num_children': ['int32'],
                    'higher_tax': ['categorical', ['Strongly Disagree',
                                                   'Disagree',
                                                   'Neutral',
                                                   'Agree',
                                                   'Strongly Agree']],
                    'marital_status': ['one-hot']
                }

'''
    Function used to convert an input into 
    Pascal case
'''
def capitalize(input):
    pascal = ''
    for i in range(len(input.split())):
        pascal += (input.split()[i][0].upper() + input.split()[i][1:].lower() + ' ')    # iterates through each word in the input
                                                                                        # and adds the first letter capitalized and 
                                                                                        # the rest of the word lowercase to the
                                                                                        # 'pascal' variable.                                                                                    
    return pascal.strip()

census.higher_tax = census.higher_tax.apply(lambda x: capitalize(x))    # convert each input in the 'higher_tax'
                                                                        # column of the dataframe to Pascal case.
census.birth_year.replace('missing', '1967', inplace=True) # replace the missing info in the 'birth_year' 
                                                           # column with the correct info

'''
  Convert each column in the census dataframe to be the 
  correct datatype using the datatype_dict dictionary.
'''
for col in datatype_dict: 
    if (len(datatype_dict[col]) == 1):
        if (datatype_dict[col][0] == 'one-hot'):
            census = pd.get_dummies(data=census, columns=[col])
        else:
            census[col] = census[col].astype(datatype_dict[col][0])
    else:
        census[col] = pd.Categorical(census[col], datatype_dict[col][1], ordered=True)

print(census.dtypes)
#print(census.higher_tax.unique())
print(census.birth_year.mean())
print(census.higher_tax.cat.codes.median())