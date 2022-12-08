using System;

namespace _07.TrekkingMania
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfGroups = int.Parse(Console.ReadLine());

            int sumOfAllpeople = 0;
            int musala = 0;
            int monblan = 0;
            int kilimanjaro = 0;
            int k2 = 0;
            int everest = 0; 

            for (int i = 1; i <= numberOfGroups; i++)
            {

                //• Група до 5 човека – изкачват Мусала
                //• Група от 6 до 12 човека – изкачват Монблан
                //• Група от 13 до 25 човека – изкачват Килиманджаро
                //• Група от 26 до 40 човека – изкачват К2
                //• Група от 41 или повече човека – изкачват Еверест

                int numberOfPeopleInAGroup = int.Parse(Console.ReadLine());

                sumOfAllpeople += numberOfPeopleInAGroup;

                if (numberOfPeopleInAGroup <= 5)
                {
                    musala += numberOfPeopleInAGroup;
                }
                else if (numberOfPeopleInAGroup >= 6 && numberOfPeopleInAGroup <= 12)
                {
                    monblan += numberOfPeopleInAGroup;
                }
                else if (numberOfPeopleInAGroup >= 13 && numberOfPeopleInAGroup <= 25)
                {
                    kilimanjaro += numberOfPeopleInAGroup;
                }
                else if (numberOfPeopleInAGroup >= 26 && numberOfPeopleInAGroup <= 40)
                {
                    k2 += numberOfPeopleInAGroup;
                }
                else if (numberOfPeopleInAGroup >= 41)
                {
                    everest += numberOfPeopleInAGroup;
                }
                

            }
            double percentMusala = musala * 1.0 / sumOfAllpeople * 100;
            double percentMonblan = monblan * 1.0 / sumOfAllpeople * 100;
            double percentKilimanjaro = kilimanjaro * 1.0 / sumOfAllpeople * 100;
            double percentK2 = k2 * 1.0 / sumOfAllpeople * 100;
            double percentEverest = everest * 1.0 / sumOfAllpeople * 100;

            Console.WriteLine($"{percentMusala:f2}%");
            Console.WriteLine($"{percentMonblan:f2}%");
            Console.WriteLine($"{percentKilimanjaro:f2}%");
            Console.WriteLine($"{percentK2:f2}%");
            Console.WriteLine($"{percentEverest:f2}%");
        }
    }
}
