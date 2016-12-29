import requests
from bs4 import BeautifulSoup


def fetchHTML(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    
    return resp.text


if __name__ == "__main__":
    url = "https://www.ptt.cc/bbs/Mix_Match/index.html"
    page_html = fetchHTML(url)
#    print(page_html)

    soup = BeautifulSoup(page_html, "html.parser")
    title_list = [title_html.text for title_html in soup.select(".title a")]
    for title in title_list:
        print(title)
