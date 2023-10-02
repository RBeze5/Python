# Function to extract and save code blocks
def extract_and_save_code_blocks(input_file):
    with open(input_file, 'r') as md_file:
        markdown_lines = md_file.readlines()

    code_block_started = False
    code_block_extension = None
    code_block_content = []

    for line in markdown_lines:
        # Check if a code block starts
        if line.startswith("```"):
            if not code_block_started:
                # Extract the extension from the opening line of the code block
                code_block_extension = line.strip()[3:]
                code_block_started = True
            else:
                # Code block ends, save it to a file
                if code_block_extension:
                    # Generate a unique filename for each code block
                    filename = f"code_block_{hash(''.join(code_block_content))}.{code_block_extension}"

                    # Save the code block to a file with the appropriate extension
                    with open(filename, 'w') as code_file:
                        code_file.writelines(code_block_content)

                    print(f"Saved code block as '{filename}'")

                code_block_started = False
                code_block_extension = None
                code_block_content = []
        elif code_block_started:
            code_block_content.append(line)

if __name__ == "__main__":
    input_file = input("Enter the path to the Markdown file (.md): ")
    extract_and_save_code_blocks(input_file)
