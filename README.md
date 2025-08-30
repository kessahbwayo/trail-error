# File Handling and Exception Handling Assignment

def file_read_write(input_filename, output_filename):
    """
    This function reads the content of input_filename,
    modifies the content (in this case, makes it uppercase),
    and writes it into output_filename.
    """
    try:
        # Open the input file in read mode
        with open(input_filename, "r") as infile:
            content = infile.read()   # Read the whole file content

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)   # Write modified content

        print(f"✅ File '{input_filename}' was successfully read and modified!")
        print(f"✅ Modified content saved to '{output_filename}'")

    except FileNotFoundError:
        # If file doesn't exist, show this error message
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        #
