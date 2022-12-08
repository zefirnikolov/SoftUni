using System;

namespace _03.Time_15Minutes
{
    class Program
    {
        static void Main(string[] args)
        {
            int hours = int.Parse(Console.ReadLine());
            int minutes = int.Parse(Console.ReadLine());

            minutes += 15;

            if (minutes >= 60)
            {
                minutes -= 60; // minutes -= 60;
                hours += 1; // hours = hours + 1;
            }
            if (hours == 24)
            {
                hours = 0;
            }
            if (hours > 24)
            {
                Console.WriteLine("N/A");
            }
            else
            {
                Console.WriteLine($"{hours}:{minutes:D2}");
            }
        }
    }
}
