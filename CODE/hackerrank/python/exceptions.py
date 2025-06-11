"""
Task

You are given two values a and b.
Perform integer division and print .

Input Format

The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.

Constraints

0 < T < 10

Output Format

Print the value of a/b.

In the case of ZeroDivisionError or ValueError, print the error code.
"""
import sys

if __name__ == '__main__':
    #Read input from STDIN. Print output to STDOUT

    T = []

    while True:
        line = input()
        if line:
            T.append(line)
        else:
            break

    counter = 0
    line_count = int(T[counter])
    """
    if line_count in range(1,10):
        print("line count is: ", line_count)
    else:
        sys.exit(0)
    """
    result = int()
    
    counter = counter + 1
    while counter < len(T):
        xy = T[counter].split(' ')
        counter = counter + 1
        try:
            a = int(xy[0])
            b = int(xy[1])
            result = a/b
            print(str(result))
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
