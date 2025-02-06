import sys
with open("try.txt", "a") as f:
    f.write("\n")
    f.write(sys.argv[1])
