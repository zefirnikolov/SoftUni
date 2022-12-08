using System;

namespace _06.CinemaTickets
{
    class Program
    {
        static void Main(string[] args)
        {
            string movieName = Console.ReadLine();



            double totalTickets = 0;
            double studentTickets = 0;
            double standardTickets = 0;
            double kidTickets = 0;

            while (movieName != "Finish")
            {
                int maxNumberOfTickets = int.Parse(Console.ReadLine());
                string typeOfTicket = Console.ReadLine();
                double counterForAMovie = 0;

                while (typeOfTicket != "End")
                {
                    if (typeOfTicket == "student")
                    {
                        studentTickets++;
                    }
                    else if (typeOfTicket == "standard")
                    {
                        standardTickets++;
                    }
                    else if (typeOfTicket == "kid")
                    {
                        kidTickets++;
                    }
                    counterForAMovie++;

                    if (counterForAMovie == maxNumberOfTickets)
                    {
                        break;
                    }                    
                    typeOfTicket = Console.ReadLine();                   
                }


                totalTickets = studentTickets + standardTickets + kidTickets;
                Console.WriteLine($"{movieName} - {(counterForAMovie / maxNumberOfTickets * 100 * 1.00):f2}% full.");
                movieName = Console.ReadLine();
            }
            Console.WriteLine($"Total tickets: {totalTickets}");
            Console.WriteLine($"{(studentTickets / totalTickets * 100 * 1.00):f2}% student tickets.");
            Console.WriteLine($"{(standardTickets / totalTickets * 100 * 1.00):f2}% standard tickets.");
            Console.WriteLine($"{(kidTickets / totalTickets * 100 * 1.00):f2}% kids tickets.");
        }
    }
}
