import argparse

def convert_to_fasta(input_file, output_file):
    with open(input_file, 'r') as f:
        entries = [line.strip().split(',') for line in f if line.strip()]
    
    with open(output_file, 'w') as f:
        for seq, category in entries:
            f.write(f">{category}\n")
            for j in range(0, len(seq), 60):
                f.write(f"{seq[j:j+60]}\n")

def main():
    parser = argparse.ArgumentParser(description='Convert sequence text file to FASTA format')
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output FASTA file')
    args = parser.parse_args()
    
    convert_to_fasta(args.input, args.output)

if __name__ == '__main__':
    main()