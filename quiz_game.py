questions=("1.Who developed Python Programming Language?",
           "2.Which type of Programming does Python support?",
           "3.Is Python case sensitive when dealing with identifiers?",
           "4.Which of the following is the correct extension of the Python file?",
           "5.Is Python code compiled or interpreted?",
           "6.Which of the following is used to define a block of code in Python language?",
           "7.Which keyword is used for function in Python language?",
           "8.Which of the following character is used to give single-line comments in Python?",
           "9.What does pip stand for python?",
           "10.Which of the following functions is a built-in function in Python?")

options=(("A.Wick van Rossum","B.Rasmus Lerdorf","C.Guido van Rossum","D.Niene Stom"),
         ("A.Objected oriented programming","B.Structured programming","C.functional programming","D.all of the above mentioned"),
         ("A.no","B.yes","C.machine dependent","D.none of the mentioned"),
         ("A..python","B..pl","C..py","D..p"),
         ("A.Python code is both compiled and interpreted","B.Python code is neither compiled nor interpreted","C.Python code is only compiled","D.Python code is only interpreted"),
         ("A.indentation","B.key","C.Brackets","D.All of the above mentioned"),
         ("A.function","B.def","C.define","D.fun"),
         ("A.//","B.#","C.!","D./*"),
         ("A.pip install Python","B.pip install packages","C.preferred installer program","D.All of the above mentioned"),
         ("A.factorial","B.print","C.seed","D.sqrt"))
         

answers=("C","D","B","C","A","A","B","B","C","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter your option:").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score +=1
        print("CORRECT")
    else:
        print("IN CORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("-----------------------")
print("       RESULTS         ")
print("-----------------------")

print("answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score=int(score/len(questions) * 100)
print(f"Your score is: {score}%")
