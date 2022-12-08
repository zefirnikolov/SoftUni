using System;

namespace _05.Godzillavs.Kong
{
    class Program
    {
        static void Main(string[] args)
        {
            double budgetForTheMovie = double.Parse(Console.ReadLine());
            int countOfActors = int.Parse(Console.ReadLine());
            double priceForDressOf1Actor = double.Parse(Console.ReadLine());
           
            if (countOfActors > 150)
            {
                priceForDressOf1Actor = priceForDressOf1Actor - (priceForDressOf1Actor * 0.1);
            }

            double decorOfTheMovie = budgetForTheMovie * 0.1;
            double PriceForClothes = countOfActors * priceForDressOf1Actor;

            double allRequiredSumForTheMovie = decorOfTheMovie + PriceForClothes;

            double budgetCheck = allRequiredSumForTheMovie - budgetForTheMovie;

            if (budgetCheck > 0)
            {
                Console.WriteLine($"Not enough money!");
                Console.WriteLine($"Wingard needs {Math.Abs(budgetCheck):f2} leva more.");
            }
            else
            {
                Console.WriteLine($"Action!");
                Console.WriteLine($"Wingard starts filming with {Math.Abs(budgetCheck):f2} leva left.");
            }
        }
    }
}
