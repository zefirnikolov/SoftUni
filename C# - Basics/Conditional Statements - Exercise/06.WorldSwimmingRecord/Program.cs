using System;

namespace _06.WorldSwimmingRecord
{
    class Program
    {
        static void Main(string[] args)
        {
            double recordInSeconds = double.Parse(Console.ReadLine());
            double lenghtInMeters = double.Parse(Console.ReadLine());
            double timeOfIvanchoInSecondsPer1M = double.Parse(Console.ReadLine());

            double sumTimeWithoutSlowing = timeOfIvanchoInSecondsPer1M * lenghtInMeters;

            double slowingBecauseOfTide = Math.Floor(lenghtInMeters / 15) * 12.50;

            double sumTimeOfIvancho = sumTimeWithoutSlowing + slowingBecauseOfTide;

            bool isRecordBeat = sumTimeOfIvancho < recordInSeconds;

            if (isRecordBeat)
            {
                Console.WriteLine($"Yes, he succeeded! The new world record is {sumTimeOfIvancho:f2} seconds.");
            }
            else
            {
                Console.WriteLine($"No, he failed! He was {(sumTimeOfIvancho - recordInSeconds):f2} seconds slower.");
            }           
        }
    }
}
