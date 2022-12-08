using System;

namespace _04.SumofTwoNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int startNumber = int.Parse(Console.ReadLine());
            int lastNumber = int.Parse(Console.ReadLine());
            int magicNumber = int.Parse(Console.ReadLine());

            int counter = 0;
            
            for (int firstNumber = startNumber; firstNumber <= lastNumber; firstNumber++)
            {
                for (int secondNumber = startNumber; secondNumber <= lastNumber; secondNumber++)
                {
                    counter++;

                    if (firstNumber + secondNumber == magicNumber)
                    {                        
                        Console.WriteLine($"Combination N:{counter} ({firstNumber} + {secondNumber} = {magicNumber})");
                        return;                                             
                    }
                }
            }
            Console.WriteLine($"{counter} combinations - neither equals {magicNumber}");
        }
    }
}
