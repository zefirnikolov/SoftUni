using System;

namespace _08.OnTimefortheExam
{
    class Program
    {
        static void Main(string[] args)
        {
            int hourOfTheExam = int.Parse(Console.ReadLine());
            int minutesOfTheExam = int.Parse(Console.ReadLine());
            int arrivalHour = int.Parse(Console.ReadLine());
            int arrivalMinutes = int.Parse(Console.ReadLine());

            //• “Late”, ако студентът пристига по-късно от часа на изпита.
            //• “On time”, ако студентът пристига точно в часа на изпита или до 30 минути по-рано.
            //• “Early”, ако студентът пристига повече от 30 минути преди часа на изпита.

            int SumOfTheExamInMinutes = hourOfTheExam * 60 + minutesOfTheExam;
            int SumOfTheArrivalInMinutes = arrivalHour * 60 + arrivalMinutes;

            if (SumOfTheArrivalInMinutes > SumOfTheExamInMinutes)
            {
                Console.WriteLine("Late");
                if (SumOfTheArrivalInMinutes - SumOfTheExamInMinutes < 60)
                {
                    Console.WriteLine($"{SumOfTheArrivalInMinutes - SumOfTheExamInMinutes} minutes after the start");
                }
                else
                {
                    int hours = (SumOfTheArrivalInMinutes - SumOfTheExamInMinutes) / 60;
                    int minutes = (SumOfTheArrivalInMinutes - SumOfTheExamInMinutes) % 60;
                    Console.WriteLine($"{hours}:{minutes:d2} hours after the start");
                }
            }
            else if (SumOfTheArrivalInMinutes == SumOfTheExamInMinutes || SumOfTheExamInMinutes - SumOfTheArrivalInMinutes <= 30)
            {
                Console.WriteLine("On time");
                if ((SumOfTheArrivalInMinutes - SumOfTheExamInMinutes) != 0)
                {
                    int minutes = SumOfTheExamInMinutes - SumOfTheArrivalInMinutes;
                    Console.WriteLine($"{minutes} minutes before the start");
                }
                else
                {
                    
                }
            }
            else if (SumOfTheExamInMinutes - SumOfTheArrivalInMinutes > 30)
            {
                Console.WriteLine("Early");
                if (Math.Abs(SumOfTheArrivalInMinutes - SumOfTheExamInMinutes) < 60)
                {
                    Console.WriteLine($"{SumOfTheExamInMinutes - SumOfTheArrivalInMinutes } minutes before the start");
                }
                else
                {
                    int hours = (SumOfTheExamInMinutes - SumOfTheArrivalInMinutes) / 60;
                    int minutes = (SumOfTheExamInMinutes - SumOfTheArrivalInMinutes) % 60;
                    Console.WriteLine($"{hours}:{minutes:d2} hours before the start");
                }
            }
        }
    }
}
 