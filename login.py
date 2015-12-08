#encoding:utf-8
from ghost import Ghost

ghost = Ghost(defaults={\
    "user_agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"\
    })

with ghost.start() as session:
    page, extra_resources = session.open("http://weibo.com/")
    assert page.http_status == 200