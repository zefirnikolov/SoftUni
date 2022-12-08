using System;

namespace _03.DepositCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            //1.Депозирана сума – реално число в интервала[100.00... 10000.00]
            //2.Срок на депозита(в месеци) – цяло число в интервала[1...12]
            //3.Годишен лихвен процент – реално число в интервала[0.00...100.00]

          
            double depositSum = double.Parse(Console.ReadLine());
            int term = int.Parse(Console.ReadLine());
            double interestRate = double.Parse(Console.ReadLine());

            //сума = депозирана сума + срок на депозита *((депозирана сума* годишен лихвен процент ) / 12)
            
            double sum = depositSum + term * ((depositSum * interestRate / 100) / 12);
           
            Console.WriteLine(sum);


            
        }
    }
}
