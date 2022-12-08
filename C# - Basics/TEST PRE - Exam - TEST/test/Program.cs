using System;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                string name = Console.ReadLine();

                if (name == "stop")
                {
                    break;
                }

                switch (name)
                {
                    case "Pesho":
                        Console.WriteLine("Ok");
                        break;
                    case "Pepi":
                        Console.WriteLine("GG");
                        break;
                    case "Cocolino":
                        Console.WriteLine("Ok again");
                        break;
                    default:
                        Console.WriteLine("nothing");
                        break;
                }
            }
            Console.WriteLine("Out of the while loop");

            string test = "This is 'example'";
            Console.WriteLine(test);
        }
    }
}
