using System;

namespace _05.SmallShop2
{
    class Program
    {
        static void Main(string[] args)
        {

            //град / продукт coffee water beer sweets peanuts
            //Sofia            0.50  0.80  1.20  1.45    1.60
            //Plovdiv          0.40  0.70  1.15  1.30   1.50
            //Varna            0.45  0.70  1.10  1.35   1.55
            // Винаги се прави switch редове по колони, а не колони по редове!

            string product = Console.ReadLine();
            string city = Console.ReadLine();
            double numberOfProductsOrdered = double.Parse(Console.ReadLine());

            double totalsum = 0;

            switch (city)
            {
                case "Sofia":
                    switch (product)
                    {
                        case "coffee":
                            totalsum = numberOfProductsOrdered * 0.50;
                            break;
                        case "water":
                            totalsum = numberOfProductsOrdered * 0.80;
                            break;
                        case "beer":
                            totalsum = numberOfProductsOrdered * 1.20;
                            break;
                        case "sweets":
                            totalsum = numberOfProductsOrdered * 1.45;
                            break;
                        case "peanuts":
                            totalsum = numberOfProductsOrdered * 1.60;
                            break;
                    }
                    break;
                case "Plovdiv":
                    switch (product)
                    {
                        case "coffee":
                            totalsum = numberOfProductsOrdered * 0.40;
                            break;
                        case "water":
                            totalsum = numberOfProductsOrdered * 0.70;
                            break;
                        case "beer":
                            totalsum = numberOfProductsOrdered * 1.15;
                            break;
                        case "sweets":
                            totalsum = numberOfProductsOrdered * 1.30;
                            break;
                        case "peanuts":
                            totalsum = numberOfProductsOrdered * 1.50;
                            break;
                    }
                    break;
                case "Varna":
                    switch (product)
                    {
                        case "coffee":
                            totalsum = numberOfProductsOrdered * 0.45;
                            break;
                        case "water":
                            totalsum = numberOfProductsOrdered * 0.7;
                            break;
                        case "beer":
                            totalsum = numberOfProductsOrdered * 1.10;
                            break;
                        case "sweets":
                            totalsum = numberOfProductsOrdered * 1.35;
                            break;
                        case "peanuts":
                            totalsum = numberOfProductsOrdered * 1.55;
                            break;
                    }
                    break;
                default:
                    Console.WriteLine("N/A");
                    break;


            }
            Console.WriteLine($"{totalsum:f2}");

        }
    }
}
