using System;

namespace _05.Number100_200
{
    class Program
    {
        static void Main(string[] args)
        {

            //double ceilingNumber = double.Parse(Console.ReadLine());
            //double floorNumber = double.Parse(Console.ReadLine());
            //double absNumber = double.Parse(Console.ReadLine());
            //double round = double.Parse(Console.ReadLine());

            //Console.WriteLine(Math.Ceiling(ceilingNumber));
            //Console.WriteLine(Math.Floor(floorNumber));
            //Console.WriteLine(Math.Abs(absNumber));
            //Console.WriteLine(Math.Round(round, 2));
           

            //• под 100 отпечатайте: "Less than 100"
            //• между 100 и 200 отпечатайте: "Between 100 and 200"
            //• над 200 отпечатайте: "Greater than 200"

            int speed = int.Parse(Console.ReadLine());

            if (speed < 100)
            {
                Console.WriteLine("Less than 100");
            }
            else if (speed <=200)
            {
                Console.WriteLine("Between 100 and 200");
            }
            else if (speed > 200)
            {
                Console.WriteLine("Greater than 200");
            }
        }
    }
}
