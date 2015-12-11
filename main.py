from weibo import Weibo

wb = Weibo()
wb.start()
wb.login()
wb.search("普元", page_count=10)
