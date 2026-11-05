
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

           # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index}-{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed successfully!"
            print(message)

        case "exit":
            break

print("Goodbye!")