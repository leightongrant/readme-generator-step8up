from os import path
from sys import exit
from rich.console import Console

console = Console()


class ReadmeGen:
    def __init__(
        self, title, description, installation, usage, license, author, contact
    ) -> None:
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.license = license
        self.author = author
        self.contact = contact

    def content(self) -> str:
        readme_content = f"""# About The Project
        \n### {self.title}
        \n{self.description}
        \n## Installation Instructions
        \n{self.installation}
        \n## Usage
        \n### To use this application:
        \n{self.usage}
        \n## License
        \nDistributed under the {self.license}.
        \n## Contact
        \n### Author
        \n{self.author}
        \n### Please contact me:
        \n{self.contact}
        """
        return readme_content

    def write_file(self) -> None:
        try:
            with open("README.md", "w") as file_handler:
                file_handler.write(self.content())
                console.print(
                    "\nYour README.md has been created.\n", style="bold blue")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="red")

    def write_readme(self) -> None:
        if path.exists("README.md"):
            console.print("\nREADME.md already exist. Do you want to overwrite? y/n:\n",
                          style="blink bold red underline on white")
            confirm = input()
            if confirm == "y":
                self.write_file()
            elif confirm == "n":
                console.print("\nYour file was not overwritten.\n",
                              style="bold green")
                exit(0)
            else:
                self.write_readme()
        else:
            self.write_file()
