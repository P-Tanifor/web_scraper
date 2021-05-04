import requests
from bs4 import BeautifulSoup
import string
import os

# user_url = input()
# response = requests.get(user_url)
# json_to_dict = response.json()
# if response.status_code == 200 and "content" in json_to_dict:
#     print(json_to_dict["content"])
# else:
#     print("Invalid quote resource!")

# url = input()
# r = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.5"})
# soup = BeautifulSoup(r.content, "html.parser")
# title = soup.find("h1")
# description = soup.find("div", {"class":"summary_text"})
# dict_ = {}
# if title and description:
#     title = title.text
#     description = description.text
#     dict_["title"] = title
#     dict_["description"] = description
#     print(dict_)
# else:
#     print("Invalid movie page!")


# user_url = input()
# r = requests.get(user_url)
# if r:
#     with open("source.html", 'wb') as source_file:
#         source_file.write(r.content)
#         print("Content saved.")
# else:
#     print(f"The URL returned {r.status_code}!")


# url = "https://www.nature.com/nature/articles"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "html.parser")
# articles_list = []
# for item in soup.findAll('article'):
#     news_articles = item.find('span', {'class':'c-meta__type'})
#     if "News" in news_articles:
#         news_link = item.find('a', {'data-track-action':'view article'}).get('href')
#         new_link = "https://www.nature.com" + news_link
#         response = requests.get(new_link, headers={"Accept-Language": "en-US,en;q=0.5"})
#         new_soup = BeautifulSoup(response.content, "html.parser")
#         title = new_soup.find('title').text.strip()
#         title = title.translate(str.maketrans('', '', string.punctuation))
#         trans_rule = title.maketrans(' ', '_')
#         title = title.translate(trans_rule)
#
#         body = new_soup.find('div', {'class':'article__body'}).text
#
#         with open(f"{title}.txt", 'ab') as articles:
#             body = bytes(body, 'utf-8')
#             articles.write(body)
#             articles_list.append(title + ".txt")
# print(articles_list)


number_of_pages = int(input())
type_of_article = input()
url = "https://www.nature.com/nature/articles"

for page_number in range(1, number_of_pages + 1):
    r = requests.get(url + '?page=' + str(page_number))
    soup = BeautifulSoup(r.content, "html.parser")
    os.mkdir(f'Page_{page_number}')
    for item in soup.findAll('article'):
        article_type = item.find('span', {'class': 'c-meta__type'})
        if type_of_article in article_type:
            article_link = item.find('a', {'data-track-action': 'view article'}).get('href')
            new_link = "https://www.nature.com" + article_link
            response = requests.get(new_link, headers={"Accept-Language": "en-US,en;q=0.5"})
            new_soup = BeautifulSoup(response.content, "html.parser")
            title = new_soup.find('title').text.strip()
            title = title.translate(str.maketrans('', '', string.punctuation))
            trans_rule = title.maketrans(' ', '_')
            title = title.translate(trans_rule)
            title = title + ".txt"

            if new_soup.find('div', {'class': 'article__body'}):
                body = new_soup.find('div', {'class': 'article__body'}).text
            else:
                body = new_soup.find('div', {'class': 'article-item__body'}).text

            with open(f"Page_{page_number}/{title}.txt", 'ab') as articles:
                body = bytes(body, 'utf-8')
                articles.write(body)
                #articles_list.append(title + ".txt")





