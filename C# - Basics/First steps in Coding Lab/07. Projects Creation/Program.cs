using System;

namespace _07._Projects_Creation
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int countOfProjescts = int.Parse(Console.ReadLine());
            int hoursFor1Project = 3;
            int ProjectsXHours = countOfProjescts * hoursFor1Project;
            Console.WriteLine($"The architect {name} will need {ProjectsXHours} hours to complete {countOfProjescts} project/s.");
        }
    }
}
