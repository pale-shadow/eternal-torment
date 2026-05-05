//
//  main.c
//
//  Created by @thedevilsvoice on 3/28/13.
//  Copyright (c) 2013 #fubaria. All rights reserved.
/*
    Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
*/

#include <stdio.h>
#include "../include/ayylmao.h"

int main(int argc, const char * argv[])
{
    int x = 1;
    for (x; x < 101; x++)
    {
        // is x a multiple of 3?
        if ((x % 3 == 0) && (x % 5 == 0))
            printf("AyyLmao\n");
        else if (x % 3 == 0)
            printf("Ayy\n");
        // is x a multiple of 5?
        else if (x % 5 == 0)
            printf("Lmao\n");
        else
            printf("%d\n",x);
    }
    return 0;
}
