import pandas as pd
import requests
   
YOUR_SHEET_ID='1LB5ZIwnScWD1fxW2ubmljTbjRHB3V01gyAiRt7vE6Ic'

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key={YOUR_SHEET_ID}&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')

# Function to enclose each value in double quotes
IOS_df = df

quote_text = lambda x: f'"{x}"'
IOS_df = df.applymap(quote_text)
android_df = df

for col in df.columns:
        IOS_df[col] = IOS_df["English"] + " = " + IOS_df[col] + ";"

print(IOS_df.head(1))

for col in df.columns:
        with open(f'{col}.strings', 'w') as f:
            for text in IOS_df[col].tolist():
                f.write(text + '\n')
