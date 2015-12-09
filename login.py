#encoding:utf-8
from os import path
from time import sleep

from ghost import Ghost

""" 登录

:param 用户名
:param 密码
:param 超时（以秒为单位）
"""
def login(username, password, timeout=10):
    # iPhone 6 Device
    ghost = Ghost(defaults={
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4",
        "viewport_size": (375, 667)
        })

    with ghost.start() as session:
        page, extra_resources = session.open("https://passport.weibo.cn/signin/login")
        assert page.http_status == 200
        session.wait_for_page_loaded()

        # login
        session.set_field_value('#loginName', username)
        session.set_field_value('#loginPassword', password)
        session.click('#loginAction')

        # wait for login
        sleep(timeout)

        # save cookies
        session.save_cookies(path.abspath('cookies'))