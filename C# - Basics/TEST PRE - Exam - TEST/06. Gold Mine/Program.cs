using System;

namespace _06._Gold_Mine
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfLocationsEqLoops1Loop = int.Parse(Console.ReadLine());
            double averageGoldExpected = double.Parse(Console.ReadLine());
            


            for (int i = 1; i <= numberOfLocationsEqLoops1Loop; i++)
            {
                int numberOfDaysOfDigginPerLocationEqLoops2Loop = int.Parse(Console.ReadLine());
                double sumOfAllGold = 0;
                double averageGold = 0;

                
                for (int j = 1; j <= numberOfDaysOfDigginPerLocationEqLoops2Loop; j++)
                {
                    double goldDigged = double.Parse(Console.ReadLine());
                    sumOfAllGold += goldDigged;

                }

                averageGold = sumOfAllGold / numberOfDaysOfDigginPerLocationEqLoops2Loop;
                if (averageGold >= averageGoldExpected)
                {
                    Console.WriteLine($"Good job! Average gold per day: {(sumOfAllGold / numberOfDaysOfDigginPerLocationEqLoops2Loop):f2}.");
                }
                else
                {
                    Console.WriteLine($"You need {(averageGoldExpected - averageGold):f2} gold.");
                }                              
                              
                if (numberOfLocationsEqLoops1Loop != i)
                {
                    averageGoldExpected = double.Parse(Console.ReadLine());
                }               
            }           
        }
    }
}
