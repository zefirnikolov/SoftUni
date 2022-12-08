using System;

namespace _02._Maiden_Party
{
    class Program
    {
        static void Main(string[] args)
        {
            
            // Любовно послание -0.60 лв.
            // Восъчна роза -7.20 лв.
            // Ключодържател - 3.60 лв.
            // Карикатура - 18.20 лв.
            // Късмет изненада -22 лв.





            double priceForTheParty = double.Parse(Console.ReadLine());
            int loveMessagesNumber = int.Parse(Console.ReadLine());
            int rosesNumber = int.Parse(Console.ReadLine());
            int keychainsNumber = int.Parse(Console.ReadLine());
            int caricaturesNumber = int.Parse(Console.ReadLine());
            int surprisesNumber = int.Parse(Console.ReadLine());

            double sumForAllSells = 0;
            double sumForSoldLoveMessages = loveMessagesNumber * 0.6;
            double sumForSoldRoses = rosesNumber * 7.2;
            double sumForSoldKeychains = keychainsNumber * 3.6;
            double sumfForSoldCarucatures = caricaturesNumber * 18.2;
            double sumForSoldSurprises = surprisesNumber * 22;

            sumForAllSells = sumForSoldLoveMessages + sumForSoldRoses + sumForSoldKeychains + sumfForSoldCarucatures + sumForSoldSurprises;

            double numberOfAllSells = loveMessagesNumber + rosesNumber + keychainsNumber + caricaturesNumber + surprisesNumber;

            if (numberOfAllSells >= 25)
            {
                sumForAllSells = sumForAllSells - (sumForAllSells * 0.35);
            }

            double sumForHosting = sumForAllSells * 0.1;

            sumForAllSells = sumForAllSells - sumForHosting;

            if (sumForAllSells >= priceForTheParty)
            {
                Console.WriteLine($"Yes! {(sumForAllSells - priceForTheParty):f2} lv left.");
            }
            else
            {
                Console.WriteLine($"Not enough money! {(priceForTheParty - sumForAllSells):f2} lv needed.");
            }
            
        }
    }
}
