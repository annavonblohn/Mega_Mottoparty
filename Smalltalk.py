import random

def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_choice = input("Enter the number of your choice: ")

    try:
        user_choice = int(user_choice)
        if 1 <= user_choice <= len(options):
            return options[user_choice - 1]
        else:
            return "Invalid choice. Please enter a valid number."
    except ValueError:
        return "Invalid input. Please enter a number."

def main():
    greeting = "Hello! I'm your mini chatbot. Let's have a quick chat."

    question1 = "What is your favorite color?"
    options1 = ["Blue", "Red", "Green", "Yellow"]

    question2 = "If you could travel anywhere, where would you go?"
    options2 = ["Berlin", "Leipzig", "Kaiserslautern", "Münster"]

    question3 = "What is your favorite programming language?"
    options3 = ["Python", "JavaScript", "Java", "C++"]

    print(greeting)

    answer1 = ask_question(question1, options1)
    print(f"Great choice! {answer1} is a fantastic color.")

    answer2 = ask_question(question2, options2)
    print(f"Nice! I would love to visit {answer2} too.")

    answer3 = ask_question(question3, options3)
    print(f"Awesome! {answer3} is a powerful language.")

    print("Thanks for chatting with me!")

if __name__ == "__main__":
    main()
