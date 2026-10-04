
print("Hello Traveler!")
name = input("What's your name? ")
print("Hello, " + name + "!")
print("I've heard you come from far away. You should have learned lots of things on your way here.")
def ask_favor():
    while True:
        favor = input("I have a favor to ask of you. Would you help me? (yes/no) ").strip().lower()
        if favor == "yes":
            print("Thank you very much!")
            return
        elif favor == "no":
            print("Please would you reconsider, I really need your help.")
        else:
            print("Invalid response. Please answer with 'yes' or 'no'.")
ask_favor()
print("I need you to solve some riddles that my dad left for me before he died. I have tried to solve them myself but I have failed.")
print("I've been wondering what the meaning could be ever since, so I am really grateful for your help.")
print("So I've got this book. It has 25 entries, and I need to find out which one is the final riddle that needs to be deciphered. The others are tricks to confuse you. The tasks will give us numbers as prizes, and the final number will be the sum of all divided by 4, that number is the one we have to search for in the book. Ready?")

print("What task do you prefer to start with?")
print("1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Final answer")

while True:
    print("\nWhat task do you prefer to start with?")
    print("1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Final answer")
    task = input("Please choose a task (1-6): ")
    if task not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please select a number between 1 and 6.")
        continue  
    if task == "1":
        print("Task 1: I am a number that is the sum of the first five prime numbers. What number am I?")
        answer = input("Your answer: ")
        if answer == "28":
            print("Correct! The number is 28.")
        else:
            print("Incorrect. Do you want to try again? (yes/no)")
            if input().lower() == "yes":
                answer = input("Your answer: ")
                if answer == "28":
                    print("Correct! The number is 28.")
                else:
                    print("Incorrect. Try later.")

    if task == "2":
        print("Task 2: I am a number that is the product of the multiplication of the first two odd numbers . What number am I?")
        answer = input("Your answer: ")
        if answer == "3":
            print("Correct! The number is 3.")
        else:
            print("Incorrect. Do you want to try again? (yes/no)")
            retry = input()
            if retry.lower() == "yes":
                answer = input("Your answer: ")
                if answer == "3":
                    print("Correct! The number is 3.")
                else:
                    print("Incorrect. Try later.")

    if task == "3":
        print("Task 3: I am a number that is the difference between the square of 10 and the square of 8. What number am I?")
        answer = input("Your answer: ")
        if answer == "36":
            print("Correct! The number is 36.")
        else:
            print("Incorrect. Do you want to try again? (yes/no)")
            retry = input()
            if retry.lower() == "yes":
                answer = input("Your answer: ")
                if answer == "36":
                    print("Correct! The number is 36.")
                else:
                    print("Incorrect. Try later.")

    if task == "4":
        print("Task 4: Find a number in the following letters: heigt What number am I?")
        answer = input("Your answer: ")
        if answer == "8":
            print("Correct! The number is 8.")
        else:
            print("Incorrect. Do you want to try again? (yes/no)")
            retry = input()
            if retry.lower() == "yes":
                answer = input("Your answer: ")
                if answer == "8":
                    print("Correct! The number is 8.")
                else:
                    print("Incorrect. Try later.")

    if task == "5":
        print("Task 5: I am the number of the gravity on earth in m/s^2 (write only the number, without decimals). What number am I?")
        answer = input("Your answer: ")
        if answer == "9":
            print("Correct! The number is 9.")
        else:
            print("Incorrect. Do you want to try again? (yes/no)")
            retry = input()
            if retry.lower() == "yes":
                answer = input("Your answer: ")
                if answer == "9":
                    print("Correct! The number is 9.")
                else:
                    print("Incorrect. Try later.")

    if task == "6":
        print("Now that you have completed all the tasks, you can enter the final answer.")
        final_value = input("Please enter the final answer: ")
        if final_value == "21":
            print("Congratulations! You have solved the riddles and found the final answer.")
            print("You can now search for the final answer in the book.")
            break 
        else:
            print("Incorrect. You lost the game.")