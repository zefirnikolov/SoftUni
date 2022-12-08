using System;

namespace _08.TennisRanklist
{
    class Program
    {
        static void Main(string[] args)
        {
            int Loops = int.Parse(Console.ReadLine());
            int startingPoints = int.Parse(Console.ReadLine());
             
            int scoreInTheTournaments = 0;
            int tournamentsWon = 0;
            double averagepoints = 0;
            
            for (int i = 1; i <= Loops; i++)
            {
                string phaseReached = Console.ReadLine();

                if (phaseReached == "W")
                {
                    scoreInTheTournaments += 2000;
                    tournamentsWon++;
                }
                else if (phaseReached == "F")
                {
                    scoreInTheTournaments += 1200;
                }
                else if (phaseReached == "SF")
                {
                    scoreInTheTournaments += 720;
                }               
            }
            averagepoints = scoreInTheTournaments / Loops;

            double averagePointsFloored = Math.Floor(averagepoints);

            Console.WriteLine($"Final points: {startingPoints + scoreInTheTournaments}");
            Console.WriteLine($"Average points: {Math.Floor(averagePointsFloored)}");
            Console.WriteLine($"{(tournamentsWon * 1.0 / Loops * 100):f2}%");



        }
    }
}
