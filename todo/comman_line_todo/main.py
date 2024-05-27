import os
import platform


add = False
show = False
edit = False
complete = False
exit = False    

tasks = []
command = None


def clear_terminal():
    # Get the current operating system
    current_os = platform.system()
    
    if current_os == "Windows":
        # Windows command to clear the terminal
        os.system('cls')
    else:
        # Unix-based systems (Linux, macOS) command to clear the terminal
        os.system('clear')




def initial_prompt():
    prompt = "Type add, show, edit, complete or exit:"
    valid = ["add", "show", "edit", "complete", "main", "exit"]
    initial = True
    usr_input = None

    while initial:
        print(prompt)
        txt = input()
        if txt in valid:
            usr_input = txt
            initial = False
        
    return usr_input


def add_task():
    clear_terminal()
    prompt = "Please enter a task: or enter complete to go back to main menu"
    print(prompt)
    new_task = input()
    if complete(new_task):
        return None
    else:
        tasks.append(new_task)
        return "add"
    


def show_tasks():
    clear_terminal()
    print(tasks)
    return None
    
    

def edit_tasks():
    clear_terminal()
    if len(tasks) == 0:
        print("There are no tasks to edit.")
        return None
    else:
        print("Please select the task ID that you would like to edit. or enter complete to return to main menu")
        for i in range(len(tasks)):
            print("task-ID:" + str(i + 1) + " " + tasks[i])
        usr_input = input()
        task_index = check_task_index(usr_input)
        task_index -= 1
        clear_terminal()
        print("Here is the task you selected, please enter new task to overwrite:")
        print(tasks[task_index])
        edited_task = input()
        if complete(edited_task):
            return None
        else: 
            tasks[task_index] = edited_task

    
    

    

def check_task_index(index):
    while index.isdigit() == False or int(index) > len(tasks):
        print("That is not a valid selection.")
        print("Please enter the ID of the task you would like to edit:")
        index = input()
    return int(index)
        

def complete(command):
    if command == "complete":
        clear_terminal()
        return True


def exit_program():
    return True




    

while exit == False:
    if command == None:
        command = initial_prompt()
    if command == "add":
        command = add_task()
    elif command == "show":
        command = show_tasks()
    elif command == "edit":
        command = edit_tasks()
    elif command == "main":
        print("main")
    elif command == "exit":
        exit = exit_program()
    
    
        
   



