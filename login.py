#encoding:utf-8
from ghost import Ghost

ghost = Ghost()

with ghost.start() as session:
    page, extra_resources = session.open("http://weibo.com/")
    assert page.http_status == 200