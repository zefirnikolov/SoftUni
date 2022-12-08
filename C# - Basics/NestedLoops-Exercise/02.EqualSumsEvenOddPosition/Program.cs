using System;

namespace _02.EqualSumsEvenOddPosition
{
    class Program
    {
        static void Main(string[] args)
        {
            int start = int.Parse(Console.ReadLine());
            int last = int.Parse(Console.ReadLine());

            for (int i = start; i <= last; i++)
            {
                string number = i.ToString();  // Превръщаме числото в стринг. от int става string. За да използваме дължината на числото.
                int evenSum = 0;
                int oddSum = 0;

                for (int j = 0; j < number.Length; j++) // Използваме дължината на числото като край на loop-a.
                {
                    int currentDigit = int.Parse(number[j].ToString());  // Вадим последователно числата, превръщаме отново в int.
                    if (j % 2 == 0)
                    {
                        oddSum += currentDigit;
                    }
                    else
                    {
                        evenSum += currentDigit;
                    }
                }
                if (evenSum == oddSum)
                {
                    Console.Write($"{i} ");
                }
            }
        }
    }
}
