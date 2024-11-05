import pandas as pd

# Load the processed dataset with AAC features
data = pd.read_csv("processed_sequences_features.csv")

# Function to convert to binary classification
def convert_to_binary(data, positive_class):
    """Convert dataset to binary classification with a specific positive class."""
    data['BinaryClass'] = data['Class'].apply(lambda x: 1 if x == positive_class else 0)
    X = data.drop(['Class', 'BinaryClass'], axis=1)
    y = data['BinaryClass']
    return X, y

# Outcomes to classify
outcomes = ['DNA', 'RNA', 'DRNA', 'nonDRNA']

# Dictionary to store paths of binary datasets
binary_datasets = {}

# Create and save individual binary datasets
for outcome in outcomes:
    # Convert to binary classification for the specific outcome
    X, y = convert_to_binary(data, outcome)

    # Combine X and y into a single DataFrame
    binary_data = pd.concat([X, y.rename('BinaryClass')], axis=1)

    # Save the binary dataset to a separate CSV file
    output_path = f"{outcome}_vs_others.csv"
    binary_data.to_csv(output_path, index=False)

    # Store the path for reference
    binary_datasets[outcome] = output_path

# Display the paths of saved binary datasets
print(binary_datasets)
