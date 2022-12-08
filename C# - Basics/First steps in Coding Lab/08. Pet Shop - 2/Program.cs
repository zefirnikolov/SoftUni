using System;

namespace _08._Pet_Shop
{
    class Program
    {
        static void Main(string[] args)
        {
            int dogFood = int.Parse(Console.ReadLine());
            int CatFood = int.Parse(Console.ReadLine());
            double PricePer1DogFood = 2.50;
            double PricePer1CatFood = 4;
            double MultipleAndSum = (dogFood * PricePer1DogFood) + (CatFood * PricePer1CatFood);
            Console.WriteLine($"{MultipleAndSum} lv.");     
        }
    }
}
