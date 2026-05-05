//
//  main.c
//  fizzbuzz
//
//  Created by fediaz on 3/28/13.
//  Copyright (c) 2013 #fubaria. All rights reserved.
/*
    Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
*/

#include <stdio.h>

int main(int argc, const char * argv[])
{

    for (int x = 1; x < 101; x++)
    {
        // is x a multiple of 3?
        if ((x % 3 == 0) && (x % 5 == 0))
            printf("FizzBuzz\n");
        else if (x % 3 == 0)
            printf("Fizz\n");
        // is x a multiple of 5?
        else if (x % 5 == 0)
            printf("Buzz\n");
        else
            printf("%d\n",x);
    }
    
    //printf("Hello, World!\n");
    return 0;
}

