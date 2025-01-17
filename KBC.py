#create a program to display questions to the user like KBC.
import sys
def main():
    questions = {"1: In 2022, which team became the first to score more than 500 runs on the first day of Test Match?": ["A:India", "B:Australlia", "C:New Zealand", "D:England"],
                "2: Which of the following countries is the world's largest producer of saffron?": ["A:Spain","B:Iran", "C:India", "D:Greece"],
                "3: Which god is also known as ‘Gauri Nandan’?": ["A:Agni","B:Indra","C.Hanuman","D:Ganesha"],
                "4: What does not grow on tree according to a popular Hindi saying?": ["A:Money","B:Flowers","C:Leaves","D:Fruits"],
                "5: Which city is known as the Pink City of India?": ["A:Banglore","B:Maysore","C:Jaipur", "D:Kochi"],
                "6: Who wrote India's National Anthem?": ["A:Rabindranath Tagore","B:Lal Bahadur Shastri", "C:Chetan Bhagat", "D:RK Narayan"],
                "7: How many major religions are there in India?": ["A:6", "B:7", "C:8", "D:9"],
                "8: When is the National Hindi Diwas celebrated?": ["A:13 September","B:14 September", "C:14 July", "D:15 August"],
                "9: Which country is the largest producer of coffee in the world?": ["A:Brazil", "B:Colombia", "C:Vietnam", "D:Ethiopia"],
                "10: Where is India Gate located?": ["A:Agra","B:Punjab","C:Mumbai","D:New Delhi"],
                }
    i = 0
    amt = 1000
    answers = {1:"D", 2:"B", 3:"D",4:"A", 5:"C", 6:"A", 7:"A", 8:"B", 9:"A", 10:"D"}
    try:
        for question in questions:  
            print(question) 
            print(questions[question])
            i = i + 1
            user_answer = input("").upper() 
            if user_answer == answers[i]:
                amt = amt + 2000
                print(f"Next Question for {amt}")
                continue
            elif user_answer == "QUIT":
                print(f"Amount you are taking home: {amt-2000}")
                sys.exit()
            else:
                print("Wrong Answer!")
                print(f"Amount you are taking home: {amt-2000}")
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()

 
if __name__ == "__main__":
    main()