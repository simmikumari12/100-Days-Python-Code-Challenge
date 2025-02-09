import sys
import csv


# Checks Input Validity
sys_len = len(sys.argv)
if sys_len <= 2:
    sys.exit("Too few command-line arguments")

if sys_len > 3:
    sys.exit("Too many command-line arguments")

unordered_csv = sys.argv[1]
ordered_csv = sys.argv[2]
ls = []
try:
    with open(unordered_csv, "r") as f:
        for line in f.readlines():
            ls.append(line.split(","))
except FileNotFoundError:
    sys.exit(f"Could not read {old_csv}")


with open(ordered_csv, "a") as f2:
    f2.write(",".join(ls[0]))
    for i in range(1,len(ls)):
        # f2.write(f'"{(ls[i][1]).replace('"',"").replace(' ','').strip()}, {(ls[i][0]).replace('"',"")}",{ls[i][2]}')
        f2.write(f'{(ls[i][1]).replace('"',"").replace(' ','').strip()}, {(ls[i][0]).replace('"',"")}, {ls[i][2]}')