countries = input().split(", ")
capitals = input().split(", ")
capitals_dict = {countries[index]: capitals[index] for index in range(len(countries))}
# capitals_dict = dict(zip(countries, capitals))
for key, value in capitals_dict.items():
    print(f"{key} -> {value}")
