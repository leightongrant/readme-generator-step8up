def print_section_title(title: str, dashes=20) -> None:
    print("\n", "-" * dashes, " ", title.capitalize(), " ", "-" * dashes, "\n")


def handle_write(content: str) -> None:
    try:
        with open("README.md", "w") as file_handler:
            file_handler.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")