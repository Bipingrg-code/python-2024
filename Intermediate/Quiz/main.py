#  --------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A,B,C,OR D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#  --------------------


def check_answer(answer, guess):
    if answer == guess:
        print("Correct.!")
        return 1
    else:
        print("Wrong.!")
        return 0
#  --------------------


def display_score(correct_guesses, guesses):
    print("----------------")
    print("RESULTS")
    print("----------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("your score is: " + str(score)+"%")
#  --------------------


def play_again():
    response = input("Do you want to play again.? (Yes or No): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#  --------------------


questions = {
    "Who is Pm of Nepal.?": "A",
    "Capital city of Nepal.?": "C",
    "Full form of HTML.?": "B",
    "Which is not a programming language.?": "D",
}

options = [["A. Puspa Kamal Dahal", "B. Sher Bahadur Deuba", "C. KP oli", "D.Rabi Lamichhane"], ["A. Dharan", "B. Pokhara", "C. Kathmandu", "D. Biratnagar"], [
    "A. Hyper Text Multiple Language", "B. Hyper Text Markup Language", "C. Hyper Text Mordern Language", "D. Hybrid Text Multiple Language"], ["A. Python", "B. PHP", "C. Java", "D. HTML"]]

new_game()

while play_again():
    new_game()

print("Thank you for playing with us.!")
