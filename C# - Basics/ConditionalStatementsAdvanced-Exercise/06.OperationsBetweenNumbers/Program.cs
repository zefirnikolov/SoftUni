using System;

namespace _06.OperationsBetweenNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = int.Parse(Console.ReadLine());
            int n2 = int.Parse(Console.ReadLine());
            char op = char.Parse(Console.ReadLine());

            double result = 0;

            switch (op)
            {
                case '+':
                    result = n1 + n2;
                    Console.Write($"{n1} + {n2} = {result}");
                    break;
                case '-':
                    result = n1 - n2;
                    Console.Write($"{n1} - {n2} = {result}");
                    break;
                case '*':
                    result = n1 * n2;
                    Console.Write($"{n1} * {n2} = {result}");
                    break;
                case '/':
                    if (n2 == 0)
                    {
                        Console.WriteLine($"Cannot divide {n1} by zero");
                    }
                    else
                    {
                        result = (double)n1 / n2;
                        Console.WriteLine($"{n1} / {n2} = {result:f2}");
                    }
                    break;
                case '%':
                    if (n2 != 0)
                    {
                        result = n1 % n2;
                        Console.WriteLine($"{n1} % {n2} = {result}");
                    }
                    else
                    {                     
                        Console.WriteLine($"Cannot divide {n1} by zero");
                    }
                    break;
            }
            if (op == '+' || op == '-' || op == '*')
            {
                if (result % 2 == 0)
                {
                    Console.WriteLine(" - even");
                }
                else
                {
                    Console.WriteLine(" - odd");
                }
                   
            }

        }
    }
}

