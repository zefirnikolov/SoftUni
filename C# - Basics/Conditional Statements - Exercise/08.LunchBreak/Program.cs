using System;

namespace _08.LunchBreak
{
    class Program
    {
        static void Main(string[] args)
        {
            string nameOfTheSeries = Console.ReadLine();
            int timeOfEpisodeOfTheSeries = int.Parse(Console.ReadLine());
            int timeOfTheWholeBreak = int.Parse(Console.ReadLine());

            double timeForLunch = timeOfTheWholeBreak * 0.125;
            double timeForRest = timeOfTheWholeBreak * 0.25;

            double howMuchTimeLeft = timeOfTheWholeBreak - timeForLunch - timeForRest;

            double isThereEnoughTimetoWatchTheSeries = howMuchTimeLeft - timeOfEpisodeOfTheSeries;

            
            
            bool isTheTimeForSeriesEnough = isThereEnoughTimetoWatchTheSeries >= 0;

            if (isTheTimeForSeriesEnough)
            {
                Console.WriteLine($"You have enough time to watch {nameOfTheSeries} and left with {Math.Ceiling(isThereEnoughTimetoWatchTheSeries)} minutes free time.");
            }
            else
            {
                
                Console.WriteLine($"You don't have enough time to watch {nameOfTheSeries}, you need {Math.Ceiling(timeOfEpisodeOfTheSeries - howMuchTimeLeft)} more minutes.");
            }
        }
    }
}
