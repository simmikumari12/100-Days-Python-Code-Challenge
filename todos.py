import sys 

def main():
    # print_func()
    if len(sys.argv) == 3:
        if sys.argv[1] == "add":
            add_to_list()
        elif sys.argv[1] == "remove":
            remove_from_list(int(sys.argv[2]))
            pass

todo_heading = ["Here's your ToDo List:\n\n","1. Ace Resident Assistant Interview\n"]

# Add Todo
def add_to_list():
    with open("list.txt", "a") as f:
        f.write("\n")
        f.write(sys.argv[2])

# Remove Todo
def remove_from_list(n):
    with open("list.txt", "r") as f:
        lines = f.readlines()
        print(lines[n + 1])

if __name__ == "__main__":
    main()


def print_func():
    for h in todo_heading:
        print(h)
    for item in todo_list:
        print(item)
    commands = ["\n*******************************************\n",f"To view ToDos: \n{sys.argv[0]}", f"\nTo add a ToDo:\n{sys.argv[0]} add \"Code CS50 Program\"\n", f"\nTo add or complete ToDo:\n{sys.argv[0]} remove 2\n"]
    for command in commands:
        print(command)












# Print List


# print("\nHere's your ToDo List:\n")
# print("1. Ace TeleCom & Social Media Influencer Interview")
# print("2. Complete Raj Sunderaman's Assigment")
# print("3. Study for Chem Exam")
# print("4. Study for Math Exam")
# print("5. Start working on next Youtube Video,'Things to know before coming to GSU' or 'My first semester experience at college in USA' or 'Do's and Don't of SAT'or 'A day in my life in Spring semester/ winter vacation")
# print("6. Prepare for Summer Confrence Leadership Position Interview")
# print("8. Prepare for th RA Interview")

#Print Commands

# print("\n*******************************************\n")
# print(f"To view ToDos: \n{sys.argv[0]}")
# print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Code CS50 Program\"\n")
# print(f"\nTo add or complete ToDo:\n{sys.argv[0]} remove 2\n")