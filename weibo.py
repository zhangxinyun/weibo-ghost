#encoding:utf-8
from os import path
from time import sleep

from yaml import safe_load

from ghost import Ghost
from bs4 import BeautifulSoup

class Weibo(object):
    def __init__(self):
        super(Weibo, self).__init__()
        
        yaml_file = open('conf.yml')
        self.config = safe_load(yaml_file)
        yaml_file.close()

        self.ghost = Ghost(defaults={
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4",
            "viewport_size": (375, 667)
            })

    def start(self):
        self.session = self.ghost.start()

    def exit(self):
        self.session.exit()
        self.ghost.exit()

    def login(self):
        if self.session:
            page, extra_resources = session.open("https://passport.weibo.cn/signin/login")
            assert page.http_status == 200
            self.session.wait_for_page_loaded()

            # login
            self.session.set_field_value('#loginName', self.config["username"])
            self.session.set_field_value('#loginPassword', self.config["password"])
            self.session.click('#loginAction')

            # wait for login
            self.session.wait_for_text("Anthony")

            # save cookies
            session.save_cookies(path.abspath('cookies'))
        else:
            self.start()
            self.login()
     
    def search(self, keyword, page_count=1):
        if self.session:
            for page_num in xrange(1,page_count):
                page_param = "&page=" + str(page_num)
                page, extra_resources = session.open("http://s.weibo.com/weibo/" + keyword + page_param)
                assert page.http_status == 200
                self.session.wait_for_page_loaded()

                # parse weibo text
                raw_data = session.content.encode('utf-8')
                content = BeautifulSoup(raw_data, 'html.parser')
                comments = content.find_all('p', class_='comment_txt')
                for comment in comments:
                    print comment.get_text()

                sleep()
        else:
            self.start()
            self.login()
            self.search(keyword)
