import os
import subprocess
from datetime import datetime

# Get today's date
today_date = datetime.now().strftime("%B %-d, %Y")

# Function to get class name from .git repo name
def get_class_name():
    try:
        # Run git command to get the repo name
        repo_name = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL)
        repo_name = repo_name.decode('utf-8').strip()
        class_name = os.path.basename(repo_name).replace("-", " ")
        return class_name
    except Exception:
        return "Unknown Class"

# Function to load LaTeX boilerplate from a file
def load_boilerplate(file_name):
    try:
        with open(file_name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return """\\documentclass{article}
\\usepackage{fancyhdr}
\\usepackage{graphicx}
\\usepackage{float}
\\usepackage{hyperref}
\\hypersetup{hidelinks}

\\begin{document}
\\end{document}"""

# Get class name from repo
class_name = get_class_name()

# Ask user for assignment number
assignment_number = input("Enter the assignment number: ")

# Load LaTeX boilerplate
boilerplate = load_boilerplate("latex/boilerplate.txt")

# Replace placeholders in the boilerplate
latex_document = boilerplate.replace("{CLASS_NAME}", class_name)
latex_document = latex_document.replace("{ASSIGNMENT_NUMBER}", assignment_number)
latex_document = latex_document.replace("{DATE}", today_date)

# Save to a .tex file
output_file = f"a{assignment_number}.tex"
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
