import pandas as pd

# CSV file ko load karein
df = pd.read_csv('data.csv')

# Example kaam: Har row mein ek column add karein
df['New_Column'] = 'Processed'

# Naya result save karein
df.to_csv('result.csv', index=False)
print("File processed successfully!")
