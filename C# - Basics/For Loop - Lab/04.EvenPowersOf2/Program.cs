using System;

namespace _04.EvenPowersOf2
{
    class Program
    {
        static void Main(string[] args)
        {
            int endOfLoop = int.Parse(Console.ReadLine());
            int num = 1;

            for (int i = 0; i <= endOfLoop; i += 3)
            {
                Console.WriteLine(num);
                num *= 2 * 2;

            }
        }
    }
}
