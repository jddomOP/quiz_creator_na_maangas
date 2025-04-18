#This is made not purely by my own, I searched for much creativity of the project
#PSEUDOCODE
#START
# 1. Display the title using pyfiglet library
# 2. Display the Main menu
#   - pick option between:
#      1. Create a Quiz
#      2. View Quiz
#      3. Delete a Question
#      4. Exit
# 3. If the user selects "Create a quiz"
#   - Prompt the user to enter what difficulty (Elementary(as easy), High School(as medium), General(as hard))
#   - After selection, it will be in a loop for the user to input questions, choices and answers
# 4. If the user selects "View Quiz":
#    - Read the saved quiz file
#    - Display all questions and answers in the stored format
#    - If no questions exist or file doesn't exist, show a message
# 5. If the user selects "Delete a Question":
#    - Load all saved questions from the file and split them using the separator line
#    - Display a numbered list of all questions
#    - Show only the question text for easier selection
#    - Ask the user to input the number of the question to delete
#    - If they type "cancel", return to the main menu
#    - If the number is valid, remove that question
#    - Rewrite the file without the deleted question
#    - Show confirmation that the question was deleted
# 6. In question loop:
#   - Ask the user to input questions
#   - If the user enter "exit" then will be redirected to main menu
#   - Otherwise, the user will be asked to input answers in the choices between a, b, c, d
#   - Prompt the user to enter the correct answer (must be in a, b, c, d)
#   - If the correct answer input is invalid, re-prompt until valid answer is given
#   - Stores the question, choices, correct answer, and difficulties in a dictionary
# 7. Write the question data to a text file in a structured format:
#   - Write the question text
#   - Write the difficulty
#   - Write the options/choices each a, b, c, d
#   - Write the correct answer
#   - Write a separator line to divide questions in text file
# 8. After saving the question, notify the user and repeat the loop to add more questions
# 9. If the user selects 'Exit' in the main menu
#   - Display goodbye message
#END


import pyfiglet

#make a function for the title
def the_title():
    title = pyfiglet.figlet_format("Welcome to the Quiz Maker!", font = 'slant')
    print(title)

#Make main menu of the code
def main_menu():
    while True:
        the_title()
        print("Main Menu")
        print("1. Create a Quiz")
        print("2. View questions")
        print("3. Delete question")
        print("4. Exit")
        choice = input("Choose an option! (1, 2, 3, 4): ")

        if choice == '1':
            create_quiz()
        elif choice == '2':
            view_quiz()
        elif choice == '3':
            delete_questions()
        elif choice == '4':
            print("Thanks for using!!")
            break
        else:
            print("Invalid input! Please try again ^_^")

def write_a_file(data, filename = 'quiz_questions_and_answers'):
    with open(filename, 'a',encoding = 'utf-8') as file:
        file.write("Q: " + data['question'] + "\n")
        file.write("Difficulty: " + data['difficulty'] + "\n")
        file.write("a). " + data['a'] + "\n")
        file.write("b). " + data['b'] + "\n")
        file.write("c). " + data['c'] + "\n")
        file.write("d). " + data['d'] + "\n")
        file.write("Answer: " + data['correct'] + "\n")
        file.write("-" * 40 +"\n")

def create_quiz():
    difficulty = input("Enter the difficulty (Elementary, High School, General): ").capitalize()
    print(f"Creating {difficulty} quiz.")

    while True:
        question = input("Enter your desired question (or type 'exit' to go back to main menu): ")
        if question.lower() == "exit":
            print("Returning to Main Menu...\n")
            break

        a = input("Choice a: ")
        b = input("Choice b: ")
        c = input("Choice c: ")
        d = input("Choice d: ")

        correct = ""
        while correct.lower() not in ['a', 'b', 'c', 'd']:
            correct = input("Enter the correct answer between a/b/c/d: ").lower()
            if correct not in ['a', 'b', 'c', 'd']:
                print("Invalid input! Please choose in a, b, c, d, ^_^")

        question_data =  {
            "question": question,
            "difficulty": difficulty,
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "correct": correct
        }

#Calls the function which is expected to write the quiz into a file
        write_a_file(question_data)
        print("Question is saved!!")

def view_quiz(filename = 'quiz_questions_and_answers'):
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            content = file.read()
            if content.strip():
                print("\n=== SAVED QUIZ QUESTIONS ===")
                print(content)
            else:
                print("No questions here -_-")
    except FileNotFoundError:
        print("Quiz file not found")

def delete_questions(filename = 'quiz_questions_and_answers'):
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            questions = file.read().split("-"* 40 + "\n")

        questions = [q.strip() for q in questions if q.strip()]
        if not questions:
            print("No questions to delete here.")
            return

        print("\n=== Questions ===")
        for i, q in enumerate(questions, start = 1):
            print(f"{i}, {q.splitlines()[0]}")

        index = input("Enter the number of the question you want to delete: ")
        if index.lower() == 'cancel':
            print("Deleting cancelled")
            return

        index = int(index)
        if 1 <= index <= len(questions):
            del questions[index - 1]
            with open(filename, 'w', encoding = 'utf-8') as file:
                for q in questions:
                    file.write(q.strip() + "\n" + "-" * 40 + "\n")
                print("Question is now deleted!\n")
        else:
            print("Invalid question number.")
    except Exception as e:
        print("Error: ", e)

#Run the code
if __name__ == "__main__":
    main_menu()