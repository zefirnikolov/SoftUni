using System;

namespace _05.Salary
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfTabsEqLoops = int.Parse(Console.ReadLine());
            int salary = int.Parse(Console.ReadLine());
            

    


            for (int i = 1; i <= numberOfTabsEqLoops; i++)
            {

                string website = Console.ReadLine();
                if (website == "Facebook")
                {
                    salary -= 150;
                }
                else if (website == "Instagram")
                {
                    salary -= 100;
                }
                else if (website == "Reddit")
                {
                    salary -= 50;
                }
                bool isTheSalaryEnough = salary <= 0;

                if (isTheSalaryEnough)
                {
                    Console.WriteLine("You have lost your salary.");
                    break;
                }
            }
            bool isTheSalaryPositive = salary > 0;

            if (isTheSalaryPositive)
            {
                Console.WriteLine(salary);
            }
        }
    }
}
