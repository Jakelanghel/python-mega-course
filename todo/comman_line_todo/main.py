import os
import platform

tasks = []
usr_action = "complete"


def clear_terminal():
    # Get the current operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        # Windows command to clear the terminal
        os.system('cls')
    else:
        # Unix-based systems (Linux, macOS) command to clear the terminal
        os.system('clear')

def get_action():
    print("Type add, show, edit, or exit: ")
    usr_action = input()
    return usr_action.strip()

def add_task():
    clear_terminal()
    print("Please enter a task: or enter complete to go back to main menu")
    new_task = input()
    new_task = new_task.strip().lower()
    if new_task == "":
        return "add"
    elif new_task == "complete":
        return "complete"
    
    tasks.append(new_task)
    return "add"


def show_tasks():
    clear_terminal()
    if not tasks:
        print("There are no tasks to show.")
    for i in range(len(tasks)):
        print(f"task ID:{i + 1}: {tasks[i]}")
    return None


def check_task_index(usr_input):
    try:
        task_index = int(usr_input)
        if 1 <= task_index <= len(tasks):
            return task_index - 1
        else:
            raise ValueError
    except ValueError:
        print("Invalid task ID. Please enter a valid number.")
        return None
      

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
    print("Please select the task ID that you would like to edit. or enter complete to return to main menu")
    usr_input = input()
    if usr_input.lower() == 'complete':
        return None

    task_index = check_task_index(usr_input)
    if task_index is not None:
        edit_task(task_index)
    
    
while True:
    match usr_action:
        case "complete": 
             clear_terminal()
             usr_action = get_action()
        case "add":
            usr_action = add_task()
        case "show":
            usr_action = show_tasks()
            get_action()
        case "edit":
            usr_action = edit_tasks()
        case "exit":
            break
        case _:
            clear_terminal()
            print("That is not a valid command! Please enter add, show, edit or exit:")
            usr_action = input()
            usr_action = usr_action.strip()
           
            





            

    
        
   



