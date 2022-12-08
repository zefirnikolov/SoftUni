using System;

namespace _04.VacationBooksList
{
    class Program
    {
        static void Main(string[] args)
        {
            //1.Брой страници в текущата книга – цяло число в интервала[1...1000]
            //2.Страници, които прочита за 1 час – цяло число в интервала[1...1000]
            //3.Броят на дните, за които трябва да прочете книгата – цяло число в интервала[1...1000]

            int AllCountofPagesInTheCurrentBook = int.Parse(Console.ReadLine());
            int PagesYouCanReadfor1Hour = int.Parse(Console.ReadLine());
            int NumberOfDayForWhichYouHaveToReadTheBook = int.Parse(Console.ReadLine());

            int divideAllPageToPagesYouCanRead = AllCountofPagesInTheCurrentBook / PagesYouCanReadfor1Hour;
            int divideNumberofHoursToAllPagesYouCanRead = divideAllPageToPagesYouCanRead / NumberOfDayForWhichYouHaveToReadTheBook;

            Console.WriteLine(divideNumberofHoursToAllPagesYouCanRead);
        }
    }
}
