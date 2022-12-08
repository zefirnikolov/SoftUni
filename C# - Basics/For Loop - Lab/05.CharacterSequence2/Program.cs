using System;

namespace _05.CharacterSequence2
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();
            int wordLenght = word.Length;

            for (int i = 0; i < wordLenght; i++)
            {

                char letter = word[i];
                Console.WriteLine(letter);

            }
        }
    }
}
