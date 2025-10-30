from utilities import handle_write
from questions import (
    title,
    description,
    installation,
    author,
    contact,
    license,
    confirm,
)

readme_content = f"""# About The Project
\n### {title}
\n{description}
\n## Installation Instructions
\n{installation}
\n## Usage
\nUse this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
\n## License
\nDistributed under the {license}. See LICENSE.txt for more information.
\n## Contact
\n### Author
\n{author}
\n### Please contact me:
\n{contact}
"""


def main():
    if confirm:
        handle_write(readme_content)


if __name__ == "__main__":
    main()
