def remove_id_column(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Process each line: split by comma and join all elements except the first
    modified_lines = []
    for line in lines:
        columns = line.strip().split(',')
        new_line = ','.join(columns[1:]) + '\n'  # Join all columns except first
        modified_lines.append(new_line)
    
    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Example usage
input_file = "aafeatures.csv"    # Replace with your input file name
output_file = "outputfeat.csv"  # Replace with desired output file name
remove_id_column(input_file, output_file)