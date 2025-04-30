# File Read & Write Program

# Function to read and write modified content
def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, "r") as input_file:
            content = input_file.read()  # Read the entire content of the file
        
        # Modify the content (e.g., add a string to it)
        modified_content = content + "\nThis is a modified version of the file."
        
        # Open the output file in write mode and write the modified content
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: Unable to read/write the file.")

# Example usage
input_filename = "input.txt"
output_filename = "output.txt"
read_and_modify_file(input_filename, output_filename)


# Error Handling Program

def read_file_with_error_handling():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open the file in read mode
        with open(filename, "r") as file:
            content = file.read()  # Read the content of the file
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IOError:
        print(f"Error: An unexpected I/O error occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_file_with_error_handling()
