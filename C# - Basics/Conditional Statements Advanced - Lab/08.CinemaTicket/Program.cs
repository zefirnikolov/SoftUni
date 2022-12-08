using System;

namespace _08.CinemaTicket
{
    class Program
    {
        static void Main(string[] args)
        {
            //Monday Tuesday Wednesday Thursday Friday Saturday Sunday
            //12        12      14        14      12      16      16

            string dayOfWeek = Console.ReadLine();

            if (dayOfWeek == "Monday" || dayOfWeek == "Tuesday" || dayOfWeek == "Friday")
            {
                Console.WriteLine("12");
            }
            else if (dayOfWeek == "Wednesday" || dayOfWeek == "Thursday")
            {
                Console.WriteLine("14");
            }
            else if (dayOfWeek == "Saturday" || dayOfWeek == "Sunday")
            {
                Console.WriteLine("16");
            }
            else
            {
                Console.WriteLine("N/A");
            }
        }
    }
}
