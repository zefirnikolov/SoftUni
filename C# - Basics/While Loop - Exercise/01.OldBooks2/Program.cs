using System;

namespace _01.OldBooks2
{
    class Program
    {
        static void Main(string[] args)
        {
            string favoriteBook = Console.ReadLine();
            string bookCheck = Console.ReadLine();
            int bookCounter = 0;

            while (favoriteBook != bookCheck)
            {

                if (bookCheck == "No More Books")
                {
                    Console.WriteLine($"The book you search is not here!");
                    Console.WriteLine($"You checked {bookCounter} books.");
                    break;
                }

                bookCounter++;
                bookCheck = Console.ReadLine();
            }
           
            if (favoriteBook == bookCheck)
            {
                Console.WriteLine($"You checked {bookCounter} books and found it.");
            }
        }
    }
}
