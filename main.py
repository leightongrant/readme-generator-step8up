from os import path

# with open('README2.md', 'w') as file_handler:
#     try:
#         file_handler.write('# TITLE')
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         raise e


try:
    with open('README3.md', 'r') as file_handler:
        file_content = file_handler.read()
        print(file_content)
except Exception as e:
    print(f"An error occurred: {e}")
    # raise e

# if path.exists('README2.md'):


def main():
    print("")


if __name__ == "__main__":
    main()
