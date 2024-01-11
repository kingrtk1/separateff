import os

def extract_blocks_with_keywords(file_path, search_terms, output_file_path):
    try:
        with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            current_block = []

            for line in input_file:
                current_block.append(line)

                if any(search_term.strip() == line.strip() for search_term in search_terms):
                    output_file.write(''.join(current_block))
                    current_block = []

            # Check if there's an incomplete block at the end
            if current_block:
                output_file.write(''.join(current_block))

        print(f"search terms extracted and saved to: {output_file_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Add the logo
    logo = """
     SSS   EEEEE  PPPP     A    RRRR     A    TTTTT  EEEEE  
    S      E      P   P   A A   R   R   A A     T    E      
     SSS   EEE    PPPP   AAAAA  RRRR   AAAAA    T    EEE    
        S  E      P      A   A  R  R   A   A    T    E      
     SSS   EEEEE  P      A   A  R   R  A   A    T    EEEEE  
    """
    print("\033[93m" + logo + "\033[0m")  # Use ANSI escape codes for color

    # Ask the user for input file, search terms, and manual output file path
    input_file_path = input("Enter the input file path: ")
    
    search_terms = []
    print("Enter the search terms. Type 'done' on  new line when finished:")
    
    while True:
        term = input()
        if term.lower() == 'done':
            break
        search_terms.append(term)

    output_file_path = input("Enter the output file path: ")

    # Run the extraction function
    extract_blocks_with_keywords(input_file_path, search_terms, output_file_path)

    # Ask the user whether to continue
    response = input("Do you want to continue? (y/n): ")
    
    if response.lower() != 'y':
        print("Exiting the script.")
