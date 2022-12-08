using System;

namespace _04._Workout
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfKilometersEqLoops = int.Parse(Console.ReadLine());
            double kilometersForFirstDay = double.Parse(Console.ReadLine());

            double kilometerThreshold = 1000;
            double allKilometers = kilometersForFirstDay;
 
            for (int i = 1; i <= numberOfKilometersEqLoops; i++)
            {

                int PercentIcrease = int.Parse(Console.ReadLine());
                kilometersForFirstDay = kilometersForFirstDay + (kilometersForFirstDay * PercentIcrease / 100);
                allKilometers += kilometersForFirstDay;

            }

            double kilometeresNeeded = kilometerThreshold - allKilometers;
            double kilometeresNeededCeiled = Math.Ceiling(kilometeresNeeded);

            double kilometersPassed = allKilometers - kilometerThreshold;
            double kilometeresPassedCeiled = Math.Ceiling(kilometersPassed);


            bool isThresholdReached = allKilometers >= kilometerThreshold;
            
            if (isThresholdReached)
            {
                Console.WriteLine($"You've done a great job running {kilometeresPassedCeiled} more kilometers!");
            }
            else
            {
                Console.WriteLine($"Sorry Mrs. Ivanova, you need to run {kilometeresNeededCeiled} more kilometers");
            }
        }
    }
}
