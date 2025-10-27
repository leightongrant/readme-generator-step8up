from InquirerPy import inquirer


title = inquirer.text(message="Project Title:").execute()
description = inquirer.text(message="Project Descripton:").execute()
installation = inquirer.text(message="Enter installation message:").execute()
licenses = inquirer.select(
    message="Pick a License:",
    choices=[
        "Apache License 2.0",
        "GNU General Public License (GPL) v3",
        "Mozilla Public License 2.0",
        "BSD 3-Clause License",
    ],
    default="MIT License",
).execute()


confirm = inquirer.confirm(message="Confirm?").execute()
