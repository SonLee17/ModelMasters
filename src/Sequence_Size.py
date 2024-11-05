import pandas as pd

# Load the dataset
data = pd.read_csv("/mnt/data/sequences_training_with_headers.csv")

# Add a new column for the sequence length
data['Sequence_Length'] = data['Sequence'].apply(len)

# Sort the data by sequence length in descending order
# Set ascending=False for descending, or ascending=True for ascending order
sorted_data = data.sort_values(by='Sequence_Length', ascending=False).reset_index(drop=True)

# Save the sorted dataset to a CSV file
output_path = "/mnt/data/sorted_sequences_by_length.csv"
sorted_data.to_csv(output_path, index=False)

print(f"Sorted dataset saved at: {output_path}")


