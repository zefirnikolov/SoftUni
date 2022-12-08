using System;

namespace _05.CharacterSequence
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();

            for (int i = 0; i < text.Length; i++)
            {
                char letter = text[i];  // В Python char letter може да започва от индекс -1, което ще бъде последната, тук не може! 
                Console.WriteLine(letter);
            }
        }
    }
}
