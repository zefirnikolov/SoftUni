using System;

namespace _04.Sequence2k_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());
            int i = 0;

            while (i <= number)
            {
                
                i = i * 2 + 1;
                if (i <= number)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
