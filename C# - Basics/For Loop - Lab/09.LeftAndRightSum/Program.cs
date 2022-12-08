using System;

namespace _09.LeftAndRightSum
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfLoops = int.Parse(Console.ReadLine());
            int totalSum1 = 0;
            int totalSum2 = 0;



            for (int i = 0; i < numberOfLoops; i++)
            {
                int currentNumber1 = int.Parse(Console.ReadLine());
                totalSum1 += currentNumber1;
            }
            

            for (int i = 0; i < numberOfLoops; i++)
            {
                int currentNumber2 = int.Parse(Console.ReadLine());
                totalSum2 += currentNumber2;
            }
            
            if (totalSum1 == totalSum2)
            {
                Console.WriteLine($"Yes, sum = {totalSum1}");
            }
            else
            {
                Console.WriteLine($"No, diff = {Math.Abs(totalSum1 - totalSum2)}");
            }
        }
    }
}
