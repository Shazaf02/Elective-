def read_even_numbered_lines(file_name):
    
    try:
        even_lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            even_lines = [lines[i] for i in range(1, len(lines), 2)]
        return even_lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

