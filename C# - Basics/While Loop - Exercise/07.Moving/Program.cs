using System;

namespace _07.Moving
{
    class Program
    {
        static void Main(string[] args)
        {
            int lenght = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());

            int m3OfTheApartment = lenght * width * height;

            double sumOfNewPieces = 0;
            string inputM3untilCommandDone = Console.ReadLine();

            while (inputM3untilCommandDone != "Done")
            {
                double increaseM3 = double.Parse(inputM3untilCommandDone);
                sumOfNewPieces += increaseM3;
                if (sumOfNewPieces > m3OfTheApartment)
                {
                    Console.WriteLine($"No more free space! You need {sumOfNewPieces - m3OfTheApartment} Cubic meters more.");
                    return;
                }

                inputM3untilCommandDone = Console.ReadLine();
            }
            Console.WriteLine($"{m3OfTheApartment - sumOfNewPieces} Cubic meters left.");
        }
    }
}
