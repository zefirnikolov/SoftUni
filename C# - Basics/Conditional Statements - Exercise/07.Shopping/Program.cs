using System;

namespace _07.Shopping
{
    class Program
    {
        static void Main(string[] args)
        {
            double budgetOfPetur = double.Parse(Console.ReadLine());
            int numberOfGraphicCards = int.Parse(Console.ReadLine());
            int numberOfCPUs = int.Parse(Console.ReadLine());
            int numberOfRAMChips = int.Parse(Console.ReadLine());

            double graphicCardPrice = 250;
            double cPUPrice = graphicCardPrice * numberOfGraphicCards * 0.35;
            double rAMChipPrice = graphicCardPrice * numberOfGraphicCards * 0.1;


            double priceOfAllComonents = (numberOfGraphicCards * graphicCardPrice) + (cPUPrice * numberOfCPUs) + (rAMChipPrice * numberOfRAMChips);

            if (numberOfGraphicCards > numberOfCPUs)
            {
                priceOfAllComonents = priceOfAllComonents - (priceOfAllComonents * 0.15);
            }

            bool isTheBudgetEnough = priceOfAllComonents <= budgetOfPetur;

            if (isTheBudgetEnough)
            {
                Console.WriteLine($"You have {(budgetOfPetur - priceOfAllComonents):f2} leva left!"); 
            }
            else
            {
                Console.WriteLine($"Not enough money! You need {Math.Abs(budgetOfPetur - priceOfAllComonents):f2} leva more!");
            }        
        }
    }
}
