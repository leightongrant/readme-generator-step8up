from InquirerPy import inquirer


title = inquirer.text(message="Project Title: ",
                      default="Readme Generator").execute()

description = inquirer.text(
    message="Project Description: ", default="A Python-based command-line tool to generate professional README.md files through a series of interactive prompts.").execute()

installation = inquirer.text(
    message="Enter installation instructions: ", multiline=True, default="* Install the interactive prompt dependency `pip3 install -r requirements.txt`").execute()

license = inquirer.select(
    message="Pick a License: ",
    choices=[
        "MIT License"
        "Apache License 2.0",
        "GNU General Public License (GPL) v3",
        "Mozilla Public License 2.0",
        "BSD 3-Clause License",
    ],
    default="MIT License",
).execute()

usage = inquirer.text(message="Usage: ", multiline=True,
                      default="Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.")

author = inquirer.text(message="Author Name: ").execute()

contact = inquirer.text(message="Contact Info : ", multiline=True).execute()


confirm = inquirer.confirm(message="Confirm?").execute()
