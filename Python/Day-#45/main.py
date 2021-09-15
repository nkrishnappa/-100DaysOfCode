from bs4 import BeautifulSoup

website_path = "website.html"
with open(website_path, "r", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title) # <title>Nandisha Personal Site</title>
print(soup.title.name) # title
print(soup.title.string) # Nandisha Personal Site

print(soup.prettify()) 

print(f"First Anchor Tag : {soup.a}") 
# First Anchor Tag : <a href="https://www.nothing.com">Nothing</a>

print(f"All of the Anchor Tags:\n {soup.find_all(name='a')}")
#  [<a href="https://www.nothing.com">Nothing</a>, <a href="https://www.linkedin.com/in/nandishakrishnappa/">LinkedIn</a>, <a href="https://twitter.com/NandishKrishna3">Twitter</a>, <a href="https://github.com/nkrishnappa">Github</a>, <a href="mailto:nandisha111@gmail.com">CONTACT ME</a>]

print(f"All of the Anchor Tags:\n {soup.find_all(name='p')}")
#  [<p><em>Founder of <strong><a href="https://www.nothing.com">Nothing</a></strong>.</em></p>, <p>I am a Software Developer. I ❤️ food.</p>]

for tag in soup.find_all(name='a'):
    print(tag.getText())
    # Nothing
    # LinkedIn
    # Twitter
    # Github
    # CONTACT ME
    print(tag.get("href"))
    # https://www.nothing.com
    # https://www.linkedin.com/in/nandishakrishnappa/
    # https://twitter.com/NandishKrishna3
    # https://github.com/nkrishnappa
    # mailto:nandisha111@gmail.com

print(soup.find(name="h3", class_="heading"))
# <h3 class="heading">Skills</h3>

company_url = soup.select_one(selector="p a")
print(company_url)
# <a href="https://www.nothing.com">Nothing</a>

name = soup.select_one(selector="#name")
print(name)
# <h1 id="name">Nandisha Krishnappa</h1>

name = soup.select(selector="#name")
print(name)
# [<h1 id="name">Nandisha Krishnappa</h1>]

heading = soup.select(".heading")
print(heading)
# [<h3 class="heading">Skills</h3>, <h3 class="heading">Other Pages</h3>]

heading = soup.find_all(name="h3")
print(heading)