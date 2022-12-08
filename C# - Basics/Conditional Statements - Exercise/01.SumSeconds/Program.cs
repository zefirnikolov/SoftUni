using System;

namespace _01.SumSeconds
{
    class Program
    {
        static void Main(string[] args)
        {
            //Calculate seconds and convert them to minutes:seconds
            
            int firstTimeInSeconds = int.Parse(Console.ReadLine());
            int secondTimeInSeconds = int.Parse(Console.ReadLine());
            int thirdTimeInSeconds = int.Parse(Console.ReadLine());

            int totalTimeInSeconds = firstTimeInSeconds + secondTimeInSeconds + thirdTimeInSeconds;

            int minutes = totalTimeInSeconds / 60;
            int seconds = totalTimeInSeconds % 60;

            if (seconds < 10)
            {
                Console.WriteLine($"{minutes}:0{seconds}");
            }
            else
            {
                Console.WriteLine($"{minutes}:{seconds}");
            }
        }
    }
}
