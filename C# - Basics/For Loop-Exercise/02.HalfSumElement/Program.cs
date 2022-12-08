using System;

namespace _02.HalfSumElement
{
    class Program
    {
        static void Main(string[] args)
        {
            //int numberOfLoops = int.Parse(Console.ReadLine());
            //int maxNumber = int.MinValue;
            //int minNumber = int.MaxValue;



            //for (int i = 0; i < numberOfLoops; i++)
            //{
            //    int currentNumber = int.Parse(Console.ReadLine());

            //    if (currentNumber > maxNumber)
            //    {
            //        maxNumber = currentNumber;
            //    }
            //    if (currentNumber < minNumber)
            //    {
            //        minNumber = currentNumber;
            //    }




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
            
            if (sumOfAll - maxNumber * 2 == 0)
            {
                Console.WriteLine($"Yes\r\nSum = {Math.Abs(sumOfAll - maxNumber)}");
            }
            else
            {
                Console.WriteLine($"No");
                Console.WriteLine($"Diff = {Math.Abs(maxNumber * 2 - sumOfAll)}");
            }
        }
    }
}
