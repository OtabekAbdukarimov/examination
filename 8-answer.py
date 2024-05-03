import requests
import bs4
import lxml

my_result=requests.get("https://tribuna.uz/")
soup=bs4.BeautifulSoup(my_result.content, "lxml")

result=soup.select(".news-title")
print(result)