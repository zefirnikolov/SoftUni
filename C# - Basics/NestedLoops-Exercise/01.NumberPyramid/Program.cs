using System;

namespace _01.NumberPyramid
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int currentNumber = 1;


            for (int rows = 1; rows <= n; rows++)
            {
                
                for (int columns = 1; columns <= rows; columns++)
                {
                    if (currentNumber > n)
                    {
                        return;
                    }
                    Console.Write($"{currentNumber} ");
                    currentNumber++;
                }

                Console.WriteLine();
            }
        }
    }
}
