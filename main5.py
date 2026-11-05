#from functions import get_todos, write_todos
import functions
import time
"""functions is a module"""
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

       # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Please enter a valid number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)

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