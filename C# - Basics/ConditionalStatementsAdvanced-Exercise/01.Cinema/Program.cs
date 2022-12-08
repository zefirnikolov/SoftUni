using System;

namespace _01.Cinema
{
    class Program
    {
        static void Main(string[] args)
        {
            string cinemaType = Console.ReadLine();
            int rows = int.Parse(Console.ReadLine());
            int columns = int.Parse(Console.ReadLine());

            double income = 0;
            
            switch (cinemaType)
            {
                case "Premiere":
                    income = rows * columns * 12;
                    break;
                case "Normal":
                    income = rows * columns * 7.5;
                    break;
                case "Discount":
                    income = rows * columns * 5;
                    break;
                default:
                    Console.WriteLine("N/A");
                    break;
            }
            if (income > 0)
            {
                Console.WriteLine($"{income:f2} leva");
                Console.WriteLine("{0:f2} leva", income);
            }
            
        }
    }
}
