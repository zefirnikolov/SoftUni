using System;

namespace _06.SumAndProduct
{
    class Program
    {
        static void Main(string[] args)
        {

            int n = int.Parse(Console.ReadLine());

            for (int a = 1; a < 9; a++)
            {
                for (int b = 9; b > a; b--)
                {
                    for (int c = 0; c < 9; c++)
                    {
                        for (int d = 9; d > c; d--)
                        {
                            int sumABCD = a + b + c + d;
                            int productABCD = a * b * c * d;

                            if (sumABCD == productABCD && n % 10 == 5)
                            {
                                Console.WriteLine($"{a}{b}{c}{d}");
                                return;
                            }
                            if (productABCD / sumABCD == 3 && n % 3 == 0)
                            {
                                Console.WriteLine($"{d}{c}{b}{a}");
                                return;
                            }
                        }
                    }
                }
            }
            Console.WriteLine("Nothing found");
        }
    }
}
