using System;

namespace _03.Vacation
{
    class Program
    {
        static void Main(string[] args)
        {
            double moneyNeeded = double.Parse(Console.ReadLine());
            double money = double.Parse(Console.ReadLine());



            int spendCounter = 0;
            int dayscounter = 0;
            

            double sumMoney = money;
            if (money >= moneyNeeded)
            {
                Console.WriteLine($"You saved the money for {dayscounter} days.");
            }

            while (spendCounter < 5)
            {
                
                string spendOrSave = Console.ReadLine();
                double addOrRemoveMoney = double.Parse(Console.ReadLine());

                if (spendOrSave == "spend")
                {
                    addOrRemoveMoney = -1 * addOrRemoveMoney;
                    
                    spendCounter++;
                }
                else if (spendOrSave == "save")
                {
                    spendCounter = 0;
                }
                else
                {
                    addOrRemoveMoney = 0;
                }
                dayscounter++;
                sumMoney += addOrRemoveMoney;
                
                if (sumMoney >= moneyNeeded)
                {
                    Console.WriteLine($"You saved the money for {dayscounter} days.");
                    break;
                }

                if (sumMoney < 0)
                {
                    sumMoney = 0;
                }
            }
            
            if (spendCounter == 5)
            {
                Console.WriteLine($"You can't save the money.");
                Console.WriteLine(dayscounter);
            }
        }
    }
}
