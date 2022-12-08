using System;

namespace _06.Oscars
{
    class Program
    {
        static void Main(string[] args)
        {

            string nameOfTheNomenee = Console.ReadLine();
            double startingPointsFromTheAcademy = double.Parse(Console.ReadLine());

            int juryCountEqLoops = int.Parse(Console.ReadLine());
            double nominationThreshold = 1250.5;

            double pointsPerloop = 0;
            double totalPointsANomeneeGets = 0;

            for (int i = 1; i <= juryCountEqLoops; i++)
            {
                string nameOfTheJury = Console.ReadLine();
                double pointsFromTheJury = double.Parse(Console.ReadLine());
                
                int wordLenght = nameOfTheJury.Length;

                pointsPerloop += ((wordLenght * pointsFromTheJury) / 2);


                totalPointsANomeneeGets = pointsPerloop + startingPointsFromTheAcademy;
                if (totalPointsANomeneeGets > nominationThreshold)
                {
                    Console.WriteLine($"Congratulations, {nameOfTheNomenee} got a nominee for leading role with {totalPointsANomeneeGets:f1}!");
                    break;
                }

            }
            if (totalPointsANomeneeGets <= nominationThreshold)
            {
                Console.WriteLine($"Sorry, {nameOfTheNomenee} you need {(nominationThreshold - totalPointsANomeneeGets):f1} more!");
            }
        }
    }
}
