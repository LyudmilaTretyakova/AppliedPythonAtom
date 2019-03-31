import sys

# Ваши импорты
import asyncio
import requests
from bs4 import BeautifulSoup
import collections
import csv


@asyncio.coroutine
def kinks(link):
    jk = []
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html5lib')
    zz = []
    z = soup.findAll("span", attrs={"class":
                                    "user-info__nickname user-info__nickname_small user-info__nickname_comment"})
    x = len(z)
    if x < 100:
        return 0
    else:
        for i in range(x):
            zz.append(z[i].contents[0])
        a = collections.Counter(zz).most_common()
        s = []
        a.sort(key=lambda x: (-x[1], x[0]))
        for i in range(len(a)):
            jk.append(link)
            jk.append(a[i][0])
            jk.append(a[i][1])
            s.append(jk)
            jk = []
        with open('top_user_comments.csv', 'a', newline="") as fp:
            writer = csv.writer(fp)
            writer.writerows(s)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    open(filename, 'w').close()
    links = sys.argv[1:4]
    lop = asyncio.get_event_loop()
    task = [
        asyncio.ensure_future(kinks(links[0])),
        asyncio.ensure_future(kinks(links[1])),
        asyncio.ensure_future(kinks(links[2]))
    ]
    wait = asyncio.wait(task)
    lop.run_until_complete(wait)
    lop.close()
