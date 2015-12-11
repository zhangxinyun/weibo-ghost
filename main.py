#encoding:utf-8
from weibo import Weibo

wb = Weibo()
wb.start()
wb.login()
wb.search(u"\u90ed\u5bcc\u57ce", page_count=50)
