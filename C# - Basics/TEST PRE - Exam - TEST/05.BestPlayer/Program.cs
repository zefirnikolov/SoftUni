using System;

namespace _05.BestPlayer
{
    class Program
    {
        static void Main(string[] args)
        {
            string nameUntilEnd = Console.ReadLine();

            int maxGoals = int.MinValue;
            string bestPlayer = string.Empty;

            while (nameUntilEnd != "END")
            {
                int currentGoals = int.Parse(Console.ReadLine());

                if (currentGoals > maxGoals)
                {
                    bestPlayer = nameUntilEnd;
                    maxGoals = currentGoals;
                }
                if (currentGoals >= 10)
                {
                    Console.WriteLine($"{bestPlayer} is the best player!");
                    Console.WriteLine($"He has scored {maxGoals} goals and made a hat-trick !!!");
                    return;
                }


                nameUntilEnd = Console.ReadLine();
            }
            Console.WriteLine($"{bestPlayer} is the best player!");
            if (maxGoals >= 3)
            {
                Console.WriteLine($"He has scored {maxGoals} goals and made a hat-trick !!!");
            }
            else
            {
                Console.WriteLine($"He has scored {maxGoals} goals.");
            }            
        }
    }
}
