using System;

namespace _08.Graduation
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int iEqGrade = 0;
            
            double totalScore = 0;
            double averageScore = 0;
            int fails = 0;

            bool is_graduated = true;
            
            
            while (iEqGrade < 12)
            {
                double score = double.Parse(Console.ReadLine());
                iEqGrade++;
                totalScore += score;
                if (score < 4)
                {
                    totalScore -= score;
                    fails++;
                }
                if (fails == 2)
                {
                    iEqGrade--;
                    is_graduated = false;
                    break;
                }
            }


            averageScore = totalScore / iEqGrade;

            if (is_graduated)
            {
                Console.WriteLine($"{name} graduated. Average grade: {averageScore:f2}");
            }
            else
            {
                Console.WriteLine($"{name} has been excluded at {iEqGrade} grade");
            }            
        }
    }
}
