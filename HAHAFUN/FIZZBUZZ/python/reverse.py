#!/usr/bin/python3

my_string = "Sample string"
stack = []

for i in my_string:
  #print (i)
  stack.append(i)

stack.reverse()
my_result = ''.join(stack)
print ("Result: " + my_result)
