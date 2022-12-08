using System;

namespace _03.EvenorOdd
{
    class Program
    {
        static void Main(string[] args)
        {

            // Ако търси четно число - кодът е = if (number % 2 == 0)
            // Ако търси нечетно число - кодът е = if (number % 2 == 1)

            int number = int.Parse(Console.ReadLine());

            if (number % 2 == 0)
            {
                Console.WriteLine("even");
            }
            else
            {
                Console.WriteLine("odd");
            }
            
        }
    }
}
