using System;

namespace _07.HotelRoom
{
    class Program
    {
        static void Main(string[] args)
        {
            string month = Console.ReadLine();
            int numberOfOvernightStays = int.Parse(Console.ReadLine());

            
            double priceForStudio1Night = 0;
            double priceForApartmanent1Night = 0;

            switch (month)
            {
                case "May":
                case "October":
                    priceForApartmanent1Night = 65;
                    priceForStudio1Night = 50;
                    if (numberOfOvernightStays > 7 && numberOfOvernightStays <= 14)
                    {
                        priceForStudio1Night = priceForStudio1Night - (priceForStudio1Night * 0.05);
                    }
                    else if (numberOfOvernightStays > 14)
                    {
                        priceForStudio1Night = priceForStudio1Night - (priceForStudio1Night * 0.3);
                        priceForApartmanent1Night = priceForApartmanent1Night - (priceForApartmanent1Night * 0.1);
                    }
                    break;
                case "June":
                case "September":
                    priceForApartmanent1Night = 68.7;
                    priceForStudio1Night = 75.2;
                    if (numberOfOvernightStays > 14)
                    {
                        priceForStudio1Night = priceForStudio1Night - (priceForStudio1Night * 0.2);
                        priceForApartmanent1Night = priceForApartmanent1Night - (priceForApartmanent1Night * 0.1);
                    }
                    break;
                case "July":
                case "August":
                    priceForApartmanent1Night = 77;
                    priceForStudio1Night = 76;
                    if (numberOfOvernightStays > 14)
                    {
                        priceForApartmanent1Night = priceForApartmanent1Night - priceForApartmanent1Night * 0.1;
                    }
                    break;

            }
            double finalpriceForStudio = priceForStudio1Night * numberOfOvernightStays;
            double finalPriceForApartment = priceForApartmanent1Night * numberOfOvernightStays;

            Console.WriteLine($"Apartment: {finalPriceForApartment:f2} lv.");
            Console.WriteLine($"Studio: {finalpriceForStudio:f2} lv.");




        }
    }
}
