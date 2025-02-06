import sys 

def main():
    create_todo_list()
    if len(sys.argv) == 3:
        if sys.argv[1] == "add":
            add_to_list()
        elif sys.argv[1] == "remove":
            remove_from_list(int(sys.argv[2]))
            pass
    read_todo_list()

# Add Todo
def add_to_list():
    with open("ToDo.txt", "a") as f:
        f.write("\n")
        f.write(sys.argv[2])

# Remove Todo
def remove_from_list(n):
    with open("ToDo.txt", "r") as f:
        lines = f.readlines()
        
        print(lines[n + 1])

# Create Todo
def create_todo_list():
    try:
        with open("ToDo.txt", "r") as f:
            pass
            # print(f.read())
    except FileNotFoundError:
        with open("ToDo.txt", "a") as f:
            f.write("Here's your to do list:\n\n")
            f.write("1. Ace Resident Assistant Interview\n")

# Read Todo
def read_todo_list():
    try:
        with open("ToDo.txt", "r") as f:
            print(f.read())
    except:
        pass
    else:
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

