import re

class UrlManager:
    """
    爬虫url管理类,负责url的去重和分类(已下载,未下载)
    """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.pattern = re.compile(r'lol\.qq\.com')

    def put(self, url):
        if not url:
            raise 'url is None'

        if isinstance(url, str):
            if url not in self.old_urls and not self.pattern.search(url):
                self.new_urls.add(url)
        if isinstance(url, list) or isinstance(url, tuple):
            for i in url:
                self.put(i)

    def get(self):

        try:
            url = self.new_urls.pop()
            self.old_urls.add(url)
        except KeyError:
            raise 'url set is empty'

        return url

