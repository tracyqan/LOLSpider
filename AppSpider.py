
import time
try:
    from .HTMLDownload import HtmlDownload
    from .HTMLParse import HtmlParse
    from .URLManager import UrlManager
    from .Storage import Storage
except:
    from HTMLDownload import HtmlDownload
    from HTMLParse import HtmlParse
    from URLManager import UrlManager
    from Storage import Storage

class Spider:

    def __init__(self):
        self.start_url = 'http://qt.qq.com/lua/lol_news/recommend_refresh?cid=12&plat=ios&version=9862&areaid=12'
        self.html_download = HtmlDownload()
        self.html_parse = HtmlParse()
        self.url_manager = UrlManager()
        self.storage = Storage()

    def run(self):
        result = self.html_download.get(self.start_url)
        articles_info = result['res'].json()['update_list']
        for i in articles_info:
            article_url = i['article_url']
            self.url_manager.put(article_url)
        while True:
            try:
                url = self.url_manager.get()
                time.sleep(0.5)
            except:
                break
            print('*' * 50)
            print(url)
            article_res = self.html_download.get(url)
            data = self.html_parse.parse(article_res)
            self.storage.save(data)






if __name__ == '__main__':
    spider = Spider()
    spider.run()
