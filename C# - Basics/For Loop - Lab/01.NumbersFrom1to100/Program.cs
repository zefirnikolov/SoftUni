using System;

namespace _01.NumbersFrom1to100
{
    class Program
    {
        static void Main(string[] args)
        {

            for (double i = 1.21; i <= 100; i += 1.5) // различно от Python - в Python i може да бъде само int!
            {
                Console.WriteLine($"{i:f2}");
            }
            for (int i = 0; i <= 100; i++) // различно от Python  - увелачавеме i  и излиза от цикъла, в Python не излиза а продължава до край!
            {
                i += 101;
                Console.WriteLine(i);
            }

        }
    }
}
