import pandas as pd

# Read the CSV file
df = pd.read_csv('RNA_vs_others.csv')  # Replace with your actual file name

# Count the number of 1's in BinaryClass column
count_ones = (df['BinaryClass'] == 1).sum()
count_zeros = (df['BinaryClass'] == 0).sum()
total_rows = len(df)

print(f"Number of 1's: {count_ones}")
print(f"Number of 0's: {count_zeros}")
print(f"Total rows: {total_rows}")
print(f"Percentage of 1's: {(count_ones/total_rows)*100:.2f}%")