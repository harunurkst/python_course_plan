from bs4 import BeautifulSoup

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, "lxml")

headline = soup.div.h1.text 
# print(headline)

title_list = soup.find_all('div', class_="jumbotron")

for title in title_list:
    ttle = title.h2.text
    body = title.p.text
    print(ttle)
    print(body)
