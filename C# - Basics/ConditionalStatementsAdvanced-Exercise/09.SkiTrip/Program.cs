using System;

namespace _09.SkiTrip
{
    class Program
    {
        static void Main(string[] args)
        {
            //▪ "room for one person" – 18.00 лв за нощувка
            //▪ "apartment" – 25.00 лв за нощувка
            //▪ "president apartment" – 35.00 лв за нощувка
            //Трети ред -оценка - "positive" или "negative"


            int numberOfDayForTrip = int.Parse(Console.ReadLine());
            string typeOfRoom = Console.ReadLine();
            string assessment = Console.ReadLine();

            double numberOfNightsForTheTrip = numberOfDayForTrip - 1;
            double priceForRoomFor1Night = 0;

            if (typeOfRoom == "room for one person")
            {
                priceForRoomFor1Night = 18;
                
            }
            else if (typeOfRoom == "apartment")
            {
                priceForRoomFor1Night = 25;
               if (numberOfDayForTrip <= 9)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.3;
                }
               else if (numberOfDayForTrip > 9 && numberOfDayForTrip <= 14)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.35;
                }
               else if (numberOfDayForTrip > 14)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.5;
                }
              
            }
            else if (typeOfRoom == "president apartment")
            {
                priceForRoomFor1Night = 35;
                if (numberOfDayForTrip <= 9)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.1;
                }
                else if (numberOfDayForTrip > 9 && numberOfDayForTrip <= 14)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.15;
                }
                else if (numberOfDayForTrip > 14)
                {
                    priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.2;
                }
               
            }
 
            

            if (assessment == "positive")
            {
                priceForRoomFor1Night = priceForRoomFor1Night + priceForRoomFor1Night * 0.25;
            }
            else if (assessment == "negative")
            {
                priceForRoomFor1Night = priceForRoomFor1Night - priceForRoomFor1Night * 0.1;
            }

            double finalPrice = numberOfNightsForTheTrip * priceForRoomFor1Night;

            Console.WriteLine($"{finalPrice:f2}");
        }
    }
}
