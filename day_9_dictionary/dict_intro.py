vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R100',
    'er5': 'kawasaki er5',
    'can-am': 'bombardier can-am 250',
    'virago': 'yamaha xv 250',
    'tenere': 'yamaha xt650',
    'jimmy': 'suzuki jimmy 1.5',
    'fiesta': 'ford fiesta ghia 1.4',
}

# my_car = vehicles['fiesta']
# print(my_car)

# for key in vehicles:
#     print(key)
# for key in vehicles:
#     print(key, vehicles[key], sep=':')

vehicles['starfighter'] = 'lockheed F-104'
vehicles['toy'] = 'glider'

# upgrade the virago
vehicles['virago'] = 'yamaha xv535'

vehicles.pop('virago')

for key, value in vehicles.items():
    print(key, value, sep=':')