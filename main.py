# import the datetime module
import datetime
# import the random module
import random


# Create a function called menu that prints the following menu:
# 1. Guess a number
# 2. Show date and time
# 3. Exit
def menu():
    print("1. Guess a number")
    print("2. Show date and time")
    print("3. Exit")


# Create a function called guess_a_number
def guess_a_number():
    # Create a list of 100 numbers
    numbers = list(range(1, 101))
    # Ask the user to enter a number between 1 and 100
    user_number = int(input("Enter a number between 1 and 100: "))
    # randomly pick a number from the list
    random_number = random.choice(numbers)
    # compare the user's number to the random number
    # if the user's number is the same as the random number, print "You guessed the number!"
    if user_number == random_number:
        print("You guessed the number!")
    # if the user's number is higher than the random number, print "You guessed too high!"
    elif user_number > random_number:
        print("You guessed too high!")
    # if the user's number is lower than the random number, print "You guessed too low!"
    elif user_number < random_number:
        print("You guessed too low!")
    # print the random number
    print("Actual number: " + str(random_number))
    # print the user's number
    print("Your number: " + str(user_number))


# Create a function called show_date_and_time
def show_date_and_time():
    # print the current date and time
    print(datetime.datetime.now())


if __name__ == '__main__':
    # Create a while loop that runs until the user enters 3
    while True:
        # Call the menu function
        menu()
        # Ask the user to enter a number
        user_input = int(input("Enter a number: "))
        # if the user enters 1, call the guess_a_number function
        if user_input == 1:
            guess_a_number()
        # if the user enters 2, exit the program
        elif user_input == 2:
            show_date_and_time()
        # if the user enters 3, exit the program
        elif user_input == 3:
            break
        # if the user enters anything else, print "Invalid input"
        else:
            print("Invalid input")
