import pandas as pd

# Read the original CSV file
df = pd.read_csv('combined.csv')

# Get list of all columns
cols = list(df.columns)

# Remove 'Class' from the list and add it at the end
cols.remove('Class')
cols.append('Class')

# Create new DataFrame with reordered columns
new_df = df[cols]

# Save to new file
new_df.to_csv('processed_features.csv', index=False)