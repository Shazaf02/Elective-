def read_file_into_list(file_name):
    
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
           
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

