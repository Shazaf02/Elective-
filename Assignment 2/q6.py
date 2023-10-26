def read_file(file_name):

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            print("File Contents:")
            print(file_contents)
            return file_contents
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def read_file_into_list(file_name):
   
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]  # Remove newline characters
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_first_line_to_file(file_contents, output_filename):
    
    try:
        # Split the file_contents by the first newline character ('\n')
        first_line = file_contents.split('\n', 1)[0]

        # Write the first line into the output file
        with open(output_filename, 'w') as file:
            file.write(first_line)

        print(f"First line '{first_line}' written to '{output_filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_even_numbered_lines(file_name):
    
    try:
        even_lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Extract even-numbered lines (considering 0-based index)
            even_lines = [lines[i] for i in range(1, len(lines), 2)]
        return even_lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def read_file_in_reverse(file_name):
    
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            reversed_lines = list(reversed(lines))
            print("Lines in Reverse Order:")
            print(reversed_lines)
            return reversed_lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    file_contents = read_file("sampletext.txt")
   
if __name__ == "__main__":
    main()
