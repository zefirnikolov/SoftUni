using System;

namespace _05._Best_Player
{
    class Program
    {
        static void Main(string[] args)
        {
            
            int maxGoals = int.MinValue;

            bool isEndtyped = true;


            for (; ;)
            {
                string name = Console.ReadLine();
                int scoredGoals = int.Parse(Console.ReadLine());


                if (name == "END")
                {
                    isEndtyped = false;
                    break;
                }


                if (scoredGoals >= 10)
                {
                    maxGoals = scoredGoals;
                    Console.WriteLine($"{name} is the best player!");
                    Console.WriteLine($"He has scored {maxGoals} goals and made a hat-trick !!!");
                    break;
                }

            }
        }
    }
}
