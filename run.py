import os

def extract_blocks_with_keywords(file_path, search_terms, output_file_path):
    with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        current_block = []
        for line in input_file:
            current_block.append(line)

            if any(search_term.strip() == line.strip() for search_term in search_terms):
                output_file.write(''.join(current_block))
                current_block = []

    print(f"search terms extracted and saved to: {output_file_path}")

if __name__ == "__main__":
    # Ask the user for input file, search terms, and manual output file path
    input_file_path = input("Enter the input file path: ")
    search_terms = []

    print("Enter search terms. Type 'done' on line when finished:")
    while True:
        term = input()
        if term.lower() == 'done':
            break
        search_terms.append(term)

    output_file_path = input("Enter the manual output file path: ")

    # Run the extraction function
    extract_blocks_with_keywords(input_file_path, search_terms, output_file_path)
