# File Handling and Exception Handling Assignment
# ----------------------------------------------
# Task 1: File Read & Write Challenge
# Task 2: Error Handling Lab

def read_and_modify_file(input_filename, output_filename):
    """
    Reads content from an input file, modifies it (example: uppercase),
    and writes the modified content to an output file.
    """
    try:
        # Open the input file in read mode
        with open(input_filename, "r") as infile:
            content = infile.read()  # Read everything from the file

        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()

        # Write the modified content into the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        # Handles the case where the input file doesn’t exist
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")

    except PermissionError:
        # Handles if we don’t have permission to read/write the file
        print(f"Error: You don’t have permission to access '{input_filename}' or '{output_filename}'.")

    except Exception as e:
        # Catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Ask user for the input filename
input_filename = input("Enter the name of the file to read from: ")

# Ask user for the output filename
output_filename = input("Enter the name of the new file to write to: ")

# Call the function
read_and_modify_file(input_filename, output_filename)
