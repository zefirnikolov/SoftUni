using System;

namespace _01.ExcellentResult
{
    class Program
    {
        static void Main(string[] args)
        {

            // За да мога да извадя % и да го преформатирам, за да може да започне да го смята - например от прочитане на конзолата
            // трябва задължително числото да му бъде зададено да бъде в double - защото по default го смята в int и го закръгля.
            // а закръглянето винаги вади 0, защото процентът е 0.05 при 5% или 0.90 при 90% например. Все закръгля на 0.

            // решение с деление за дебъг% при изписване без 2 точки отзад - вади 0

            Console.WriteLine(15 / 100);

            // решение с деление за дебъг% при изписване с 2 точки отзад - вади правилния процент - използваш винаги double = 15% = 0.15.

            Console.WriteLine(15.00 / 100);

            // ако имам входно число int, за да го дебъгна в % - решението би трябвало да изглежда така:

            int percent = int.Parse(Console.ReadLine());
            double makePercentDoubleToBeAbleToDebugIt = percent;
            double CalculateTheRealPercentForDebug = makePercentDoubleToBeAbleToDebugIt / 100;

            Console.WriteLine(CalculateTheRealPercentForDebug);

        }
    }
}
