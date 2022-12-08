using System;

namespace _06.BarcodeGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1 = int.Parse(Console.ReadLine()); //2345
            int num2 = int.Parse(Console.ReadLine());   //6789

            for (int b1 = num1 / 1000; b1 <= num2 / 1000; b1++)
            {// 2345 / 1000 = 2;       6789 / 1000 = 6;  ---> 2 <= 6 проверяваме 1вите числа.

                if (b1 % 2 == 0)
                {
                    continue;
                }

                for (int b2 = num1 / 100 % 10; b2 <= num2 / 100 % 10; b2++)
                {// 2345 / 100 % 10 = 3;       6789 / 100 % 10 = 7;  ---> 3 <= 7 проверяваме 2рите числа.
                    if (b2 % 2 == 0)
                    {
                        continue;
                    }

                    for (int b3 = num1 / 10 % 10 ; b3 <= num2 / 10 % 10; b3++)
                    {// 2345 / 10 % 10 = 4;       6789 / 10 % 10= 8;  ---> 4 <= 8 проверяваме 3тите числа.
                        if (b3 % 2 == 0)
                        {
                            continue;
                        }

                        for (int b4 = num1 % 10; b4 <= num2 % 10; b4++)
                        {//Със % 10 се намира последното число от всяка цифра. 

                            if (b4 % 2 == 0)
                            {
                                continue;

                            }
                            Console.Write($"{b1}{b2}{b3}{b4} ");
                        }
                    }
                }
            }
        }
    }
}
