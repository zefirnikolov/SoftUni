using System;

namespace _03.SumPrimeNonPrime
{
    class Program
    {
        static void Main(string[] args)
        {

            string numToString = Console.ReadLine();

            int sumPrimeNumbers = 0;
            int sumNonPrimeNumbers = 0;

            while (numToString != "stop")
            {
                int num = int.Parse(numToString);
                int prime = 0;

                if (num < 0)
                {
                    
                    Console.WriteLine($"Number is negative.");
                    numToString = Console.ReadLine();
                    continue;
                }
                for (int i = 1; i <= num; i++)
                {
                    if (num % i == 0)
                    {
                        prime++;
                    }
                }
                if (prime == 2)
                {
                    sumPrimeNumbers += num;
                }
                else
                {
                    sumNonPrimeNumbers += num;
                }
                numToString = Console.ReadLine();
            }
            Console.WriteLine($"Sum of all prime numbers is: {sumPrimeNumbers}");
            Console.WriteLine($"Sum of all non prime numbers is: {sumNonPrimeNumbers}");
        }
    }
}
