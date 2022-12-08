using System;

namespace _05.Travelling
{
    class Program
    {
        static void Main(string[] args)
        {
            string destination = Console.ReadLine();


            while (destination != "End")
            {
                double sumForDestination = double.Parse(Console.ReadLine());
                
                double budget = 0;
                while (budget < sumForDestination)
                {
                    double sumAddedToBudget = double.Parse(Console.ReadLine());
                    budget += sumAddedToBudget;
                }
 
                if (budget >= sumForDestination)
                {
                    Console.WriteLine($"Going to {destination}!");
                }
                destination = Console.ReadLine();
            }
        }
    }
}
