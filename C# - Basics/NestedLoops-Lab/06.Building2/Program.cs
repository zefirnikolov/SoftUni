using System;

namespace _06.Building2
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfFloors = int.Parse(Console.ReadLine());
            int numberOfBuildingsOnAFloor = int.Parse(Console.ReadLine());

            for (int i = numberOfFloors; i >= 1; i--)
            {
                for (int j = 0; j < numberOfBuildingsOnAFloor; j++)
                {
                    if (i == numberOfFloors)
                    {
                        Console.Write($"L{i}{j} ");
                    }
                    else if (i % 2 == 0)
                    {
                        Console.Write($"O{i}{j} ");
                    }
                    else
                    {
                        Console.Write($"A{i}{j} ");
                    }                       
                }
                Console.WriteLine(); // Изписваме cw, за да може да прехвърли на нов ред новите данни след като излезе от малкия цикъл.
            }
        }
    }
}
