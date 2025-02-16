def main():
    
    p = input("Truth value for p: ").title()
    q = input("Truth value for q: ").title()
    print("p and q:",conjunction(p,q))
    print("p or q:", disjunction(p,q))
    print("p xor q:", exclusive_or(p,q))
    print("p --> q:", conditional(p,q))
    print("p <--> q:", bi_conditional(p,q))

def conjunction(a,b):
    if a == True and b == True:
        return True
    else:
        return False

def  disjunction(a,b):
    if a == False and b == False:
        return False
    else:
        return True

def exclusive_or(a,b):
    if a != b:
        return True
    else:
        return False
    
def conditional(a,b):
    if a == True and b == False:
        return True
    else:
        return False
    
def bi_conditional(a,b):
    if a == b:
        return True
    else:
        return False

    


if __name__ == "__main__":
    main()