using System;

namespace _08.BasketballEquipment
{
    class Program
    {
        static void Main(string[] args)
        {
            
            //• Баскетболни кецове – цената им е 40 % по - малка от таксата за една година
            //• Баскетболен екип – цената му е 20 % по - евтина от тази на кецовете
            //• Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
            //• Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка


            int YearlyTax = int.Parse(Console.ReadLine());

            double runningShoesPrice = YearlyTax - (YearlyTax * 40 / 100);
            double sportOutfitPrice = runningShoesPrice - (runningShoesPrice * 0.2);
            double basketBallPrice = sportOutfitPrice * 0.25;
            double accesoriesPrice = basketBallPrice * 0.2;

            double allExpenses = YearlyTax + runningShoesPrice + sportOutfitPrice + basketBallPrice + accesoriesPrice;

            Console.WriteLine(allExpenses);


        }
    }
}
