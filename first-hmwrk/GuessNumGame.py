
# ---------------------------------------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    answer = None

    for key in questions:
        print("---------------------------------")
        print(key)
        for option in answers[question_num-1]:
           print(option)
        answer = input("Enter the answer (A, B, C) : ").upper()
        guesses.append(answer)

        question_num+=1
        correct_guesses += check_answer(questions.get(key),answer)
    display_score(correct_guesses,guesses)
    
# ---------------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------------------------------------------------------
def play_again():
    pass
# ---------------------------------------------------------------------
def display_score(correct_guesses,guesses):
    print("---------------------------------------------------------------------")
    print("RESULTS")
    print("---------------------------------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i),end="")
    print("Guesses: ", end="")
    for i in guesses:
        print(i,end=" ")
        
# ---------------------------------------------------------------------
questions = {
    "1/ Quel type d'ordinateur était le premier ordinateur portable ?":"C",
    "2/ Quel est le plus grand réseau de médias sociaux au monde ?":"B",
    "3/ Qui est considéré comme le fondateur de l’informatique moderne ?":"A",
    "4/ En quelle année l’iPhone est-il sorti pour la première fois ? ":"A",
    "5/ Un hibou vert est la mascotte de quelle application ?" :"C"
}
answers=[["A : Apple Macintosh","B : IBM PC","C : Osborne 1"],
         ["A : Twitter","B : Facebook","C : Instagram"],
         ["A : Alan Turing","B : Steve Jobs","C : Bill Gates"],
         ["A : 2007","B : 2009","C : 2010"],
         ["A : Spotify ","B : Tinder ","C : Duolingo"]]

new_game()