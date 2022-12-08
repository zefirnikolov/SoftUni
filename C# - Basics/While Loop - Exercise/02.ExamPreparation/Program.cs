using System;

namespace _02.ExamPreparation
{
    class Program
    {
        static void Main(string[] args)
        {
            int howMuchBadScoresHeHasToHave = int.Parse(Console.ReadLine());

            double sumGrades = 0;
            int badGradesCounter = 0;
            int numberOfProblems = 0;
            string lastProblem = string.Empty;


            string nameOfTheProblem = Console.ReadLine(); // Слага се точно преди да се отвори While loop и след това същото се вкарва
                                                          // да се чете най-отдолу в loop-a.
            while (nameOfTheProblem != "Enough")
            {
                int grade = int.Parse(Console.ReadLine());

                if (grade <= 4)
                {
                    badGradesCounter++;

                }
                if (badGradesCounter == howMuchBadScoresHeHasToHave)
                {
                    Console.WriteLine($"You need a break, {badGradesCounter} poor grades.");
                    break;
                }

                numberOfProblems++;
                sumGrades += grade;
                lastProblem = nameOfTheProblem;
                nameOfTheProblem = Console.ReadLine();
            }

            if (nameOfTheProblem == "Enough")
            {
                double averageGrade = sumGrades / numberOfProblems;
                Console.WriteLine($"Average score: {averageGrade:f2}");
                Console.WriteLine($"Number of problems: {numberOfProblems}");
                Console.WriteLine($"Last problem: {lastProblem}");
            }            
        }
    }
}
