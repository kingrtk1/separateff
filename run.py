def search_and_append(input_file, output_file, search_term):
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'a') as out_file:
            for line in in_file:
                if search_term in line:
                    out_file.write(line)

        print(f"Search and append completed. Results appended to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path of the output file: ")

    while True:
        search_term = input("Enter the search term (or type 'exit' to end): ")
        if search_term.lower() == 'exit':
            break

        search_and_append(input_file, output_file, search_term)
