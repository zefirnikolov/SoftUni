using System;

namespace _04.ToyShop
{
    class Program
    {
        static void Main(string[] args)
        {
            //            Цени на играчките:
            //• Пъзел - 2.60 лв.
            //• Говореща кукла -3 лв.
            //• Плюшено мече -4.10 лв.
            //• Миньон - 8.20 лв.
            //• Камионче - 2 лв.



            double puzzle = 2.60;
            double speakingDoll = 3;
            double teddyBear = 4.1;
            double minion = 8.20;
            double toyTruck = 2;

            double PriceOfTheExcursion = double.Parse(Console.ReadLine());
            int numberOfPuzzles = int.Parse(Console.ReadLine());
            int numberOfSpeakingDolls = int.Parse(Console.ReadLine());
            int numberOfTeddyBears = int.Parse(Console.ReadLine());
            int numberOfminions = int.Parse(Console.ReadLine());
            int numberOfToyTrucks = int.Parse(Console.ReadLine());

            double priceOfAllToys = (numberOfPuzzles * puzzle) + (numberOfSpeakingDolls * speakingDoll) + (numberOfTeddyBears * teddyBear) + (numberOfminions * minion) + (numberOfToyTrucks * toyTruck);
            int countOfAllToys = numberOfPuzzles + numberOfSpeakingDolls + numberOfTeddyBears + numberOfminions + numberOfToyTrucks;

            if (countOfAllToys >= 50)
            {
                priceOfAllToys = priceOfAllToys - (priceOfAllToys * 0.25);
            }

            double rent = priceOfAllToys * 10 / 100;

            double profit = priceOfAllToys - rent;

            double excursionCheck = profit - PriceOfTheExcursion; 

            if (excursionCheck >= 0)
            {
                Console.WriteLine($"Yes! {excursionCheck:f2} lv left.");
            }
            else
            {
                Console.WriteLine($"Not enough money! {Math.Abs(excursionCheck):f2} lv needed.");
            }
        }
    }
}
