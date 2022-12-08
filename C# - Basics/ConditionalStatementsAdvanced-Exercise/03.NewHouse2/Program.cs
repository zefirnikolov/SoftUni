using System;

namespace _03.NewHouse2
{
    class Program
    {
        static void Main(string[] args)
        {

            //"Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
            string flower = Console.ReadLine();
            int numberOfFlowers = int.Parse(Console.ReadLine());
            int budget = int.Parse(Console.ReadLine());

            double price = 0;

            switch (flower)
            {
                case "Roses":
                    price = 5;
                    break;
                case "Dahlias":
                    price = 3.8;
                    break;
                case "Tulips":
                    price = 2.8;
                    break;
                case "Narcissus":
                    price = 3;
                    break;
                case "Gladiolus":
                    price = 2.5;
                    break;
            }

            double finalPrice = numberOfFlowers * price;

            if (flower == "Roses" && numberOfFlowers > 80)
            {
                finalPrice = finalPrice - (finalPrice * 0.1);
            }
            else if (flower == "Dahlias" && numberOfFlowers > 90)
            {
                finalPrice = finalPrice - (finalPrice * 0.15);
            }
            else if (flower == "Tulips" && numberOfFlowers > 80)
            {
                finalPrice = finalPrice - (finalPrice * 0.15);
            }
            else if (flower == "Narcissus" && numberOfFlowers < 120)
            {
                finalPrice = finalPrice + (finalPrice * 0.15);
            }
            else if (flower == "Gladiolus" && numberOfFlowers < 80)
            {
                finalPrice = finalPrice + (finalPrice * 0.20);
            }

            double difference = Math.Abs(finalPrice - budget);

            bool isTheBudgetEnough = budget >= finalPrice;

            if (isTheBudgetEnough)
            {
                Console.WriteLine($"Hey, you have a great garden with {numberOfFlowers} {flower} and {(difference):f2} leva left.");
            }
            else
            {
                Console.WriteLine($"Not enough money, you need {difference:f2} leva more.");
            }
        }
    }
}
