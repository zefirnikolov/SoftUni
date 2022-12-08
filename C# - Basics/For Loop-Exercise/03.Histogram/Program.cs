using System;

namespace _03.Histogram
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfLoops = int.Parse(Console.ReadLine());
            int p1 = 0;
            int p2 = 0;
            int p3 = 0;
            int p4 = 0;
            int p5 = 0;

            for (int i = 1; i <= numberOfLoops; i++)
            {
                int histogram = int.Parse(Console.ReadLine());
                if (histogram < 200)
                {
                    p1++;
                }
                else if (200 <= histogram && histogram <= 399)
                {
                    p2++;
                }
                else if (histogram >= 400 && histogram <= 599)
                {
                    p3++;
                }
                else if (histogram >= 600 && histogram <= 799)
                {
                    p4++;
                }
                else if (histogram >= 800)
                {
                    p5++;
                }
            }
            double percentP1 = p1 * 1.0 / numberOfLoops * 100;
            double percentP2 = p2 * 1.0 / numberOfLoops * 100;


            Console.WriteLine($"{percentP1:f2}%");
            Console.WriteLine($"{percentP2:f2}%");
            Console.WriteLine($"{(p3 * 1.0 / numberOfLoops * 100):f2}%");
            Console.WriteLine($"{(p4 * 1.0 / numberOfLoops * 100):f2}%");
            Console.WriteLine($"{(p5 * 1.0 / numberOfLoops * 100):f2}%");
        }
    }
}
