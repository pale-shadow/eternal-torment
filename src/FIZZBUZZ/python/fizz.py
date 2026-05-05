#!/usr/bin/python3

for num in range(1,101):
  # if modulo 3 & 5
  if (num % 3 == 0) and (num % 5 == 0):
    print ("fizzbuzz")
  # if multiple of 5 
  elif num % 5 == 0: 
    print ("buzz")
  # divisible by 3 and 5  
  elif (num % 3 == 0) :
    print ("fizz")
  # else print number
  else: 
    print ("Number: " + str(num))
