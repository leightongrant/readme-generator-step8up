from InquirerPy import inquirer


def print_section_title(title: str, dashes=20) -> None:
    print("\n", "-" * dashes, " ", title.capitalize(), " ", "-" * dashes, "\n")


print_section_title("About Your Project")

title = inquirer.text(
    message="What is the title of your project: ",
    default="Readme Generator",
    mandatory=True,
).execute()

description = inquirer.text(
    message="Project Description: ",
    default="A Python-based command-line tool to generate professional README.md files through a series of interactive prompts.",
    mandatory=True,
).execute()

print_section_title("How to install this project")

installation = inquirer.text(
    message="Enter installation instructions: ",
    instruction="This is a multiline input for the installation section",
    multiline=True,
    default="* Clone repository: `git clone repo`",
    mandatory=True,
).execute()

print_section_title("how to use this project")

usage = inquirer.text(
    message="Usage: ",
    instruction="This is a multiline input displayed at the bottom of the prompt",
    multiline=True,
    default="1. Answer each prompt with relevant information about your project",
    mandatory=True,
).execute()


print_section_title("Choose a license")

license = inquirer.select(
    message="Choose a license for your project: ",
    choices=[
        "MIT License" "Apache License 2.0",
        "GNU General Public License (GPL) v3",
        "Mozilla Public License 2.0",
        "BSD 3-Clause License",
    ],
    default="MIT License",
    mandatory=True,
).execute()


print_section_title("contact information")

author = inquirer.text(
    message="Author Name: ", default="Leighton Grant", mandatory=True
).execute()

contact = inquirer.text(
    message="Contact Info : ", default="* dev@leightongrant.me", instruction="", multiline=True, mandatory=True
).execute()

confirm = inquirer.confirm(message="Confirm?", mandatory=True).execute()
