using System;

namespace _01.NumberPyramid3
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int numberPrinter = 1;


            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    if (numberPrinter > n)
                    {
                        return;
                    }
                    Console.Write($"{numberPrinter} ");
                    numberPrinter++;
                }
                Console.WriteLine();
            }
        }
    }
}
