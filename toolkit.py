# Personal Mini-Toolkit
# PLP Week 8 Final Project
# This program provides a calculator, a to-do list, and a number guessing game.


def get_number(prompt):
    """Ask for a number until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# Tool 1: Perform basic arithmetic on two numbers.
def calculator():
    print("\n========== SIMPLE CALCULATOR ==========")
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter your choice (1-4): ").strip()

    if operation == "1":
        answer = first_number + second_number
    elif operation == "2":
        answer = first_number - second_number
    elif operation == "3":
        answer = first_number * second_number
    elif operation == "4":
        if second_number == 0:
            print("Sorry, you cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print(f"Sorry, '{operation}' is not a valid operation.")
        return

    print(f"The answer is: {answer}")


# Tool 2: Add, view, and remove tasks stored in a changing list.
def todo_manager(tasks):
    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        task_choice = input("Choose an option (1-4): ").strip()

        if task_choice == "1":
            new_task = input("Enter your new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully!")
            else:
                print("A task cannot be empty.")

        elif task_choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif task_choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = input("Enter the task number to remove: ").strip()
                if task_number.isdigit():
                    task_number = int(task_number)
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed!")
                    else:
                        print("That task number does not exist.")
                else:
                    print("Please enter a valid whole number.")

        elif task_choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")


# Tool 3: Give the user hints until they guess the secret number.
def guessing_game():
    print("\n========== NUMBER GUESSING GAME ==========")
    secret_number = 7
    attempts = 0
    print("I have selected a number between 1 and 10.")

    while True:
        guess_text = input("Enter your guess: ").strip()

        if not guess_text.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_text)
        if not 1 <= guess <= 10:
            print("Please choose a number between 1 and 10.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number}!")
            print(f"You got it in {attempts} attempts.")
            break


# Main program: keep showing the menu until the user chooses Quit.
def main():
    tasks = []

    print("====================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("====================================")
    print("\nWelcome to your Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_manager(tasks)
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("\nThank you for using the Personal Mini-Toolkit!")
            print("Goodbye!")
            break
        else:
            print(f"\nSorry, '{choice}' is not a valid choice.")
            print("Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
