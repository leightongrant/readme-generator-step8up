from os import path
from sys import exit

def print_section_title(title: str, dashes=20) -> None:
    print("\n", "-" * dashes, " ", title.capitalize(), " ", "-" * dashes, "\n")


def handle_write(content: str) -> None:
    try:
        with open("README.md", "w") as file_handler:
            if path.exists('README.md'):
                confirm = input("README.md already exist. Do you want to overwrite? y/n: ")
                if confirm == "y":
                    file_handler.write(content)
                elif confirm == "n":
                    handle_write(content)
                else:
                    exit(0)
            print("Your README.md has been created.")
    except Exception as e:
        print(f"An error occurred: {e}")