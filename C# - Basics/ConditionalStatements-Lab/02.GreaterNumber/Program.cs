using System;

namespace _02.GreaterNumber
{
    class Program
    {
        static void Main(string[] args)
        {

            int number1 = int.Parse(Console.ReadLine());
            int number2 = int.Parse(Console.ReadLine());

            bool isNumber1GreaterThanNumber2 = number1 > number2;

            if (isNumber1GreaterThanNumber2)
            {
                Console.WriteLine(number1);
            }
            else
            {
                Console.WriteLine(number2);
            }
        }
    }
}
