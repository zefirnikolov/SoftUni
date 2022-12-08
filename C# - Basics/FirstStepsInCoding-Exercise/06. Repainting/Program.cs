using System;

namespace _06._Repainting
{
    class Program
    {
        static void Main(string[] args)
        {
            //• Предпазен найлон -1.50 лв.за кв. метър + 2 кв м
            //• Боя - 14.50 лв.за литър + 10% боя
            //• Разредител за боя - 5.00 лв.за литър 
            // + 0.40 за торбички

            //Входът се чете от конзолата и съдържа точно 4 реда:
            //1.Необходимо количество найлон(в кв.м.) -цяло число в интервала[1... 100] 
            //2.Необходимо количество боя(в литри) -цяло число в интервала[1...100] 
            //3.Количество разредител(в литри) - цяло число в интервала[1...30] 5.00 лв.за литър 
            //4.Часовете, за които майсторите ще свършат работата -цяло число в интервала[1...9]

            
            
            int nylon = int.Parse(Console.ReadLine());
            double priceOfNylonPerM2 = 1.50;
            double extraM2Nylon = 2;
            int paint = int.Parse(Console.ReadLine());
            double priceOfPaintPerLitre = 14.50;
            double extraPaintPerLitreInPercent = 0.1;
            int waterForPaint = int.Parse(Console.ReadLine());
            double PriceforWaterForPaint = 5;
            double bags = 0.40;
            int workingHours = int.Parse(Console.ReadLine());


            double sumOfNylonPlusExtra = (nylon + extraM2Nylon) * priceOfNylonPerM2;
            double sumOfPaintPlusExtraPercent = (paint + (paint * extraPaintPerLitreInPercent)) * priceOfPaintPerLitre;
            double sumOfWaterForPaint = waterForPaint * PriceforWaterForPaint;
            double sumOfAllPlusBags = sumOfNylonPlusExtra + sumOfPaintPlusExtraPercent + sumOfWaterForPaint + bags;
            double sumforWorkers = (sumOfAllPlusBags * 0.3) * workingHours;

            double sumofAllexpenses = sumOfAllPlusBags + sumforWorkers;

            Console.WriteLine($"{sumofAllexpenses}");

        }
    }
}
 