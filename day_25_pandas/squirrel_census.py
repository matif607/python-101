import pandas as pd

squirrel = pd.read_csv('2018_cp_squirrel_count.csv')

gray_squirrels = len(squirrel[squirrel['Primary Fur Color'] == 'Gray'])
red_squirrels = len(squirrel[squirrel['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(squirrel[squirrel['Primary Fur Color'] == 'Black'])
print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

squirrel_count = {
    'Primary Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels, red_squirrels, black_squirrels]
}

df = pd.DataFrame(squirrel_count)

df.to_csv('squirreL_color_census.csv')
