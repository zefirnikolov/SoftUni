using System;

namespace _03.NewHouse
{
    class Program
    {
        static void Main(string[] args)
        {



            //ВЯРНО РЕШЕНИЕ - ЗАДЪЛЖИТЕЛНО ГЛЕДАЙ ПО-МАЛКО ИЛИ РАВНО!!!! ТРЯБВА ЗАДЪЛЖИТЕЛНО ДА ГЛЕДАШ УСЛОВИЕТО И ПО-ГОЛЯМО ИЛИ РАВНО
            // ПРАВИШ МНОГО ГРЕШКИ НА ПО-ГОЛЯМО ИЛИ РАВНО ИЛИ САМО ПО-ГОЛЯМО!!!!!
            


            //цвете                 "Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
            //Цена на брой в лева       5       3.80       2.80        3           2.50
            //Съществуват следните отстъпки:
            //• Ако Нели купи повече от 80 Рози - 10 % отстъпка от крайната цена
            //• Ако Нели купи повече от 90 Далии - 15 % отстъпка от крайната цена
            //• Ако Нели купи повече от 80 Лалета - 15 % отстъпка от крайната цена
            //• Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15 %
            //• Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20 %

            

            string flower = Console.ReadLine();
            int numberOfFlowers = int.Parse(Console.ReadLine());
            int budget = int.Parse(Console.ReadLine());

            

            double priceForRoses = 5;
            double priceForDahlias = 3.8;
            double priceForTulips = 2.8;
            double priceForNarcissus = 3;
            double priceForGladiolus = 2.5;

            double priceForAllFlowers = 0;

            switch (flower)
            {
                case "Roses":
                    if (numberOfFlowers > 80)
                    {
                        priceForAllFlowers = (priceForRoses * numberOfFlowers) - (priceForRoses * numberOfFlowers * 0.1);
                    }
                    else
                    {
                        priceForAllFlowers = priceForRoses * numberOfFlowers;
                    }
                    break;
                case "Dahlias":
                    if (numberOfFlowers > 90)
                    {
                        priceForAllFlowers = (priceForDahlias * numberOfFlowers) - (priceForDahlias * numberOfFlowers * 0.15);
                    }
                    else
                    {
                        priceForAllFlowers = (priceForDahlias * numberOfFlowers);
                    }
                    break;
                case "Tulips":
                    if (numberOfFlowers > 80)
                    {
                        priceForAllFlowers = (priceForTulips * numberOfFlowers) - (priceForTulips * numberOfFlowers * 0.15);
                    }
                    else
                    {
                        priceForAllFlowers = priceForTulips * numberOfFlowers;
                    }
                    break;
                case "Narcissus":
                    if (numberOfFlowers < 120)
                    {
                        priceForAllFlowers = (priceForNarcissus * numberOfFlowers) + (priceForNarcissus * numberOfFlowers * 0.15);
                    }
                    else
                    {
                        priceForAllFlowers = priceForNarcissus * numberOfFlowers;
                    }
                    break;
                case "Gladiolus":
                    if (numberOfFlowers < 80)
                    {
                        priceForAllFlowers = (priceForGladiolus * numberOfFlowers) + (priceForGladiolus * numberOfFlowers * 0.2);
                    }
                    else
                    {
                        priceForAllFlowers = priceForGladiolus * numberOfFlowers;
                    }
                    break;

            }

            bool isTheBudgeEnough = budget >= priceForAllFlowers;



            if (isTheBudgeEnough)
            {
                Console.WriteLine($"Hey, you have a great garden with {numberOfFlowers} {flower} and {(budget - priceForAllFlowers):f2} leva left.");
            }
            else
            {
                Console.WriteLine($"Not enough money, you need {(priceForAllFlowers - budget):f2} leva more.");
            }



        }
    }
}
