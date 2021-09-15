import requests 
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")

ycombinator_contents = response.text

# <a href="https://www.replay.io/" class="storylink">Show HN: Time Travel Debugger</a>
# <span class="score" id="score_28539247">205 points</span>

soup = BeautifulSoup(ycombinator_contents, "html.parser")
# print(soup.find_all(name="span", class_="score"))
# print(soup.find_all(name="td", class_="title"))

# Nandisha finding
# all_titles = soup.select(selector=".storylink")
# for title in all_titles:
#     # print(title.text)
#     print(title.getText())    # Show HN: Time Travel Debugger
#     print(title.get("href"))  # 
#     print(soup.find_all(name="span", class_="score").getText())

all_titles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for title in all_titles:
    article_texts.append(title.getText())
    article_links.append(title.get("href"))

article_score = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")] 
# BUG: If any non scored title then you will get  wrong results

largest_number = max(article_score)
largest_index = article_score.index(largest_number)

largest_text = article_texts[largest_index]
largest_link = article_links[largest_index]

print(largest_number)
print(largest_index)
print(largest_text)