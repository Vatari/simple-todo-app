FILEPATH = "./data/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read file and print todos """
    with open(filepath, 'r') as f:
        items_local = f.readlines()
    return items_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)


# FOR LOCAL TESTING func.py filename
if __name__ == "__main__":
    print(get_todos())
