using System;

namespace _03._Deposit_Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            //1.Депозирана сума – реално число в интервала[100.00... 10000.00]
            //2.Срок на депозита(в месеци) – цяло число в интервала[1...12]
            //3.Годишен лихвен процент – реално число в интервала[0.00...100.00]


            double depositSum = double.Parse(Console.ReadLine());
            int terminmonths = int.Parse(Console.ReadLine());
            double interestRate = double.Parse(Console.ReadLine());

            double interestfor1yearAcrued = depositSum * interestRate / 100;
            double interestfor1monthAcrued = interestfor1yearAcrued / 12;
            double sum = interestfor1monthAcrued * terminmonths + depositSum;

            Console.WriteLine(sum);

        }
    }
}
