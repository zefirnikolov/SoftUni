using System;

namespace _05.AccountBalance
{
    class Program
    {
        static void Main(string[] args)
        {

            

            string input = Console.ReadLine();

            double totalSum = 0;
            
            while (input != "NoMoreMoney")
            {
                double moneyIncrease = double.Parse(input); // Взимаме Input, не четем конзолата! Превръщаме Input в число и четем число!
                if (moneyIncrease < 0)
                {
                    Console.WriteLine($"Invalid operation!");
                    break;
                }
                               
                Console.WriteLine($"Increase: {moneyIncrease:f2}");
                totalSum += moneyIncrease;

                input = Console.ReadLine();
            }
            Console.WriteLine($"Total: {totalSum:f2}");
        }
    }
}
