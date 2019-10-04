#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:50:17 2019

@author: mallika
"""
#Hangman

from os import system, name
from time import sleep

def clrscr():
    if (name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')

flag = 0

clrscr()
sleep(2)

print("\n\n\n\n\n")
print("HANGMAN".center(60))

sleep(2)
clrscr()


word = list("HELLO")
display = list("-----")
tries = 7
guess = ' '

def check(wrd, disp):
    flg=1
    for x in range (5):
        if wrd[x]!=disp[x]:
            flg=0
    return flg

def compare(wrd,disp,gu):
    flg=0
    for x in range (5):
        if word[x] == guess:
            display[x] = guess
            flg = 1
    return flg
    
def view(disp,tri):
    print("TRIES LEFT:",tri)
    print("\n\t\t",display)
    
    
#game start
#print(display)
while (flag != 3 and tries!=0):
    flag = 0
    view(display,tries)
    guess = input("GUESS:")
    guess = guess.upper()
    if (compare(word,display,guess)):
        flag = 1
    if flag == 0:
        tries-=1
    if (check(word,display)):
        flag=3
    clrscr()
print("\n\t\t",display)
sleep(2)
print("DONE".center(60,'-'))