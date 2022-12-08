using System;

namespace _01.ExcellentResult2
{
    class Program
    {
        static void Main(string[] args)
        {
            const double EXCELLENT_GRADE = 5.50;

            double Grade = double.Parse(Console.ReadLine());
            bool isTheGradeExcellent = Grade >= EXCELLENT_GRADE;

            if (isTheGradeExcellent)
            {
                Console.WriteLine("Excellent!");
            }
            else
            {
                Console.WriteLine("Not Excellent!");
            }

        } 
    }
}