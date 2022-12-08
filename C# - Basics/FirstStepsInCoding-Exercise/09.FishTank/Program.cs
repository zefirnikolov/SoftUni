using System;

namespace _09.FishTank
{
    class Program
    {
        static void Main(string[] args)
        {
            int lenght = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());
            double percentWaterInTheAquarium = double.Parse(Console.ReadLine());

            double m3oftheAquarium = lenght * width * height;
            double m3inLiters = m3oftheAquarium * 0.001;
            double debugPercent = percentWaterInTheAquarium / 100;

            double litersNeeded = m3inLiters * (1 - debugPercent);

            Console.WriteLine(litersNeeded);


        }
    }
}
