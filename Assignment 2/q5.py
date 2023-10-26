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

