using System;

namespace _03.SumNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int mainNumber = int.Parse(Console.ReadLine());

            int sum = 0;

            while (mainNumber > sum)
            {
                int newNumber = int.Parse(Console.ReadLine());

                sum += newNumber;

            }
            
            Console.WriteLine(sum);

        }
    }
}
