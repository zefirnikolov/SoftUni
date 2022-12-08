﻿using System;

namespace _05.Coins
{
    class Program
    {
        static void Main(string[] args)
        {
            double input = double.Parse(Console.ReadLine());
            double change = Math.Floor(input * 100);


            int coinsCounter = 0;

            while (change != 0)
            {
                if (change - 200 >= 0)
                {
                    change -= 200;
                    coinsCounter++;
                }
                else if (change - 100 >= 0)
                {
                    change -= 100;
                    coinsCounter++;
                }
                else if (change - 50 >= 0)
                {
                    change -= 50;
                    coinsCounter++;
                }
                else if (change - 20 >= 0)
                {
                    change -= 20;
                    coinsCounter++;
                }
                else if (change - 10 >= 0)
                {
                    change -= 10;
                    coinsCounter++;
                }
                else if (change - 5 >= 0)
                {
                    change -= 5;
                    coinsCounter++;
                }
                else if (change - 2 >= 0)
                {
                    change -= 2;
                    coinsCounter++;
                }
                else if (change - 1 >= 0)
                {
                    change -= 1;
                    coinsCounter++;
                }
                else if (change < 0.01)
                {
                    break;
                }
            }
            Console.WriteLine(coinsCounter);
        }
    }
}
