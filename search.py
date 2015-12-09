#encoding:utf-8
from os import path

from ghost import Ghost
from bs4 import BeautifulSoup

ghost = Ghost(defaults={\
    "user_agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",\
    "viewport_size": (1280, 950)
    })

with ghost.start() as session:
    page, extra_resources = session.open("http://s.weibo.com/weibo/python")
    assert page.http_status == 200

    raw_data = session.content.encode('utf-8')

    file = open(path.abspath('content'), 'w')
    file.write(raw_data)
    file.close()

    content = BeautifulSoup(raw_data, 'html.parser')
    comments = content.find_all('p', class_='comment_txt')
    for comment in comments:
        print comment.get_text()
