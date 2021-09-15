import requests 
from bs4 import BeautifulSoup

empire = "https://www.empireonline.com/movies/features/best-movies-2"

response = requests.get(url=empire)
# print(response.text)

soap = BeautifulSoup(response.text, "html.parser")
print(soap.prettify())

# print(soap.find_all(name="h3", class_="jsx-4245974604"))
# class="jsx-4245974604"

# <h3 class="jsx-4245974604">100) Stand By Me</h3>
# https://www.empireonline.com/movies/features/best-movies-2/