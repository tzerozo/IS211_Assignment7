#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week7 (10/05/2020 - 10/11/2020)  "Game of Pig"
#Lang | 10/11/2020 |
#had to rewrite from beginning as somehow got errors of indentation

import random
import sys

class Dice:
    """Generates random number from 1 to 6."""
    def __init__(self):
        self.number = int()
        seed = 0

    def roll_dice(self):
        """To roll a dice."""
        self.number = random.randint(1,6)
        return self.number

class Player:
    """ Attributes and Behaviors of players."""
    def __init__(self):
        self.turn = False
        self.hold = False
        self.roll = True
        self.total_points = 0

    def choose(self):
        """Keep rolling or holding it."""
        question = input("Do you want to keep rolling or hold it?")
        if question == 'r':
            self.roll = True
            self.hold = False
        elif question == 'h':
            self.roll = False
            self.hold = True
        else:
            print("Please enter either 'r' or 'h'!")
            self.choose

class Game:
    """To play the game."""
    def __init__(self,player1,player2,dice):
        self.player1 = player1
        self.player2 = player2
        self.player1.name  = 'Gamer1'
        self.player2.name  = 'Gamer2'
        self.player1.score = 0
        self.player2.score = 0
        self.total_points = 0
        self.dice = dice

        ask = input("Do you wanna play first, enter y or n: ")
        if ask == 'y':
            self.currentplayer = player1
            print("Gamer1 will begin")
        elif ask == 'n':
            self.currentplayer = player2
            print("Gamer2 will begin")
        self.switch()

    def next_player(self):
        self.total_points = 0
        if self.player1.score >= 100:
            print("Gamer1 has won!!!")
            sys.exit()
        elif self.player2.score >= 100:
            print("Gamer2 has won!!!")
            sys.exit()
        else:
            if self.currentplayer == self.player1:
                self.currentplayer = self.player2
            elif self.currentplayer == self.player2:
                self.currentplayer = self.player1
        print(self.currentplayer.name, "Will take turn")
        self.switch()

    def switch(self):
        """Taking turn of rolling"""
        print("Gamer1's total_points: ", self.player1.score)
        print("Gamer2's total_points: ", self.player2.score)
        self.dice.roll_dice()
        if self.dice.number == 1:
            print("Sorry you rolled 1, we will forfeit your turn")
            self.total_points = 0
            self.next_player()
        else:
            self.total_points += self.dice.number
            print(self.dice.number," is rolled, you will earn the points")
            print("Your current score for this turn is ", self.total_points)
            self.currentplayer.choose()
            if self.currentplayer.hold == True and self.currentplayer.roll == False:
                self.currentplayer.score += self.total_points
                self.next_player()
            elif self.currentplayer.hold == False and self.currentplayer.roll == True:
                self.switch()
def main():
    """To start the program/game"""
    begin = input("Are you ready? Enter: y or n: ")
    if begin == 'y':
        player1 = Player()
        player2 = Player()
        dice = Dice()
        start = Game(player1,player2,dice)
    elif begin == 'n':
        print ("Cool,have a nice time!")
        sys.exit()
    else:
        print("You must enter 'y' or 'n'")
        main()

if __name__ == '__main__':
    main()
