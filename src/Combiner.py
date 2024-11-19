import pandas as pd
from collections import Counter

# File paths
original_file_path = 'processed_features.csv'
sequences_file_path = 'sequences_training.csv'

# Load the datasets
original_data = pd.read_csv(original_file_path)
sequences_data = pd.read_csv(sequences_file_path, header=None)  # No header in sequences file

# Extract sequences and classifications
sequences_data.columns = ['sequence', 'classification']  # Assign column names

# Ensure row alignment if necessary
if len(original_data) != len(sequences_data):
    raise ValueError("The number of rows in the original dataset and the sequences dataset must match!")

# Add the sequences and classification to the original dataset
original_data['sequence'] = sequences_data['sequence']

# List of amino acids
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Generate all possible dipeptides
dipeptides = [a1 + a2 for a1 in amino_acids for a2 in amino_acids]

# Create a DataFrame for dipeptide frequencies initialized with float values
dipeptide_df = pd.DataFrame(0.0, index=original_data.index, columns=dipeptides)


# Function to calculate dipeptide frequencies for a single sequence
def calculate_dipeptide_frequencies(sequence):
    if not isinstance(sequence, str) or len(sequence) < 2:
        return {dp: 0.0 for dp in dipeptides}  # Handle invalid or too-short sequences

    # Count dipeptides in the sequence
    dipeptide_counts = Counter([sequence[i:i + 2] for i in range(len(sequence) - 1)])
    total_dipeptides = sum(dipeptide_counts.values())

    # Normalize frequencies
    return {dp: dipeptide_counts.get(dp, 0) / total_dipeptides if total_dipeptides > 0 else 0.0 for dp in dipeptides}


# Calculate dipeptide frequencies for each row in the dataset
for index, row in original_data.iterrows():
    frequencies = calculate_dipeptide_frequencies(row['sequence'])
    for dipeptide, freq in frequencies.items():
        dipeptide_df.at[index, dipeptide] = freq

# Concatenate the dipeptide frequencies back to the original dataset
result = pd.concat([original_data, dipeptide_df], axis=1)

# Save the resulting dataset with dipeptide frequencies and classification
output_path = 'combined_with_dipeptide_frequencies.csv'
result.to_csv(output_path, index=False)

# Display the first few rows of the updated dataset
result.head()
