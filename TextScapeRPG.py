# Base game file
# version 1.1

import sys
import time
import os

# Functions
def actionPrompt():
   print("What would you like to do?")
   print("Enter 'help' for more options.")
   action=input("Action: ")
   if (action in actionList):
       print "Evans"

def fight():
   print "You are now fighting."
#

# Actions
actionList = ["fight", "fish", "cook", "heal"]
#

#    Variables
# User skills
attack = 1
strength = 1
defence = 1
health = 1
fishing = 1
cooking = 1

#
#

# Run program
actionPrompt()
