from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
response.raise_for_status()

movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")

tags_list = soup.find_all(name="h3", class_="card-title")
movie_list = [(item.getText()) for item in tags_list]

ranking_list = ''

for movie in movie_list:
    movie_rank = movie.strip()
    if movie_rank[0] != "C":
        ranking_list += f"{movie_rank} \n"

with open("movies.txt", "w", encoding="utf-16") as file:
    file.write(ranking_list)



