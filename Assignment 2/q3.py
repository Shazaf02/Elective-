def write_first_line_to_file(file_contents, output_filename):
   
    try:
        with open(output_filename, 'w') as file:
            file.write(first_line)
            print(f"First line '{first_line}' written to '{output_filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

