using System;

namespace _05._Christmas_Gifts
{
    class Program
    {
        static void Main(string[] args)
        {
            string ageUntilChristmasEqStop = Console.ReadLine();

            int kidsCounter = 0;
            int priceFor1Toy = 5;
            int SumOfAllToys = 0;

            int adultCounter = 0;
            int priceFor1Sweater = 15;
            int SumOfAllSweaters = 0;

            while (ageUntilChristmasEqStop != "Christmas")
            {
                int ageParsed = int.Parse(ageUntilChristmasEqStop);
                if (ageParsed <= 16)
                {
                    kidsCounter++;

                }
                else
                {
                    adultCounter++;
                }
                ageUntilChristmasEqStop = Console.ReadLine();
            }
            SumOfAllToys = kidsCounter * priceFor1Toy;
            SumOfAllSweaters = adultCounter * priceFor1Sweater;


            Console.WriteLine($"Number of adults: {adultCounter}");
            Console.WriteLine($"Number of kids: {kidsCounter}");
            Console.WriteLine($"Money for toys: {SumOfAllToys}");
            Console.WriteLine($"Money for sweaters: {SumOfAllSweaters}");
        }
    }
}
