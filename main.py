from readme_gen import ReadmeGen
from questions import (
    title,
    description,
    installation,
    usage,
    license,
    author,
    contact,
    confirm,
)

readme_gen = ReadmeGen(
    title, description, installation, usage, license, author, contact
)


def main():
    if confirm:
        readme_gen.write_readme()


if __name__ == "__main__":
    main()
