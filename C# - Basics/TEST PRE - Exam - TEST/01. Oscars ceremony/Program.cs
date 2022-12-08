using System;

namespace _01._Oscars_ceremony
{
    class Program
    {
        static void Main(string[] args)
        {
            int RentPrice = int.Parse(Console.ReadLine());

            double statuesPrice = RentPrice * 1.0 - (RentPrice * 0.3);
            double catering = statuesPrice - (statuesPrice * 0.15);
            double soroundSound = catering * 0.5;

            double sumOfAll = RentPrice + statuesPrice + catering + soroundSound;

            Console.WriteLine($"{sumOfAll:f2}");
        }
    }
}
