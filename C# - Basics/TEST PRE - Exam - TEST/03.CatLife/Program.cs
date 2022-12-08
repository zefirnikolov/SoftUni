using System;

namespace _03.CatLife
{
    class Program
    {
        static void Main(string[] args)
        {
            //Порода British Shorthair | Siamese    | Persian    | Ragdoll | American Shorthair | Siberian
            //Мъжки пол(m)    13 години   15 години  14 години    16 години      12 години         11 години
            //Женски пол (f) 14 години     16 години  15 години    17 години      13 години         12 години

            string breed = Console.ReadLine();
            string genderOfTheCat = Console.ReadLine();


            double monthsOfTheCat = 0;



            switch (breed)
            {
                case "British Shorthair":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 13 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 14 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                case "Siamese":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 15 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 16 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                case "Persian":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 14 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 15 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                case "Ragdoll":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 16 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 17 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                case "American Shorthair":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 12 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 13 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                case "Siberian":
                    if (genderOfTheCat == "m")
                    {
                        monthsOfTheCat = 11 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    else if (genderOfTheCat == "f")
                    {
                        monthsOfTheCat = 12 * 12 / 6;
                        Console.WriteLine($"{monthsOfTheCat} cat months");
                    }
                    break;
                default:
                    Console.WriteLine($"{breed} is invalid cat!");
                    break;
            }
        }
    }
}
