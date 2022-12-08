using System;

namespace _02._Mountain_Run
{
    class Program
    {
        static void Main(string[] args)
        {
            double recordInSeconds = double.Parse(Console.ReadLine());

            double metersNeeded = double.Parse(Console.ReadLine());
            double timeInSeconds = double.Parse(Console.ReadLine());


            

            double slowing = (Math.Floor(metersNeeded / 50)) * 30;

            double totalTime = metersNeeded * timeInSeconds + slowing;

            if (totalTime < recordInSeconds)
            {
                Console.WriteLine($"Yes! The new record is {totalTime:f2} seconds.");
            }
            else
            {
                Console.WriteLine($"No! He was {(totalTime - recordInSeconds):f2} seconds slower.");
            }
        }
    }
}
