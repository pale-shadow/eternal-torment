using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AyyLmao
{
    class Program
    {
        static void Main(string[] args)
        {

            for (int x = 1; x < 101; x++)
            {
                // is x a multiple of 3?
                if ((x % 3 == 0) && (x % 5 == 0))
                    Console.Write("AyyLmao\n");
                else if (x % 3 == 0)
                    Console.Write("Ayy\n");
                // is x a multiple of 5?
                else if (x % 5 == 0)
                    Console.Write("Lmao\n");
                else
                    String.Format("{0}\n",x);
            }
            Console.ReadKey();
    
        }
    }
}
