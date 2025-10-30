from InquirerPy import inquirer
from utilities import print_section_title

print(
    """
====================================
Welcome to ReadmeGenPY! 📝
====================================

This CLI tool helps you generate professional README.md files through interactive prompts.

How to Use This Tool:
--------------------
1. Answer each prompt with relevant information about your project
2. For multiline inputs (like installation steps):
   - Type your content, using markdown formatting
   - Press Esc + Enter when you're done
   - Use arrows to navigate through previous entries

Markdown Examples:
----------------
• Headers:      # Main Title
               ## Subheading
• Lists:        * Bullet point
               1. Numbered item
• Code:         `pip install package`
• Code blocks:  ```python
               your_code_here
               ```
• Links:        [Text](URL)

Tips:
----
• You can use the default values as templates
• Press Ctrl+C at any time to exit
• Your README will be generated in the current directory

Let's begin creating your README!
"""
)

print_section_title("About Your Project")
title = inquirer.text(
    message="What is the title of your project: ", default="Readme Generator"
).execute()
description = inquirer.text(
    message="Project Description: ",
    default="A Python-based command-line tool to generate professional README.md files through a series of interactive prompts.",
).execute()

print_section_title("How to install this project")

installation = inquirer.text(
    message="Enter installation instructions: ",
    multiline=True,
    default="* Install the interactive prompt dependency `pip3 install -r requirements.txt`",
).execute()

print_section_title("how to use this project")

usage = inquirer.text(
    message="Usage: ",
    multiline=True,
    default="Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.",
)

print_section_title("Choose a license")

license = inquirer.select(
    message="Pick a License: ",
    choices=[
        "MIT License" "Apache License 2.0",
        "GNU General Public License (GPL) v3",
        "Mozilla Public License 2.0",
        "BSD 3-Clause License",
    ],
    default="MIT License",
).execute()


print_section_title("contact information")

author = inquirer.text(message="Author Name: ", default="Leighton Grant").execute()

contact = inquirer.text(message="Contact Info : ", multiline=True).execute()

confirm = inquirer.confirm(message="Confirm?").execute()
