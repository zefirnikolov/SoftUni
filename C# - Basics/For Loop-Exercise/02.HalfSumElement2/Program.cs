using System;

namespace _02.HalfSumElement2
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfLoops = int.Parse(Console.ReadLine());
            int maxNumber = int.MinValue;
            int sumOfAll = 0;



            for (int i = 0; i < numberOfLoops; i++)
            {
                int numberFromTheConsole = int.Parse(Console.ReadLine());

                sumOfAll += numberFromTheConsole;
                if (numberFromTheConsole > maxNumber)
                {
                    maxNumber = numberFromTheConsole;
                }
            }
            int sumOfTheNumbersWithoutMaxNumber = sumOfAll - maxNumber;
            if (sumOfTheNumbersWithoutMaxNumber == maxNumber)
            {
                Console.WriteLine("Yes");
                Console.WriteLine($"Sum = " + maxNumber);
            }
            else
            {
                Console.WriteLine("No");
                Console.WriteLine($"Diff = " + Math.Abs(maxNumber - sumOfTheNumbersWithoutMaxNumber));
            }
        }
    }
}
