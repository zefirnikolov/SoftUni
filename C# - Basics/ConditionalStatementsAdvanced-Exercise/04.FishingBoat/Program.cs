using System;

namespace _04.FishingBoat
{
    class Program
    {
        static void Main(string[] args)
        {
            // "Spring", "Summer", "Autumn", "Winter
            double budget = double.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            int fishermen = int.Parse(Console.ReadLine());

            double priceForRentOfTheShip = 0;

            switch (season)
            {
                case "Spring":
                    priceForRentOfTheShip = 3000;
                    break;
                case "Summer":
                    priceForRentOfTheShip = 4200;
                    break;
                case "Autumn":
                    priceForRentOfTheShip = 4200;
                    break;
                case "Winter":
                    priceForRentOfTheShip = 2600;
                    break;
            }

            if (fishermen >= 0 && fishermen <= 6)
            {
                priceForRentOfTheShip = priceForRentOfTheShip - (priceForRentOfTheShip * 0.1);
            }
            else if (fishermen > 6 && fishermen <= 11)
            {
                priceForRentOfTheShip = priceForRentOfTheShip - (priceForRentOfTheShip * 0.15);
            }
            else if (fishermen > 11)
            {
                priceForRentOfTheShip = priceForRentOfTheShip - (priceForRentOfTheShip * 0.25);
            }
            
            if (season != "Autumn" && fishermen % 2 == 0)
            {
                priceForRentOfTheShip = priceForRentOfTheShip - (priceForRentOfTheShip * 0.05);
            }

            double difference = Math.Abs(budget - priceForRentOfTheShip);
            
            bool isTheBudgetEnough = budget >= priceForRentOfTheShip;

            if (isTheBudgetEnough)
            {
                Console.WriteLine($"Yes! You have {difference:f2} leva left."); 
            }
            else
            {
                Console.WriteLine($"Not enough money! You need {difference:f2} leva.");
            }
        }
    }
}
