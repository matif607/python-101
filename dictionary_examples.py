travel_log_a = {
    "France": {"cities_visted": ["paris", "Dijon", "Bordeux", "Lyon"]},
    "India": {"cites_visted": ["Delhi", "Pune", "Mumbai", "Chennai", "bangalore", "Aligarh"]},
    "Spain": {"cities_visited": ["Madrid", "barcelona", "seville"]},
}

for countries in travel_log_a:
    print(countries[2])
print(travel_log_a["France"])


vlog = [
  {
      "Countries_visited": "France",
      "Cities_visited": ["paris", "lyon", "bordeaux"],
      "no. of visites": 10
  },
  {
     "Countries_visited": "India",
      "Cities_visited": ["Pune", "Mumbai", "Chennai"],
      "no. of visites": 20 
  },  
]


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# def add_new_country(country, visits, cities):
#     new_country = {}
#     new_country["country"] = name_of_country
#     new_country["visits"] = no._of_visits
#     new_country["cities"] = name_of_cities_visited
#     travel_log.append(new_country)

def add_new_country(name_of_country, no_of_visits, cities_visited):
    new_country = {}
    new_country["country"] = name_of_country
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Kremlin", "crimea"])
add_new_country("India", 4, ["Chennai", "Pune", "Mumbai"])
print(travel_log)