using System;

namespace _04.Cinema
{
    class Program
    {
        static void Main(string[] args)
        {
            int capacityOfTheCinema = int.Parse(Console.ReadLine());

            int counterOfPeople = 0;
            double priceOfOneTicket = 5;
            double sumOfAllTickets = 0;
            double priceReduction = 0;

            string numberOfPeopleUntilStop = Console.ReadLine();
            while (numberOfPeopleUntilStop != "Movie time!")
            {
                int peopleComingParsed = int.Parse(numberOfPeopleUntilStop);

                counterOfPeople += peopleComingParsed;

                
                if (counterOfPeople > capacityOfTheCinema)
                {
                    Console.WriteLine($"The cinema is full.");
                    sumOfAllTickets = (counterOfPeople  - peopleComingParsed ) * priceOfOneTicket + priceReduction;
                    Console.WriteLine($"Cinema income - {sumOfAllTickets} lv.");
                    break;
                }
                if (peopleComingParsed % 3 == 0)
                {
                    priceReduction -= 5;
                }
                numberOfPeopleUntilStop = Console.ReadLine();
            }
            sumOfAllTickets = counterOfPeople * priceOfOneTicket + priceReduction;
            if (counterOfPeople <= capacityOfTheCinema)
            {
                Console.WriteLine($"There are {capacityOfTheCinema - counterOfPeople} seats left in the cinema.");
                Console.WriteLine($"Cinema income - {sumOfAllTickets} lv.");
            }           
        }
    }
}
