from InquirerPy import inquirer


def print_section_title(title: str, dashes=20) -> None:
    print("\n", "-" * dashes, " ", title.capitalize(), " ", "-" * dashes, "\n")


def instructions() -> str:
    return "\n    - Type your content, using markdown formatting\n    - Use arrows to navigate through previous entries\n    - Press Esc + Enter when you're done"


def ask_questions():
    print_section_title("About Your Project")

    title = inquirer.text(
        message="What is the title of your project: ",
        default="Readme Generator",
        mandatory=True,
        mandatory_message="Title cannot be empty",
        amark="✔",
    ).execute()

    description = inquirer.text(
        message="Project Description: ",
        default="A Python-based command-line tool to generate professional README.md files through a series of interactive prompts.",
        mandatory=True,
        amark="✔",
    ).execute()

    print_section_title("How to install this project")

    installation = inquirer.text(
        message="Enter installation instructions: ",
        instruction=instructions(),
        multiline=True,
        default="* Clone repository: `git clone repo`",
        mandatory=True,
        amark="✔",
        wrap_lines=True
    ).execute()

    print_section_title("how to use this project")

    usage = inquirer.text(
        message="Usage: ",
        instruction=instructions(),
        multiline=True,
        default="1. Answer each prompt with relevant information about your project",
        mandatory=True,
        amark="✔",
    ).execute()

    print_section_title("Choose a license")

    license = inquirer.select(
        message="Choose a license for your project: ",
        choices=[
            "MIT License",
            "Apache License 2.0",
            "GNU General Public License (GPL) v3",
            "Mozilla Public License 2.0",
            "BSD 3-Clause License",
        ],
        default="MIT License",
        mandatory=True,
        amark="✔",
    ).execute()

    print_section_title("contact information")

    author = inquirer.text(
        message="Author Name: ", default="Leighton Grant", mandatory=True, amark="✔",
    ).execute()

    contact = inquirer.text(
        message="Enter contact information (e.g., email, GitHub profile):",
        instruction=instructions(),
        multiline=True,
        mandatory=True,
        amark="✔",
    ).execute()

    confirm = inquirer.confirm(message="Confirm?").execute()

    return [title,
            description,
            installation,
            usage,
            license,
            author,
            contact,
            confirm,]
