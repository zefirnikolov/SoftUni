using System;

namespace _02._Beer_And_Chips
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            double budget = double.Parse(Console.ReadLine());
            int numberOfBeers = int.Parse(Console.ReadLine());
            int numberOfChips = int.Parse(Console.ReadLine());

            double priceOf1Beer = 1.2;

            double sumForBeers = numberOfBeers * priceOf1Beer;

            double priceFor1Chips = sumForBeers * 0.45;

            double sumForChips = Math.Ceiling(priceFor1Chips * numberOfChips);

            double sumForAll = sumForBeers + sumForChips;

            if (sumForAll <= budget)
            {
                Console.WriteLine($"{name} bought a snack and has {(budget - sumForAll):f2} leva left.");
            }
            else
            {
                Console.WriteLine($"{name} needs {(sumForAll - budget):f2} more leva!");
            }
        }
    }
}
