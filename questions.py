from InquirerPy import inquirer
from utilities import print_section_title

print(
    """
Welcome ReadmeGenPY.

Please follow the prompts to generate your readme.

You can use markdown to add your installation steps on each line. Press Esc + Enter when done. Eg: 1. Create virtual environment `python3 -m venv .venv` 2. Install requirements 
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
