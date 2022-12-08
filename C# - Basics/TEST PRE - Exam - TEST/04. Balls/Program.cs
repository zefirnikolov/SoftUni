using System;

namespace _04._Balls
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ако топката е “red” точките ни се повишават с 5.
            // Ако топката е “orange” точките ни се повишават с 10.
            // Ако топката е “yellow” точките ни се повишават с 15.
            // Ако топката е “white” точките ни се повишават с 20.
            // Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.

            int BallsEqLoops = int.Parse(Console.ReadLine());


            double points = 0;
            int redBalls = 0;
            int orangeBalls = 0;
            int yellowBalls = 0;
            int whiteBalls = 0;
            int otherColorBalls = 0;
            int divideFromBlackBalls = 0;


            for (int i = 1; i <= BallsEqLoops; i++)
            {
                string colors = Console.ReadLine();

                if (colors == "red")
                {
                    points += 5;
                    redBalls++;
                }
                else if (colors == "orange")
                {
                    points += 10;
                    orangeBalls++;
                }
                else if (colors == "yellow")
                {
                    points += 15;
                    yellowBalls++;
                }
                else if (colors == "white")
                {
                    points += 20;
                    whiteBalls++;
                }
                else if (colors == "black")
                {
                    points /= 2;                   
                    divideFromBlackBalls++;
                }
                else
                {
                    otherColorBalls++;
                }
            }
            Console.WriteLine($"Total points: {Math.Floor(points)}");
            Console.WriteLine($"Red balls: {redBalls}");
            Console.WriteLine($"Orange balls: {orangeBalls}");
            Console.WriteLine($"Yellow balls: {yellowBalls}");
            Console.WriteLine($"White balls: {whiteBalls}");
            Console.WriteLine($"Other colors picked: {otherColorBalls}");
            Console.WriteLine($"Divides from black balls: {divideFromBlackBalls}");


        }
    }
}
