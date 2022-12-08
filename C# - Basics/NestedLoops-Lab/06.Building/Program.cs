using System;

namespace _06.Building
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfFloors = int.Parse(Console.ReadLine());
            int numberOfBuildingsOnAFloor = int.Parse(Console.ReadLine());

            int highestFloorEqCounter = 0;
             
            for (int i = numberOfFloors; i >= 1; i--)
            {
                highestFloorEqCounter++;
                
                for (int j = 0; j < numberOfBuildingsOnAFloor; j++)
                {
                    if (highestFloorEqCounter != 1 && i % 2 == 0)
                    {
                        if (j == 0)
                        {
                            Console.Write($"\r\nO{i}{j} ");
                        }
                        else
                        {
                            Console.Write($"O{i}{j} ");
                        }
                    }
                    else if (highestFloorEqCounter != 1 && i % 2 == 1)
                    {
                        if (j == 0)
                        {
                            Console.Write($"\r\nA{i}{j} ");
                        }
                        else
                        {
                            Console.Write($"A{i}{j} ");
                        }
                    }
                    if (highestFloorEqCounter == 1)
                    {
                        Console.Write($"L{i}{j} ");
                    }
                }
            }
        }
    }
}
