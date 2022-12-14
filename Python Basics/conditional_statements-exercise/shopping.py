budget = float(input())
gpus_number = int(input())
cpus_number = int(input())
ram_number = int(input())

price_per_gpu = 250
gpus_sum = gpus_number * price_per_gpu
price_per_cpu = gpus_sum * 0.35
price_per_ram = gpus_sum * 0.1

sum_of_all = gpus_sum + price_per_cpu * cpus_number + price_per_ram * ram_number

if gpus_number > cpus_number:
    sum_of_all *= 0.85

difference = abs(budget - sum_of_all)
if budget >= sum_of_all:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
