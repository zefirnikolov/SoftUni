using System;

namespace _03._Excursion_Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            //                 Пролет(spring)    Лято(summer)      Есен(autumn)      Зима(winter)
            //До 5 човека      50.00 лв.на човек 48.50 лв.на човек 60.00 лв.на човек 86.00 лв.на човек
            //Над 5 човека     48.00 лв.на човек 45.00 лв.на човек 49.50 лв.на човек 85.00 лв.на човек

            // При "summer"-> 15 % отстъпка
            // При "winter"-> 8 % оскъпяван


            int peopleCount = int.Parse(Console.ReadLine());
            string season = Console.ReadLine();

            double price = 0;

            switch (season)
            {
                case "spring":
                    if (peopleCount <= 5)
                    {
                        price = peopleCount * 50;
                    }
                    else
                    {
                        price = peopleCount * 48;
                    }
                    break;
                case "summer":
                    if (peopleCount <= 5)
                    {
                        price = peopleCount * 48.5;
                        price = price - price * 0.15;
                    }
                    else
                    {
                        price = peopleCount * 45;
                        price = price - price * 0.15;

                    }
                    break;
                case "autumn":
                    if (peopleCount <= 5)
                    {
                        price = peopleCount * 60;
                    }
                    else
                    {
                        price = peopleCount * 49.5;
                    }
                    break;
                case "winter":
                    if (peopleCount <= 5)
                    {
                        price = peopleCount * 86;
                        price = price + price * 0.08;
                    }
                    else
                    {
                        price = peopleCount * 85;
                        price = price + price * 0.08;

                    }
                    break;

            }
            Console.WriteLine($"{price:f2} leva.");
        }
    }
}
