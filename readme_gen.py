from os import path
from sys import exit


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

    def content(self):
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

    def write_readme(self) -> None:
        try:
            with open("README.md", "w") as file_handler:
                if path.exists("README.md"):
                    confirm = input(
                        "README.md already exist. Do you want to overwrite? y/n: "
                    )
                    if confirm == "y":
                        file_handler.write(self.content())
                        print("Your README.md has been created.")
                    elif confirm == "n":
                        print("Your file was not overwritten.")
                        exit(0)
                    else:
                        self.write_readme()

        except Exception as e:
            print(f"An error occurred: {e}")
