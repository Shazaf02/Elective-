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
