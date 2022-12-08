using System;

namespace _04.TrainTheTrainers
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfPeopleInTheJuryEqLoops = int.Parse(Console.ReadLine());

            
            double sumOfAllGrades = 0;            
            double gradesInTheWhileLoopCounter = 0;
            double sumOfAllSpins = 0;

            string theme = Console.ReadLine();
            while (theme != "Finish")
            {
                double sumOfGradesPerTheme = 0;
                double gradesInTheForLoopCounter = 0;
                for (int i = 1; i <= numberOfPeopleInTheJuryEqLoops; i++)
                {
                    double grade = double.Parse(Console.ReadLine());
                    sumOfGradesPerTheme += grade;
                    gradesInTheForLoopCounter++;
                }

                sumOfAllGrades += sumOfGradesPerTheme;
                gradesInTheWhileLoopCounter++;
                sumOfAllSpins = gradesInTheWhileLoopCounter * numberOfPeopleInTheJuryEqLoops;
                Console.WriteLine($"{theme} - {(sumOfGradesPerTheme / gradesInTheForLoopCounter):f2}.");
                theme = Console.ReadLine();
            }
            Console.WriteLine($"Student's final assessment is {(sumOfAllGrades / sumOfAllSpins):f2}.");
        }
    }
}
