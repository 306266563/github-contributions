import requests
from bs4 import BeautifulSoup

def simple_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string
    return None

if __name__ == "__main__":
    # print(simple_scraper('https://github.com'))
    pass

# Minor update 1 at 2026-06-02T14:09:43
# Minor update 2 at 2026-06-02T13:17:43
# Minor update 3 at 2026-06-02T18:11:43
# Minor update 4 at 2026-06-02T12:30:43
# Minor update 5 at 2026-06-02T13:25:43
# Minor update 6 at 2026-06-02T17:45:43
# Minor update 7 at 2026-06-02T14:44:43
# Minor update 8 at 2026-06-02T10:21:43