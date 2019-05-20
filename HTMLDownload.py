
import requests
import re

class HtmlDownload:
    '''
        爬虫html下载类,请求网页返回response
    '''
    def __init__(self):
        self.headers = {
            'Host': 'qt.qq.com',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'GH-HEADER': '1-2-105-742-744233866',
            'User-Agent': 'QTL/7.4.2 (iPhone; iOS 12.2; Scale/2.00)',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Accept-Encoding': 'gzip, deflate',
        }
        Cookie = 'skey=M3x7iHJzqF;uin=o744233866;p_skey=amaC-c9J7d5nwABb-33xaMyz03vghea0OkLNNYO623I_;p_uin=o744233866'
        self.cookies = {x.split('=')[0]: x.split('=')[1] for x in Cookie.split(';')}
        self.pattern = re.compile(r'.*?//(?:www.)?(.*?)/.*')

    def get(self, url, params=None):
        domain = self.pattern.search(url).group(1)
        result = {'domain':domain, 'url':url}
        try:
            res = requests.get(url, params=params, cookies=self.cookies, headers=self.headers)
            res.raise_for_status()
        except Exception as e:
            print(e)
            res = None
        result['res'] = res
        return result

