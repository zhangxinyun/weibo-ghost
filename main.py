from weibo import Weibo

wb = Weibo()
wb.start()
wb.login()
wb.search("python", page_count=10)
