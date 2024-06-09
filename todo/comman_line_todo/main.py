import os
import platform


usr_action = "back"

file = open("todos.txt", "r")
tasks = file.readlines()
file.close()




def clear_terminal():
    # Get the current operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        # Windows command to clear the terminal
        os.system('cls')
    else:
        # Unix-based systems (Linux, macOS) command to clear the terminal
        os.system('clear')


def check_back_exit(input):
    input = input.lower()
    if input == "back" or input == "exit":
        return input
    return False

def get_action():
    print("Type add, show, edit, complete or exit: ")
    usr_action = input()
    return usr_action.strip()


def add_task():
    clear_terminal()
    print("Please enter a task: or enter back to go back to main menu")
    new_task = input()
   
    new_task = new_task.strip()
    command = check_back_exit(new_task)
    if not command:
        if new_task != "":
            tasks.append(new_task)
            file = open("todos.txt", "w")
            file.write("\n".join(tasks) + "\n")
            file.close()
        return "add"
    return command
    


def show_tasks():
    clear_terminal()
    print(tasks)
    if not tasks:
        print("There are no tasks to show.")
    for i, task in enumerate(tasks):
        print(f"task_ID:{i + 1}: {task}")

    


def check_task_index(usr_input):
    def prompt_user():
        clear_terminal()
        show_tasks()
        return input("Invalid ID! Please enter a task ID from the list above: ")

    while True:
        try:
            task_index = int(usr_input)
            if 1 <= task_index <= len(tasks):
                return task_index - 1
            else:
                raise ValueError
        except ValueError:
            usr_input = prompt_user()

    

      

def edit_task(task_index):
    clear_terminal()
    print("Here is the task you selected, please enter a new task to overwrite:")
    print(tasks[task_index])
    edited_task = input()
    clear_terminal()
    tasks[task_index] = edited_task
    print("Updated tasks:")
    show_tasks()
     
    

def edit_tasks():
    clear_terminal()
    if not tasks:
        print("There are no tasks to edit.")
        return None
    show_tasks()
    print("Please select the task ID that you would like to edit. or enter back to return to main menu")
    usr_input = input().lower()
    if usr_input == "back":
        return "back"
    task_index = check_task_index(usr_input)
    edit_task(task_index)



def complete_task():
    if not tasks:
        print("There are no tasks to complete.")
        action = get_action()
        return action
    show_tasks()
    print("Please enter the task ID you would like to complete.")
    usr_input = input()
    if usr_input == "back":
        return "back"
    task_index = (check_task_index(usr_input))
    tasks.pop(task_index)
    return "back"





    
    
while True:
    match usr_action:
        case "back": 
             clear_terminal()
             usr_action = get_action()
             
        case "add":
            usr_action = add_task()
        case "show":
            show_tasks()
            usr_action = get_action()
        case "edit":
            edit_tasks()
            usr_action = get_action()
        case "complete":
            usr_action = complete_task()
        case "exit":
            break
        case _:
            clear_terminal()
            print("That is not a valid command! Please enter add, show, edit, complete or exit:")
            usr_action = input()
            usr_action = usr_action.strip()
           
            





            

    
        
   



