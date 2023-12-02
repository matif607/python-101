import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data)

avg_temp = data['temp'].mean()
print(avg_temp)

max_num = data['temp'].max()
print(max_num)

print(data[data.day == 'Monday'])
print(data[data['day'] == 'Monday'])

print(data[data.temp == data.temp.max()])

mon_temp = data.temp[0]
mon_temp_f = mon_temp * 9 / 5 + 32
print(mon_temp_f)

data_dict = {
    'student': ['Atif', 'Anas', 'Sana'],
    'Score': [99, 90, 30]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv('new_data.csv')

# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # for row in data:
#     #     print(row)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
