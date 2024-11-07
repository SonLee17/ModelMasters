def remove_second_column(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Keep only the first column by splitting on comma and taking first part
    modified_lines = [line.split(',')[0] + '\n' for line in lines]
    
    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Example usage
input_file = "sequences_training.txt"    # Replace with your input file name
output_file = "output.txt"  # Replace with desired output file name
remove_second_column(input_file, output_file)