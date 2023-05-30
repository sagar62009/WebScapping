from bs4 import BeautifulSoup
import requests
import pandas as pd

try:

    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')

    d =[]
    for movie in movies:

        name = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text

        d.append({'Rank':rank, 'Name':name, 'Year':year, 'Rating':rating})  

except Exception as e:
    print(e)

df = pd.DataFrame(d, columns=['Rank','Name','Year','Rating'])
print(df)
# df.to_csv('data.csv', index=False)
fileName = input('Enter file name: ')
saveData = df.to_csv(fileName + '.csv', index=False)