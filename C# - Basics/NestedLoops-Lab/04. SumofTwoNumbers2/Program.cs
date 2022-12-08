using System;

namespace _04._SumofTwoNumbers2
{
    class Program
    {
        static void Main(string[] args)
        {
            int startNumber = int.Parse(Console.ReadLine());
            int lastNumber = int.Parse(Console.ReadLine());
            int magicNumber = int.Parse(Console.ReadLine());

            int counter = 0;
            bool isMagicNumber = false;

            for (int firstNumber = startNumber; firstNumber <= lastNumber; firstNumber++)
            {
                for (int secondNumber = startNumber; secondNumber <= lastNumber; secondNumber++)
                {
                    counter++;

                    if (firstNumber + secondNumber == magicNumber)
                    {
                        isMagicNumber = true;
                        Console.WriteLine($"Combination N:{counter} ({firstNumber} + {secondNumber} = {magicNumber})");
                        break;
                    }
                }
                if (isMagicNumber)
                {
                    break;
                }
            }
            if (!isMagicNumber)
            {
                Console.WriteLine($"{counter} combinations - neither equals {magicNumber}");
            }
        }
    }
}
