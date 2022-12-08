using System;

namespace _06.MaxNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            string numberOrStopCommand = Console.ReadLine();

            int maxNumber = int.MinValue;

            while (numberOrStopCommand != "Stop")
            {
                int textToNumber = int.Parse(numberOrStopCommand); // Взимаме String-1, не четем конзолата! Превръщаме string в число!

                if (textToNumber > maxNumber)
                {
                    maxNumber = textToNumber;
                }
                
                numberOrStopCommand = Console.ReadLine();
                
            }
            Console.WriteLine(maxNumber);
        }
    }
}
