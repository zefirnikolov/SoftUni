using System;

namespace _09._Yard_Greening
{
    class Program
    {
        static void Main(string[] args)
        {
            double squareMeters = double.Parse(Console.ReadLine());
            double pricePer1m2 = 7.61;
            double GrossPrice = squareMeters * pricePer1m2;
            double discount = 0.18;
            double discountedPrice = GrossPrice * discount;
            double finalPrice = GrossPrice - discountedPrice;
            Console.WriteLine($"The final price is: {finalPrice} lv.");
            Console.WriteLine($"The discount is: {discountedPrice} lv.");
        }
    }
}
