countries = 'country_info.txt'

country_capitals = {}
with open(countries) as countryInfo:
    countryInfo.readline()    # readline will automatically moves to next line so for loop will start from next line
    for row in countryInfo:
        data = row.strip('\n').split('|')
        country, capital, code, code3, iac, tz, currency = data
        # print(country, capital, cc, cc3, iac, tz, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'cc': code,
            'cc3': code3,
            'dialing_code': iac,
            'timezone': tz,
            'currency': currency
        }
        # print(country_dict)
        country_capitals[country.casefold()] = country_dict
        country_capitals[code.casefold()] = country_dict

print(country_capitals)


while True:
    country_name = input("please enter a country name: ").casefold()
    if country_name in country_capitals:
        country_data = country_capitals[country_name]
        print(f"Capital of {country_name} is {country_data['capital']}")
    elif country_name == 'quit':
        break
