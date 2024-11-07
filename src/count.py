import pandas as pd

def count_class_occurrences(file_path):
    """
    Reads a CSV file and counts occurrences of different classes (DNA, RNA, dRNA, nonDRNA)
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    dict: Dictionary containing counts of each class
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Initialize counter dictionary
        class_counts = {
            'DNA': 0,
            'RNA': 0,
            'DRNA': 0,
            'nonDRNA': 0
        }
        
        # Count occurrences of each class
        for class_type in df['Class'].values:
            if class_type in class_counts:
                class_counts[class_type] += 1
        
        return class_counts
        
    except FileNotFoundError:
        return "Error: File not found"
    except KeyError:
        return "Error: 'Class' column not found in the CSV file"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Replace 'your_file.csv' with your actual file path
    result = count_class_occurrences('processed_features.csv')
    
    if isinstance(result, dict):
        print("\nClass Counts:")
        for class_type, count in result.items():
            print(f"{class_type}: {count}")
    else:
        print(result)  # Print error message if any