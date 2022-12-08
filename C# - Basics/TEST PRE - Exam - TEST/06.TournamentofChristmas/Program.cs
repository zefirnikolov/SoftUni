using System;

namespace _06.TournamentofChristmas
{
    class Program
    {
        static void Main(string[] args)
        {

            int numberOfDaysEqLoops = int.Parse(Console.ReadLine());
            int allDaysLoseCounter = 0;
            int alldaysWinCounter = 0;
            double totalMoney = 0;

            for (int i = 1; i <= numberOfDaysEqLoops; i++)
            {

                string typeOfSportUntilFinish = Console.ReadLine();

                int loseCounterForTheDay = 0;
                int winCounterForTheDay = 0;
                double moneyWonForADay = 0;
                while (typeOfSportUntilFinish != "Finish")
                {
                    string winOrLose = Console.ReadLine();
                    if (winOrLose == "win")
                    {
                        alldaysWinCounter++;
                        winCounterForTheDay++;
                        moneyWonForADay += 20;
                    }
                    else if (winOrLose == "lose")
                    {
                        loseCounterForTheDay++;
                        allDaysLoseCounter++;
                    }
                    typeOfSportUntilFinish = Console.ReadLine();
                }
                
                if (winCounterForTheDay > loseCounterForTheDay)
                {
                    moneyWonForADay = moneyWonForADay + moneyWonForADay * 0.1;
                }
                totalMoney += moneyWonForADay;
            }

            if (alldaysWinCounter > allDaysLoseCounter)
            {
                totalMoney = totalMoney + totalMoney * 0.2;
                Console.WriteLine($"You won the tournament! Total raised money: {totalMoney:f2}");
            }
            else
            {
                Console.WriteLine($"You lost the tournament! Total raised money: {totalMoney:f2}");
            }
        }
    }
}
