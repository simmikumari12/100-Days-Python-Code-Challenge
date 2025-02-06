import sys 
import os

file_name = "ToDo.txt"
def main():
    
    create_todo_list()
    if len(sys.argv) == 3:
        if sys.argv[1] == "add":
            add_to_list()
        elif sys.argv[1] == "remove":
            remove_from_list(int(sys.argv[2]))
            pass
    read_todo_list()

# Create Todo
def create_todo_list():
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            num_lines = len(lines)
    except FileNotFoundError:
        with open(file_name, "a") as f:
            f.write("Here's your to do list:\n\n")
            f.write("1. Ace Resident Assistant Interview")
    else:
        if num_lines == 0:
            with open(file_name, "a") as f:
                f.write("Here's your to do list:\n\n")
                f.write("1. Ace Resident Assistant Interview")


# Add Todo
def add_to_list():
    with open(file_name, "a") as f:
        f.write(f"{sys.argv[2]}\n")

# Remove Todo
def remove_from_list(n):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            del lines[n+1]
        with open(file_name, "a"):
                f.writelines(lines)     
    except:
        print(f"Nothing at {n+1} to remove")

# Read Todo
def read_todo_list():
    with open(file_name, "r") as f:
        print(f.read())

    with open("todo_commands.txt", "r") as c:
        print(c.read())

if __name__ == "__main__":
    main()



# print("\nHere's your ToDo List:\n")
# print("1. Ace TeleCom & Social Media Influencer Interview")
# print("2. Complete Raj Sunderaman's Assigment")
# print("3. Study for Chem Exam")
# print("4. Study for Math Exam")
# print("5. Start working on next Youtube Video,'Things to know before coming to GSU' or 'My first semester experience at college in USA' or 'Do's and Don't of SAT'or 'A day in my life in Spring semester/ winter vacation")
# print("6. Prepare for Summer Confrence Leadership Position Interview")
# print("8. Prepare for th RA Interview")

