"""
OUTPUT_PATH=./franklin python3 ./capitalize.py
"""
import os

def solve(s):
    """[summary]

    Split line s on whitespace
    Validate first character of each word is [a-z]

    Figure out the time/space complexity of this function

    Args:
        s ([type]): [description]
    """
    result = str()

    words = s.split(' ')

    for word in words:
        x = word[0:1] # first cahr

        if x.islower():
            x = x.upper()
            new_word = x + word[1:]
        else:
            new_word = word
        result = result + new_word + ' '
        
        print (result)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') # prepend the execution with setting OUTPUT_PATH

    s = input()

    result = solve(s)
    
    fptr.write(result + '\n')

    fptr.close()

"""Hacker Rank - Capitalize
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name.

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""
