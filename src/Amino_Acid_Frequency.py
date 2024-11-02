#SCRIPT TO COMPUTE AMINO ACID FREQUENCY
import pandas as pd

# List of 20 standard amino acids
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

def compute_aac(sequence):
    """Compute amino acid composition for a given sequence."""
    length = len(sequence)
    # Calculate the relative frequency of each amino acid
    return {aa: sequence.count(aa) / length for aa in amino_acids}

# Apply AAC feature extraction to the dataset
data['AAC'] = data['Sequence'].apply(compute_aac)

# Expand the AAC dictionary into separate columns for each amino acid
aac_features = pd.json_normalize(data['AAC'])
dataset_with_features = pd.concat([data['Class'], aac_features], axis=1)

# Save the transformed dataset to a CSV file
output_path = "/mnt/data/processed_sequences_features.csv"
dataset_with_features.to_csv(output_path, index=False)

output_path  # Returning the path to the saved file
