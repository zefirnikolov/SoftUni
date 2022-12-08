using System;

namespace _04.Walking
{
    class Program
    {
        static void Main(string[] args)
        {
            string seekingForStringEnteringNumbers = Console.ReadLine();

            int totalSteps = 0;

            while (seekingForStringEnteringNumbers != "Going home")
            {
                int stepsIncrease = int.Parse(seekingForStringEnteringNumbers); // преобразувам стринга в числа, за да го смятам

                totalSteps += stepsIncrease;
                if (totalSteps >= 10000)
                {
                    Console.WriteLine($"Goal reached! Good job!");
                    Console.WriteLine($"{totalSteps - 10000} steps over the goal!");
                    return;
                }
                seekingForStringEnteringNumbers = Console.ReadLine();
            }
            
                        
            int stepsToHome = int.Parse(Console.ReadLine());
            totalSteps += stepsToHome;

            if (totalSteps >= 10000)
            {
                Console.WriteLine($"Goal reached! Good job!");
                Console.WriteLine($"{totalSteps - 10000} steps over the goal!");
            }
            else
            {
                Console.WriteLine($"{10000 - totalSteps} more steps to reach goal.");
            }
        }
    }
}
