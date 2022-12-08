using System;

namespace _06.VowelsSum
{
    class Program
    {
        static void Main(string[] args)
        {

            //буква    a  e  i  o  u
            //стойност 1  2  3  4  5


            string word = Console.ReadLine();
            int wordLenght = word.Length;
            int sum = 0;

            for (int i = 0; i < wordLenght; i++)
            {
                char letter = word[i];

                switch (letter)
                {
                    case 'a':
                        sum++;
                        break;
                    case 'e':
                        sum += 2;
                        break;
                    case 'i':
                        sum += 3;
                        break;
                    case 'o':
                        sum += 4;
                        break;
                    case 'u':
                        sum += 5;
                        break;

                }               
            }
            Console.WriteLine(sum);
        }
    }
}
