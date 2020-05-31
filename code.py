# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x: x.lower())
df['total'] = df['Jan'] + df['Feb'] +df['Mar']

sum_row = df[['Jan','Feb','Mar','total']].sum()
df_final= df.append(sum_row,ignore_index=True)

# Code ends here


# --------------
import requests

# Code starts here


url ="https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1 = df1[11::]
df1.rename(columns = df1.loc[11],inplace=True )
df1.drop(df1.index[0],inplace=True)  
df1["United States of America"] = df1["United States of America"].str.replace(" ","")




# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping =dict(zip(df1['United States of America'],df1['US']))
df_final['abbr'] = df_final['state'].map(mapping)
print(df_final['abbr'])

# Code ends here


# --------------
# Code stars here
df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan,'MS')

df_final.replace(df_final.iloc[6],df_mississipi,inplace=True)


df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan,'TN')

df_final.replace(df_final.iloc[10],df_tenessee,inplace=True)


# Code ends here



# --------------
# Code starts here

df_sub = df_final.groupby(['abbr'])[["Jan","Feb","Mar","total"]].sum()
formatted_df = df_sub.applymap(lambda x: '$'+str(x))


# Code ends hee


# --------------
# Code starts here
sum_row  =df[['Jan','Feb','Mar','total']].sum()
df_sub_sum = sum_row.T
df_sub_sum = df_sub_sum.apply(lambda x: '$'+str(x))
final_table = formatted_df.append(df_sub_sum,ignore_index=True)
print(final_table)
final_table.rename(index = {13:'Total'},inplace=True)


# Code ends here


# --------------
# Code starts here

df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']

df_sub['total'].plot.pie(figsize=(5,5))
plt.show()

# Code ends here


