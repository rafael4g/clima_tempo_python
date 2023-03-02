import pandas as pd
#df = pd.read_json(r'./weather_16.json')

#print(df.head())

df = pd.read_json (r'./city.list.json')

df_filter = df[(df['country'] == 'BR')]

df_filter.to_csv('openweathermaplistcity.csv', sep=';', encoding='utf-8', index=None)

print('OK---------')


