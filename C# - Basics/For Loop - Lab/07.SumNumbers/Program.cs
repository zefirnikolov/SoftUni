using System;

namespace _07.SumNumbers
{
    class Program
    {
        static void Main(string[] args)
        {

            //Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
            //• От първия ред на входа се въвежда броят числа n.
            //• От следващите n реда се въвежда по едно цяло число.
            //Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

            int numberOfLoops = int.Parse(Console.ReadLine());
            int totalSum = 0;
            
            
            for (int i = 0; i < numberOfLoops; i++)
            {
                int currentNumber = int.Parse(Console.ReadLine());
                totalSum += currentNumber;
            }
            Console.WriteLine(totalSum);

        }
    }
}
