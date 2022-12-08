using System;

namespace _05.Journey
{
    class Program
    {
        static void Main(string[] args)
            //ДА РЕША ОТНОВО!


        {
            double budget = double.Parse(Console.ReadLine());
            string seasonWinterOrSummer = Console.ReadLine();

            string HotelOrCampTypeOfRest = string.Empty;
            string destination = string.Empty;
            double expenses = 0;

            if (budget <= 100)
            {
                destination = "Bulgaria";
                if (seasonWinterOrSummer == "summer")
                {
                    expenses = budget * 0.3;
                    HotelOrCampTypeOfRest = "Camp";
                }
                else if (seasonWinterOrSummer == "winter")
                {
                    expenses = budget * 0.7;
                    HotelOrCampTypeOfRest = "Hotel";
                }
            }
            else if (budget <= 1000)
            {
                destination = "Balkans";
                if (seasonWinterOrSummer == "summer")
                {
                    expenses = budget * 0.4;
                    HotelOrCampTypeOfRest = "Camp";
                }
                else if (seasonWinterOrSummer == "winter")
                {
                    expenses = budget * 0.8;
                    HotelOrCampTypeOfRest = "Hotel";
                }
            }
            else if (budget > 1000)
            {
                destination = "Europe";
                expenses = budget * 0.9;
                HotelOrCampTypeOfRest = "Hotel";
            }
            Console.WriteLine($"Somewhere in {destination}");
            Console.WriteLine($"{HotelOrCampTypeOfRest} - {expenses:f2}");

        }
    }
}
