using System;

namespace _04.PasswordGuess
{
    class Program
    {
        static void Main(string[] args)
        {
            const string TRUE_PASSWORD = "s3cr3t!P@ssw0rd";

            string passwordEntered = Console.ReadLine();
            bool isThisTheTruePassword = passwordEntered == TRUE_PASSWORD;

            if (isThisTheTruePassword)
            {
                Console.WriteLine("Welcome");
            }
            else
            {
                Console.WriteLine("Wrong password!");
            }
        }
    }
}
