using System;

namespace _03._World_Snooker_Championship
{
    class Program
    {
        static void Main(string[] args)
        {
            //               Четвъртфинал      Полуфинал        Финал
            //Стандартен     55.50 £/ бр.      75.88 £/ бр.     110.10 £/ бр.
            //Премиум        105.20 £/ бр.     125.22 £/ бр.    160.66 £/ бр.
            //ВИП            118.90 £/ бр.     300.40 £/ бр.    400 £/ бр.

            string phaseOfTheChampionship = Console.ReadLine();
            string typeOfTheTickets = Console.ReadLine();
            int numberOfTickets = int.Parse(Console.ReadLine());

            char pictureWithTheThrophy = char.Parse(Console.ReadLine());

            double priceOfTheTickets = 0;

            switch (typeOfTheTickets)
            {
                case "Standard":
                    if (phaseOfTheChampionship == "Quarter final")
                    {
                        priceOfTheTickets = numberOfTickets * 55.50;
                    }
                    else if (phaseOfTheChampionship == "Semi final")
                    {
                        priceOfTheTickets = numberOfTickets * 75.88;
                    }
                    else if (phaseOfTheChampionship == "Final")
                    {
                        priceOfTheTickets = numberOfTickets * 110.1;
                    }
                    break;
                case "Premium":
                    if (phaseOfTheChampionship == "Quarter final")
                    {
                        priceOfTheTickets = numberOfTickets * 105.2;
                    }
                    else if (phaseOfTheChampionship == "Semi final")
                    {
                        priceOfTheTickets = numberOfTickets * 125.22;
                    }
                    else if (phaseOfTheChampionship == "Final")
                    {
                        priceOfTheTickets = numberOfTickets * 160.66;
                    }
                    break;
                case "VIP":
                    if (phaseOfTheChampionship == "Quarter final")
                    {
                        priceOfTheTickets = numberOfTickets * 118.90;
                    }
                    else if (phaseOfTheChampionship == "Semi final")
                    {
                        priceOfTheTickets = numberOfTickets * 300.40;
                    }
                    else if (phaseOfTheChampionship == "Final")
                    {
                        priceOfTheTickets = numberOfTickets * 400;
                    }
                    break;
            }


            if (priceOfTheTickets > 4000)
            {
                priceOfTheTickets = priceOfTheTickets - priceOfTheTickets * 0.25;
            }
            else if (priceOfTheTickets > 2500 && priceOfTheTickets <= 4000)
            {
                priceOfTheTickets = priceOfTheTickets - priceOfTheTickets * 0.1;
            }

            if (pictureWithTheThrophy == 'Y' && priceOfTheTickets <= 4000)
            {
                priceOfTheTickets = priceOfTheTickets + (numberOfTickets * 40);
            }
            else if (pictureWithTheThrophy == 'N')
            {

            }



            Console.WriteLine($"{priceOfTheTickets:f2}");


        }
    }
}
