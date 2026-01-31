import pandas as pd

# Sahi 'Raw' URL use karein
url = 'https://raw.githubusercontent.com/ravindra00123/demo2/main/sales_data.csv'

# CSV file load karein
df = pd.read_csv(url)

# Example kaam: Har row mein ek column add karein
df['New_Column'] = 'Processed'

# Naya result save karein
df.to_csv('result.csv', index=False)

print("File processed successfully!")
