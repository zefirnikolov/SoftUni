using System;

namespace _01.USDtoBGN
{
    class Program
    {
        static void Main(string[] args)
        {
            double NumberUsd = double.Parse(Console.ReadLine());
            double USDto1BGN = 1.79549;
            double ConverUsdtoBGN = NumberUsd * USDto1BGN;
            Console.WriteLine(ConverUsdtoBGN);
        }
    }
}
