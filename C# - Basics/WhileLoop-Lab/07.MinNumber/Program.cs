using System;

namespace _07.MinNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            string numberOrStopCommand = Console.ReadLine();

            int minNumber = int.MaxValue;

            while (numberOrStopCommand != "Stop")
            {
                int textToNumber = int.Parse(numberOrStopCommand);// Взимаме string-a, не четем конзолата! Превръщаме string в число!

                if (textToNumber < minNumber)
                {
                    minNumber = textToNumber;
                }

                numberOrStopCommand = Console.ReadLine();

            }
            Console.WriteLine(minNumber);
        }
    }
}
 