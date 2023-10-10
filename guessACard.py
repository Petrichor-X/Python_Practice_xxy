""" This file will be used in Project 3.
    NAME:Xiaoyu Xiao    
    DATE:09/26/2023
    Description of Project 3:
"""
import random
import sys


# Put any libararies to be imported below


def getSuit():
    # replace the following line with your implementation
    # put all the type of the card in the list, and randomly choice one of it.

    totalsuit = ["diamonds", "hearts", "clubs", "spades"]

    # print("the number is:", str(cardtype)) to show how many card in the selection

    # randomly choose a card in the list.
    getSuit = random.choice(totalsuit)

    # print it out to the user
    print("The suit that you get is: ", str(getSuit))


def getValue():
    # base on the question, the total cards values, and make them into list.
    totalvalue = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    # Select a random card value
    getValue = random.choice(totalvalue)

    # Print the selected value to the user
    print("The card value you got is:", getValue)


def printCard(getValue, getSuit):
    # Describe printCard here
    # replace the following line with your implementation
    printCard(getValue, getSuit)


def main():
    # Describe what the program will do here
    # replace the pass below with your implementation
    # suggestion: use this function to test getSuit, getValue and printCard
    # before implementing the main described in the Project 3 description
    print("This is the card that you get which is:" + str(printCard))


if __name__ == "__main__":
    main()
