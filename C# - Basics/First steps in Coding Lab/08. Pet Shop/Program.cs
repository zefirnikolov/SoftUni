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
            double DogFoodXPricePer1DogFood = dogFood * PricePer1DogFood;
            double CatFoodXPricePer1CatFood = CatFood * PricePer1CatFood;
            double MultipleOfAll = DogFoodXPricePer1DogFood + CatFoodXPricePer1CatFood;
            Console.WriteLine($"{MultipleOfAll} lv.");
        }
    }
}
