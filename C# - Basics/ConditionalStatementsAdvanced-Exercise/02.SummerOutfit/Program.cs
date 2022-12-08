using System;

namespace _02.SummerOutfit
{
    class Program
    {
        static void Main(string[] args)
        {
            
            




            int degrees = int.Parse(Console.ReadLine());
            string timeOfDay = Console.ReadLine();

            string outfit = string.Empty;
            string shoes = "";

            // Може да бъде направено и с If (degrees), if else (degrees) if else (degrees) и след това да бъде вкаран switch 
            // switch вътре в IF statement-a - отново се решава - редове по колони. Тук е 3 по 3 така е същото,
            // Но виждам че го решават редове по колони, а не колони по редове.

            switch (timeOfDay)
            {
                case "Morning":
                    if (10 <= degrees && degrees <= 18)
                    {
                        outfit = "Sweatshirt";
                        shoes = "Sneakers";
                    }
                    else if (18 < degrees && degrees <= 24)
                    {
                        outfit = "Shirt";
                        shoes = "Moccasins";
                    }
                    else if (degrees >= 25)
                    {
                        outfit = "T-Shirt";
                        shoes = "Sandals";
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "Afternoon":
                    if (10 <= degrees && degrees <= 18)
                    {
                        outfit = "Shirt";
                        shoes = "Moccasins";
                    }
                    else if (18 < degrees && degrees <= 24)
                    {
                        outfit = "T-Shirt";
                        shoes = "Sandals";
                    }
                    else if (degrees >= 25)
                    {
                        outfit = "Swim Suit";
                        shoes = "Barefoot";
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "Evening":
                    if (10 <= degrees && degrees <= 18)
                    {
                        outfit = "Shirt";
                        shoes = "Moccasins";
                    }
                    else if (18 < degrees && degrees <= 24)
                    {
                        outfit = "Shirt";
                        shoes = "Moccasins";
                    }
                    else if (degrees >= 25)
                    {
                        outfit = "Shirt";
                        shoes = "Moccasins";
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                default:
                    Console.WriteLine("N/A");
                    break;
            }
            Console.WriteLine($"It's {degrees} degrees, get your {outfit} and {shoes}.");

        }
    }
}
