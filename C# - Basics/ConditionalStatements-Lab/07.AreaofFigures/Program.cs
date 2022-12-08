using System;

namespace _07.AreaofFigures
{
    class Program
    {
        static void Main(string[] args)
        {

            //• Ако фигурата е квадрат(square): на следващия ред се чете едно дробно число -дължина на
            //страната му
            //• Ако фигурата е правоъгълник(rectangle): на следващите два реда четат две дробни числа -
            //дължините на страните му
            //• Ако фигурата е кръг(circle): на следващия ред чете едно дробно число - радиусът на кръга
            //• Ако фигурата е триъгълник(triangle): на следващите два реда четат две дробни числа -дължината
            //на страната му и дължината на височината към нея
            //Резултатът да се закръгли до 3 цифри след десетичната запетая.

            string figureName = Console.ReadLine();

            if (figureName == "square")
            {
                double side = double.Parse(Console.ReadLine());
                double area = side * side;
                Console.WriteLine($"{area:f3}");
            }
            else if (figureName == "rectangle")
            {
                double side1 = double.Parse(Console.ReadLine());
                double side2 = double.Parse(Console.ReadLine());
                double area = side1 * side2;
                Console.WriteLine($"{area:f3}");
            }
            else if (figureName == "circle")
            {
                double radius = double.Parse(Console.ReadLine());
                double area = radius * radius * Math.PI;
                Console.WriteLine($"{area:f3}");
            }
            else if (figureName == "triangle")
            {
                double side1 = double.Parse(Console.ReadLine());
                double side2 = double.Parse(Console.ReadLine());
                double area = side1 * side2 / 2;
                Console.WriteLine($"{area:f3}");
            }
        }
    }
}
