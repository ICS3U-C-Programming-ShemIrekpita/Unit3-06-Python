#!/usr/bin/env python3
# Created by: Shem
# Created on: 10/26/2025
# This program is a number guessing game between 0 and 9
# It checks if the user entered an integer and tells them if they guessed correctly.
import random

def main():
# This generate a random number between 0 and 9
    correct_number = random.randint(0, 9)
# This ask's user to enter a number
    userInput = input("Guess a number between 0 and 9: ")
# This is the function to check for errors
    try:
# This is to check if they enterd a number or letter
        guess = int(userInput)
# Check if the guess is correct
        if guess == correct_number:
            print(userInput ,"is not an integer, You guessed the correct number:", correct_number)
        else:
            print("Wrong guess. The correct number was:", correct_number)
    except ValueError:
        print(userInput ,"is not an Number.")

if __name__ == "__main__":
    main()
