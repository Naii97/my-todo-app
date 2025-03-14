FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """Read a text file and return a list of to-do Items"""

    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do list to the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())