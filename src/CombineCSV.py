import pandas as pd

# Read both CSV files
df1 = pd.read_csv('processed_sequences_features.csv')  # file with Class, A, C, D...
df2 = pd.read_csv('aafeatures.csv')  # file with ID, PCP_PC...

# Remove the ID column from the second dataframe
df2 = df2.drop('ID', axis=1)

# Combine horizontally (side by side)
combined = pd.concat([df1, df2], axis=1)

# Save the combined result
combined.to_csv('combined.csv', index=False)