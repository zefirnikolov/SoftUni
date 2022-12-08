using System;

namespace _01.OldBooks
{
    class Program
    {
        static void Main(string[] args)
        {
            string book = Console.ReadLine();

            int bookCounter = 0;

            while (book != "No More Books")
            {

                string bookCheck = Console.ReadLine();

                if (bookCheck == book)
                {
                    Console.WriteLine($"You checked {bookCounter} books and found it.");
                    break;
                }
                
                if (bookCheck == "No More Books")
                {
                    Console.WriteLine($"The book you search is not here!");
                    Console.WriteLine($"You checked {bookCounter} books.");
                    break;
                }
                bookCounter++;
            }
            
        }
    }
}
