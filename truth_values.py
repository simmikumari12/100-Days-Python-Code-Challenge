import sys

def main():

    print("\n")
    truth_values = ["True", "False"]
    p = input("Truth value for p: ").title()
    if p not in truth_values:
        sys.exit("Invalid Truth for 'p'")
        
    q = input("Truth value for q: ").title()
    if q not in truth_values:
        sys.exit("Invalid Truth Value for 'q'")

    print("p and q:",conjunction(p,q))
    print("p or q:", disjunction(p,q))
    print("p xor q:", exclusive_or(p,q))
    print("p --> q:", conditional(p,q))
    print("p <--> q:", bi_conditional(p,q))

    print("\n")

def conjunction(a,b):
    return True if a == "True" and b == "True" else False

def  disjunction(a,b):
    return False if a == "False" and b == "False" else True

def exclusive_or(a,b):
    return True if a != b else False
    
def conditional(a,b):
    return False if a == "True" and b == "False" else True
    
def bi_conditional(a,b):
    return True if a == b else False

if __name__ == "__main__":
    main()