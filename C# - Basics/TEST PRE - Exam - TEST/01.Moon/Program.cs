using System;

namespace _01.Moon
{
    class Program
    {
        static void Main(string[] args)
        {
            double averageSpeed = double.Parse(Console.ReadLine());
            double litersNeededFor100km = double.Parse(Console.ReadLine());

            double distanceToTheMoonAndBack = 384400 * 2;

            double timeToGoAndBack = Math.Ceiling(distanceToTheMoonAndBack / averageSpeed);
            double timeIncludingStayOnTheMoon = timeToGoAndBack + 3;

            double litersNeededForAll = (litersNeededFor100km * distanceToTheMoonAndBack) / 100;

            Console.WriteLine(timeIncludingStayOnTheMoon);
            Console.WriteLine(litersNeededForAll);

        }
    }
}
