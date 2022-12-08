using System;

namespace _06.Cake
{
    class Program
    {
        static void Main(string[] args)
        {
            int lenght = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());

            int numberOfPiecesInTheCake = lenght * width;

            int sumOfPieces = 0;
            string piecesTakenUntilStop = Console.ReadLine();

            while (piecesTakenUntilStop != "STOP")
            {
                int piecesIncrease = int.Parse(piecesTakenUntilStop);
                
                sumOfPieces += piecesIncrease;
                if (sumOfPieces > numberOfPiecesInTheCake)
                {
                    Console.WriteLine($"No more cake left! You need {sumOfPieces - numberOfPiecesInTheCake} pieces more.");
                    return;
                }


                piecesTakenUntilStop = Console.ReadLine();
            }

            Console.WriteLine($"{numberOfPiecesInTheCake - sumOfPieces} pieces are left.");

        }
    }
}
