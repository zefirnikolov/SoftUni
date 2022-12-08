using System;

namespace _05.SmallShop
{
    class Program
    {
        static void Main(string[] args)
        {
            string product = Console.ReadLine();
            string city = Console.ReadLine();
            double numberOfProductsOrdered = double.Parse(Console.ReadLine());

            switch (product)
            {
                case "coffee":
                    if (city == "Sofia")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.50);
                    }
                    else if (city == "Plovdiv")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.40);
                    }
                    else if (city == "Varna")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.45);
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "water":
                    if (city == "Sofia")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.80);
                    }
                    else if (city == "Plovdiv")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.70);
                    }
                    else if (city == "Varna")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 0.70);
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "beer":
                    if (city == "Sofia")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.20);
                    }
                    else if (city == "Plovdiv")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.15);
                    }
                    else if (city == "Varna")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.10);
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "sweets":
                    if (city == "Sofia")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.45);
                    }
                    else if (city == "Plovdiv")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.3);
                    }
                    else if (city == "Varna")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.35);
                    }
                    else
                    {
                        Console.WriteLine("N/A");
                    }
                    break;
                case "peanuts":
                    if (city == "Sofia")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.60);
                    }
                    else if (city == "Plovdiv")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.50);
                    }
                    else if (city == "Varna")
                    {
                        Console.WriteLine(numberOfProductsOrdered * 1.55);
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
        }
    }
}
