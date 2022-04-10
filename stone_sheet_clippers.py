#!/usr/bin/env python3

# stone_sheet_clippers.py
# A shitty clone of Rock Paper Scissors in Python
# Copyright (C) 2022 Gutsy Millie

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from os import system
from random import choice
from platform import system as sys_os

# Checks if the logo text file exists, if not the game will just display "Stone Sheet Clippers"
try:
    logo_file = open("logo.txt", "r")
    logo_text = logo_file.read()
except:
    pass

values = ("s", "h", "c")

# Creates a function to tell the player the result
def check():
    if usr_input == com_input:
        print("Draw !")
    if usr_input == "s" and com_input == "h":
        print("Stone vs Sheet : You lost !")
    if usr_input == "s" and com_input == "c":
        print("Stone vs Clippers : You won !")
    if usr_input == "h" and com_input == "s":
        print("Sheet vs Stone : You won !")
    if usr_input == "h" and com_input == "c":
        print("Sheet vs Clippers : You lost !")
    if usr_input == "c" and com_input == "s":
        print("Clippers vs Stone : You lost !")
    if usr_input == "c" and com_input == "h":
        print("Clippers vs Sheet : You won !")

# Creates a function to properly clean the screen
def clear_screen():
    if sys_os() == "Linux" or sys_os() == "Darwin":
        system("clear")
    else:
        system("cls")

# Main loop
try:
    while True:
        clear_screen()
        usr_input = ""
        com_input = ""
        try:
            print(logo_text)
        except:
            print("Stone Sheet Clippers")
        print("")

        while bool(usr_input) == False and not usr_input in values:
            usr_input = input("Stone (s), Sheet (h), Clippers (c) ! (Use Ctrl-C to quit) ").lower().strip()
            com_input = choice(values)

        check()

        input("Press Enter to play again... ")

# A better way to stop the game
except KeyboardInterrupt:
    print("")
    print("Bye !")
