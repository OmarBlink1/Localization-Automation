import pandas as pd
import requests
   
YOUR_SHEET_ID='1LB5ZIwnScWD1fxW2ubmljTbjRHB3V01gyAiRt7vE6Ic'

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key={YOUR_SHEET_ID}&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')

# Function to enclose each value in double quotes
IOS_df = df
# Make all columns between quotations
quote_text = lambda x: f'"{x}"'

# Make all of the raw column lowercase
IOS_df["raw"] = IOS_df["English"].str.lower()

# Remove whitespaces from left and right
IOS_df["raw"] = IOS_df["raw"].str.strip()

# Replace spaces with  `_` in raw col
IOS_df["raw"] = IOS_df["raw"].apply(lambda x: x.replace(' ', '_'))

# Apply double <quote_text> to all cols
IOS_df = df.applymap(quote_text)

for col in df.columns:
        IOS_df[col] = IOS_df["raw"] + " = " + IOS_df[col] + ";"

print(IOS_df.head(1))

# Extract
for col in df.columns:
    if col != "raw":
        with open(f'{col}.strings', 'w') as f:
            for text in IOS_df[col].tolist():
                f.write(text + '\n')
