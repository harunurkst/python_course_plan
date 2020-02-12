from bs4 import BeautifulSoup

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


title_list = soup.find_all('div', class_="jumbotron")
for title in title_list:
    title_text = title.h2.text 
    body_text = title.p.text
    print(title_text)
    print(body_text)
    print("--------------")
