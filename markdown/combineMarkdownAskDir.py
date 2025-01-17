import os

# Prompt the user to input the target directory path
directory = input("Enter the path to the directory containing markdown files: ").strip()
if not os.path.isdir(directory):
    print("Invalid directory. Please check the path and try again.")
    exit(1)

output_filename = os.path.basename(directory.rstrip(os.sep)) + ".md"

# List all markdown files and sort them alphabetically
markdown_files = sorted([f for f in os.listdir(directory) if f.endswith(".md") and os.path.isfile(os.path.join(directory, f))])

if not markdown_files:
    print("No markdown files found in the specified directory.")
else:
    with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as output_file:
        for markdown_file in markdown_files:
            # Use the filename (without extension) as the section header
            section_header = os.path.splitext(markdown_file)[0]
            output_file.write(f"# {section_header}\n\n")
            
            # Read and write the content of the markdown file
            with open(os.path.join(directory, markdown_file), 'r', encoding='utf-8') as input_file:
                content = input_file.read()
                output_file.write(content + "\n\n")

    print(f"Combined markdown files into '{output_filename}' in the specified directory.")
