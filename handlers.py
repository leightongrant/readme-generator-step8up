def handle_write(content: str) -> None:
    try:
        with open('README2.md', 'w') as file_handler:
            file_handler.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")


def handle_read(filename: str) -> None:
    try:
        with open(filename, "r") as file_handler:
            file_content = file_handler.read()
            print(file_content)
    except Exception as e:
        print(f"An error occurred: {e}")
