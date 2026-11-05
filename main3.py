def get_todos():
    with open("files/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

       # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Please enter a valid number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed successfully!"
            print(message)
        except IndexError:
            print("There is no item as this number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid. ")

print("Goodbye!")