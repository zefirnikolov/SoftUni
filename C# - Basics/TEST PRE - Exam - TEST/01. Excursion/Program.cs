using System;

namespace _01._Excursion
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfPeople = int.Parse(Console.ReadLine());
            int nightstays = int.Parse(Console.ReadLine());
            int cards = int.Parse(Console.ReadLine());
            int museumTickets = int.Parse(Console.ReadLine());

            double nightstay = 20;
            double card = 1.6;
            double museumTicket = 6;

            double sumForNightStays = nightstays * nightstay;
            double sumForTransport = cards * card;
            double sumForMuseums = museumTicket * museumTickets;

            double sumForAllPeople = (sumForTransport + sumForNightStays + sumForMuseums) * numberOfPeople;

            double allExpenses = sumForAllPeople + (sumForAllPeople * 0.25);

            Console.WriteLine($"{allExpenses:f2}");
        }
    }
}
