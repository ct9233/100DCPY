from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to retrieve music from? \nEnter date in the format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
