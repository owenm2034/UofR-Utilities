# paste me in the repo you want to generate an assignment for


import os
import subprocess
from datetime import datetime
import sys

# Get today's date
today_date = datetime.now().strftime("%B %-d, %Y")

# Function to get class name from .git repo name
def get_class_name(target_dir):
    try:
        # Run git command to get the repo name
        repo_name = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], 
            stderr=subprocess.DEVNULL,
            cwd=target_dir)
        repo_name = repo_name.decode('utf-8').strip()
        class_name = os.path.basename(repo_name).replace("-", " ")
        return class_name
    except Exception:
        raise ValueError(f'No git repo found at {target_dir}.')

# Function to load LaTeX boilerplate from a file
def load_boilerplate(file_name):
    try:
        with open(file_name, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError('No template file found.')

if len(sys.argv) < 3:
    print("Error: Assignment number is required.")
    sys.exit(1)

assignment_number = sys.argv[1]
target_dir = sys.argv[2]

if not os.path.isdir(target_dir):
    print(f"Error: The specified target directory '{target_dir}' does not exist.")
    sys.exit(1)


# Get class name from repo
class_name = get_class_name(target_dir)

# Load LaTeX boilerplate
boilerplate = load_boilerplate("latex/boilerplate.txt")

# Replace placeholders in the boilerplate
latex_document = boilerplate.replace("{CLASS_NAME}", class_name)
latex_document = latex_document.replace("{ASSIGNMENT_NUMBER}", assignment_number)
latex_document = latex_document.replace("{DATE}", today_date)

# Save to a .tex file
output_file = f"{target_dir}/assignments/a{assignment_number}/a{assignment_number}.tex"
if os.path.exists(output_file):
    overwrite = input(f"The file '{output_file}' already exists. Do you want to overwrite it? (y/n): ")
    if overwrite.lower() != 'y':
        print("Operation cancelled. No file was overwritten.")
    else:
        with open(output_file, "w") as f:
            f.write(latex_document)
        print(f"LaTeX document generated and saved as '{output_file}'")
else:
    with open(output_file, "w") as f:
        f.write(latex_document)
    print(f"LaTeX document generated and saved as '{output_file}'")
