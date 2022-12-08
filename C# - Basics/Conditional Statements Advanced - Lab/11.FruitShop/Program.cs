using System;

namespace _11.FruitShop
{
    class Program
    {
        static void Main(string[] args)
        {
            //плод      (banana / apple / orange / grapefruit / kiwi / pineapple / grapes)
            // Monday      2.50    1.20     0.85     1.45       2.70    5.50         3.85
            // Tuesday     2.50    1.20     0.85     1.45       2.70    5.50         3.85
            //Wednesday    2.50    1.20     0.85     1.45       2.70    5.50         3.85
            //Thursday     2.50    1.20     0.85     1.45       2.70    5.50         3.85
            // Friday      2.50    1.20     0.85     1.45       2.70    5.50         3.85
            //Saturday     2.70    1.25     0.90     1.60       3.00    5.60         4.20
            // Sunday      2.70    1.25     0.90     1.60       3.00    5.60         4.20

            string fruit = Console.ReadLine();
            string dayOfWeek = Console.ReadLine();
            double numberOfProductsOrdered = double.Parse(Console.ReadLine());

            double totalsum = 0;

            // Правиш го наобратно. Винаги е редове по колони, а не колони по редове. Т.е Switch (dayOfWeek) и вътре switch (fruit);

            switch (fruit)
            {
                case "banana":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 2.50;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 2.70;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                case "apple":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 1.20;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 1.25;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        default:
                            Console.WriteLine("error");
                            break;
                    }
                    break;
                case "orange":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 0.85;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 0.90;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                case "grapefruit":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 1.45;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 1.60;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                case "kiwi":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 2.70;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 3.00;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                case "pineapple":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 5.50;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 5.60;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                case "grapes":
                    switch (dayOfWeek)
                    {
                        case "Monday":
                        case "Tuesday":
                        case "Wednesday":
                        case "Thursday":
                        case "Friday":
                            totalsum = numberOfProductsOrdered * 3.85;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                        case "Saturday":
                        case "Sunday":
                            totalsum = numberOfProductsOrdered * 4.20;
                            Console.WriteLine($"{totalsum:f2}");
                            break;
                    }
                    break;
                default:
                    Console.WriteLine("error");
                    break;
            }
        }
    }
}
