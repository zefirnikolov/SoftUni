using System;

namespace _07.FoodDelivery
{
    class Program
    {
        static void Main(string[] args)
        {
            // Примерен вход и изход
            //2
            //4
            //3
            //116.2

            //Пилешко меню – 10.35 лв.
            //• Меню с риба – 12.40 лв.
            //• Вегетарианско меню – 8.15 лв.

            //• Брой пилешки менюта – цяло число в интервала[0... 99]
            //• Брой менюта с риба – цяло число в интервала[0... 99]
            //• Брой вегетариански менюта – цяло число в интервала[0... 99]

            //Десерт с цена 20% от общата сметка
            //Доставка = 2.50 lv.

          
            double priceForChickenMenu = 10.35;
            double priceForFishMenu = 12.40;
            double priceForVegMenu = 8.15;
            double priceForDelivery = 2.50;


            int numberOfChickenMenus = int.Parse(Console.ReadLine());
            int numberOfFishMenus = int.Parse(Console.ReadLine());
            int numberOfVegMenus = int.Parse(Console.ReadLine());

            double sumOfMenusWithoutDesert = (numberOfChickenMenus * priceForChickenMenu) + (numberOfFishMenus * priceForFishMenu) + (numberOfVegMenus * priceForVegMenu);
            double priceForDesert = sumOfMenusWithoutDesert * 0.2;

            double sumOfAll = priceForDesert + sumOfMenusWithoutDesert + priceForDelivery;

            Console.WriteLine($"{sumOfAll}");

        }
    }
}
