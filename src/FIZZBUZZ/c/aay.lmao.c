#include <stdio.h>

#define AYY 0
#define LMAO 1
#define ayy_lmao(format, ...) fprintf (stderr, format, __VA_ARGS__)

void main()
{
   int turnt = 8;
   // muffled ayy lmao from @da_667 in the distance
   ayy_lmao("all lit up    : %d===>~~ \n", turnt );
}
