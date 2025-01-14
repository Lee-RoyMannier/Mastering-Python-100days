from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = [movie.getText() for movie in soup.find_all("h3", class_="title")][::-1]

with open("movies.text","a") as file:
    for movie in movies:
        file.write(movie+"\n")
