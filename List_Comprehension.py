
##################################################
# List Comprehensions
##################################################

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

df = sns.load_dataset("car_crashes")

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

["NUM_" + col.upper() if df[col].dtype == "float64" else col.upper() for col in df.columns]

# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################

##### 1. ÇÖZÜM #####
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

##### 2. ÇÖZÜM #####
[col.upper()+"_FLAG" if  'no'  not in col else col.upper() for col in df.columns  ]

##### 3. ÇÖZÜM #####
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
#
og_list = ["abbrev", "no_previous"]

##### 1. ÇÖZÜM #####
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

##### 2. ÇÖZÜM #####
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head(10)
new_df.tail()
