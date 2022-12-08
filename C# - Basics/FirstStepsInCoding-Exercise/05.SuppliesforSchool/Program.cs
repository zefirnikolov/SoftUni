using System;

namespace _05.SuppliesforSchool
{
    class Program
    {
        static void Main(string[] args)
        {
            //• Пакет химикали -5.80 лв.
            //• Пакет маркери -7.20 лв.
            //• Препарат - 1.20 лв(за литър)
            

            // Input
        //• Брой пакети химикали - цяло число в интервала[0...100]
        //• Брой пакети маркери - цяло число в интервала[0...100]
        //• Литри препарат за почистване на дъска -цяло число в интервала[0...50]
        //• Процент намаление -цяло число в интервала[0...100]

            int PacketsOfPens = int.Parse(Console.ReadLine());
            double PricePerPacketofPens = 5.80;
            int PacketsOfMarkers = int.Parse(Console.ReadLine());
            double PricePerPacketofMarkers = 7.20;
            int packetsOfWashingPowder = int.Parse(Console.ReadLine());
            double PricePerPacketofWashingPowder = 1.20;
            int PriceReductionInPercent = int.Parse(Console.ReadLine());
            

            double sum = (PacketsOfPens * PricePerPacketofPens) + (PacketsOfMarkers * PricePerPacketofMarkers) + (packetsOfWashingPowder * PricePerPacketofWashingPowder);
            double sumWithPriceReduction = sum - (sum * PriceReductionInPercent / 100);

            Console.WriteLine(sumWithPriceReduction);
            


        }
    }
}
