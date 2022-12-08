using System;

namespace _01.NumberPyramid2
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int currentNumber = 1;
            bool isCurrentNumberHigherThanNFLAG = false;

            for (int rows = 1; rows <= n; rows++)
            {

                for (int columns = 1; columns <= rows; columns++)
                {
                    if (currentNumber > n)
                    {
                        isCurrentNumberHigherThanNFLAG = true;
                        break;
                    }
                    Console.Write($"{currentNumber} ");
                    currentNumber++;
                }
                if (isCurrentNumberHigherThanNFLAG)
                {
                    break;
                }
                Console.WriteLine();
            }
        }
    }
}
