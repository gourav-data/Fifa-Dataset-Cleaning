#!/usr/bin/env python
# coding: utf-8

# # Project Fifa Data cleaning
# 
# # Import Liabraries

# In[1]:


import pandas as pd
import numpy as np


# ## Read Dataset
# 

# In[2]:


pd.set_option('display.max_column',None) # for none of the rows hidden
data = pd.read_csv('D:/Projects/Fifa Datacleaning/fifa21 raw data v2.csv')
data.sample(10)


# In[3]:


data.shape # to check rows and columns


# In[4]:


data.info()  # to check data types in columns


# # Data Cleaning
# ## Copy Dataframe

# In[5]:


fifa = data.copy()


# ### Club Column Checking
# 
# Current Club of player

# In[6]:


fifa['Club'].dtype #String Datatype


# In[7]:


fifa['Club'].unique() # trailing and leading spaces in this column


# In[8]:


fifa['Club'] =fifa['Club'].str.strip()
fifa['Club'].unique()


# ### Contract Column

# In[9]:


fifa['Contract'].dtype


# In[10]:


fifa['Contract'].unique()


# In[11]:


for index,row in fifa.iterrows():
    if 'On Loan' in row['Contract'] or 'Free' in row['Contract']:
        print(row['Contract'])


# In[12]:


def extract_Contract_info(contract):
    if contract == 'Free' or 'On Loan' in contract:
        start_date = np.nan
        end_date = np.nan
        contract_length = 0
    else:
        start_date,end_date = contract.split(' ~ ')
        start_year = int(start_date[:4])
        end_year = int(end_date[:4])
        contract_length = end_year - start_year
        return start_date, end_date, contract_length

# Apply function to contract column & create new columns
new_cols = ['Contract Start','Contract End','Contract Length(year)']
new_data = fifa['Contract'].apply(lambda x:pd.Series(extract_Contract_info(x)))

for i in range(len(new_cols)):
    fifa.insert(loc=fifa.columns.get_loc('Contract')+i+1,column=new_cols[i],value = new_data[i])


# In[13]:


fifa.sample(5)


# In[14]:


fifa[['Contract','Contract Start','Contract End','Contract Length(year)']].sample(5)


# In[15]:


fifa['Contract'].unique()


# In[16]:


def Categorize_contract_status(contract):
    if contract == 'Free':
        return 'Free'
    elif 'On Loan' in contract:
        return 'On Loan'
    else:
        return 'Contract'
# Add contract status
fifa.insert(fifa.columns.get_loc('Contract Length(year)')+1,'Contract Status',fifa['Contract'].apply(Categorize_contract_status))
fifa.sample(5)


# In[17]:


fifa['Contract Status'].unique()


# # Height Column

# In[18]:


fifa['Height'].dtype


# In[19]:


fifa['Height'].unique()


# In[20]:


def height_cms(height):
    if "cm" in height:
        return int(height.strip('cm'))
    else:
        ft,inch = height.split("\'")
        ft_cms = int(ft)
        inch_cms = int(inch.replace('"',''))
        Ht = ft_cms*30.48+inch_cms*2.54
        return int(Ht)
fifa['Height'] = fifa['Height'].apply(height_cms)


# In[21]:


fifa = fifa.rename(columns={'Height':'Height(cm)'})
fifa.sample(5)


# # Weight Column

# In[22]:


fifa['Weight'].dtype


# In[23]:


fifa['Weight'].unique()


# In[24]:


def weight_kg(weight):
    if 'kg' in weight:
        return int(weight.strip('kg'))
    else:
        return int(int(weight.strip('lbs'))*0.453592)
fifa['Weight'] = fifa['Weight'].apply(weight_kg)
fifa['Weight'].unique()


# In[25]:


fifa = fifa.rename(columns={'Weight':'Weight(kgs)'})
fifa


# In[26]:


fifa


# # Loan Date End

# In[27]:


fifa['Loan Date End'].dtype


# In[28]:


fifa['Loan Date End'].unique()


# In[29]:


Onloan = fifa[fifa['Contract Status']=='On Loan']
Onloan[['Contract','Contract Status','Loan Date End']]


# ###  Value	Wage	Release Clause	

# In[30]:


fifa[['Value','Wage','Release Clause']].info()


# In[31]:


fifa.Value.unique()


# In[32]:


fifa.Wage.unique()


# In[33]:


fifa['Release Clause'].unique()


# In[34]:


def transform_m2k(value):
    if 'M' in value:
        return int(float(value.strip('€M'))*1000000)
    elif 'K' in value:
        return int(float(value.strip('€K'))*1000)
    else:
        return int(value.strip('€'))
columns = ['Value','Wage','Release Clause']
for i in range(len(columns)):
    fifa[columns[i]] = fifa[columns[i]].apply(transform_m2k)
        


# In[35]:


fifa['Release Clause'].unique()


# In[36]:


fifa.sample(5)


# # W/F,SM,IR
# 

# In[37]:


fifa['W/F'].dtype


# In[38]:


fifa['W/F'].unique()


# In[39]:


fifa['W/F'] = fifa['W/F'].str.replace('★','')


# In[40]:


fifa['W/F'] = fifa['W/F'].str.strip()


# In[41]:


fifa['SM'].dtype


# In[42]:


fifa['SM'].unique()


# In[43]:


fifa['SM'] = fifa['SM'].str.strip('★')


# In[44]:


fifa['IR'].dtype


# In[45]:


fifa['IR'].unique()


# In[46]:


fifa['IR'] = fifa['IR'].str.strip()


# In[47]:


fifa.info()


# In[48]:


fifa['Hits'].unique()


# In[49]:


def hits_ktoTH(value):
    if pd.isna(value):  # Check if the value is NaN
        return None  # Or return a default value like 0
    value = str(value)  # Convert the value to a string
    if 'K' in value:
        return int(float(value.replace('K', '')) * 1000)
    else:
        return int(float(value))  # Handle numeric values
    
fifa['Hits'] = fifa['Hits'].apply(hits_ktoTH)


# In[50]:


fifa['Hits'].count()


# ### To CSV

# In[51]:


fifa.to_csv('Fifa_Cleaned_Dataset.csv')


# In[ ]:




