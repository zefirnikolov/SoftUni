using System;

namespace _04._Gifts_from_Santa
{
    class Program
    {
        static void Main(string[] args)
        {
            int nEqEndOfTheLoop = int.Parse(Console.ReadLine());
            int mEqStartOfTheLoop = int.Parse(Console.ReadLine());
            int sEqStop = int.Parse(Console.ReadLine());

            

            for (int i = mEqStartOfTheLoop; i >= nEqEndOfTheLoop; i--)
            {


                if (i % 2 == 0 && i % 3 == 0)
                {
                    if (i == sEqStop)
                    {
                        return;
                    }
                    Console.Write($"{i} ");
                }
            }

        }
    }
}
