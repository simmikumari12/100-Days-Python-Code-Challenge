months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
  date = input("Date: ")
  
  if "/" in date:
    m, d, y = date.split("/")
    break
  elif "," in date:
    md, y  = date.split(", ")
    m, d = md.split(" ")
    if m in months:
        for i in range(len(months)):
            if months[i] == m:
                m =  i + 1
        break
    else:
        pass
  else:
     pass
print(f"{y}-{m}-{d}")