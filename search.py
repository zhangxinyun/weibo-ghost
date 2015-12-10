#encoding:utf-8
from os import path

from ghost import Ghost
from bs4 import BeautifulSoup

def search(keyword, page):

    # Config "page" parameter
    if page:
        page = "&page=" + page

    # Windows Chrome
    ghost = Ghost(defaults={
        "user_agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        "viewport_size": (1280, 950)
        })

    with ghost.start() as session:
        cookies_file_path = path.abspath('cookies')
        if path.exists(cookies_file_path):
            session.load_cookies(cookies_file_path)

        page, extra_resources = session.open("http://s.weibo.com/weibo/" + keyword + page)
        assert page.http_status == 200

        # parse weibo text
        raw_data = session.content.encode('utf-8')
        content = BeautifulSoup(raw_data, 'html.parser')
        comments = content.find_all('p', class_='comment_txt')
        for comment in comments:
            print comment.get_text()
