
from lxml import etree
import re

class HtmlParse:
    """html解析类,负责解析html,抓取相关信息
    """
    def __init__(self):
        self.time_pattern = re.compile(r'2019-.* \d{2}:\d{2}:\d{2}')
        self.author_pattern = re.compile(r'作者：\s*([^ ]+)')

    def parse(self, result):
        article = {}
        domain = result['domain']
        res = result['res']
        article['url'] = result['url']
        try:
            html = etree.HTML(res.text)
        except:
            article = {}
            return article
        if domain == 'qt.qq.com':
            article['title'] = html.xpath('//div[@class="article_box"]/h1/text()')[0]
            article['author'] = html.xpath('//div[@class="article_author"]/text()')[0]
            article['public_time'] = html.xpath('//div[@class="article_meta"]/text()')[0]
            contents = html.xpath('//div[@class="article_content"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = html.xpath('//span[@id="like_num"]/text()')[0]
            article['dislike_num'] = html.xpath('//span[@id="unlike_num"]/text()')[0]
            article['source'] = '企鹅电竞'

        elif domain == 'dadianjing.cn':
            article['title'] = html.xpath('//div[@class="title"]/text()')[0]
            author = html.xpath('//span[@class="from"]/text()')[0]
            article['author'] = author.split('：')[1]
            public_time = html.xpath('//span[@class="date"]/span/text()')
            article['public_time'] = ''.join(public_time)
            contents = html.xpath('//div[@class="content"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '大电竞'

        elif domain == 'nag.cn':
            article['title'] = html.xpath('//h1[@class="titleBlock"]/text()')[0]
            info = html.xpath('//div[@class="inforBlock"]')[0]
            article['author'] = self.author_pattern.search(info).group(1)
            article['public_time'] = self.time_pattern.search(info).group(1)
            contents = html.xpath('//div[@class="txtBlock"]//text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = html.xpath('//i[@class="num"]/text()')[0]
            article['dislike_num'] = ''
            article['source'] = '英雄电竞俱乐部'

        elif domain == 'loldk.com':
            article['title'] = html.xpath('//h2[@class="detail-title"]/text()')[0]
            article['author'] = html.xpath('//p[@class="detail-date"]/span/text()')[0].split('：')[1]
            article['public_time'] = html.xpath('//p[@class="detail-date"]/text()')[0].split()[0]
            contents = html.xpath('//div[@class="detail-cont"]//span/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '英雄联盟大咖'

        elif domain == 'titanar.com':
            article['title'] = html.xpath('//div[@class="cai_title"]/text()')[0]
            article['author'] = html.xpath('//div[@class="cai_source"]/div/text()')[0].split('：')[1]
            article['public_time'] = html.xpath('//div[@class="cai_viewdate"]/span/text()')[0]
            contents = html.xpath('//div[@class="cai_details"]//span/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '神之梯电竞'

        elif domain == 'chijizs.uuu9.com':
            article['title'] = html.xpath('//div[@class="robing_con clear_fix m-20"]/h1/text()')[0]
            info = html.xpath('//div[@id="textdetail"]/h4/text()')[0]
            article['author'] = self.author_pattern.search(info).group(1)
            article['public_time'] = self.time_pattern.search(info).group(1)
            contents = html.xpath('//div[@id="textdetail"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '游久英雄联盟'

        elif domain == 'famulei.com':
            article['title'] = html.xpath('//div[@class="main-top-title"]/text()')[0]
            article['author'] = html.xpath('//div[@class="desc-user-name"]/text()')[0]
            article['public_time'] = ''
            contents = html.xpath('//div[@class="main-top-cont"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '游乐场'

        elif domain == 'gamemei.com':
            article['title'] = html.xpath('//div[@class="Information-left-newscont"]/h2/text()')[0]
            info = html.xpath('//div[@class="Information-left-newscont-time"]/span/text()')
            info = ' '.join(info)
            article['author'] = self.author_pattern.search(info).group(1)
            article['public_time'] = self.time_pattern.search(info).group(1)
            contents = html.xpath('//div[@class="Information-left-newscont-news"]//text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '游戏魅'

        elif domain == 'l.zhangyoubao.com':
            article['title'] = html.xpath('//div[@class="article-box hb-md"]/h1/text()')[0]
            info = html.xpath('//div[@class="article-info"]/span/text()')
            article['author'] = info[0].split('：')[1]
            article['public_time'] = info[1]
            contents = html.xpath('//div[@class="article-content"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '掌游宝'

        elif domain == 'lol.dianjinghu.com':
            article['title'] = html.xpath('//div[@class="c-title"]/h1/text()')[0]
            info = html.xpath('//p[@class="time"]/text()')[0]
            article['author'] = '电竞虎'
            article['public_time'] = info.split('来')[0].strip()
            contents = html.xpath('//div[@class="new_conts"]/p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '电竞虎'

        elif domain == 'lol.te5.com':
            article['title'] = html.xpath('//h1[@class="fwr f30 arctitle"]/text()')[0]
            article['author'] = html.xpath('//span[@class="author"]/text()')[0].split('：')[1]
            article['public_time'] = html.xpath('//span[@class="time"]/text()')[0]
            contents = html.xpath('//div[@class="con f14"]/p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '特玩网'

        elif domain == 'lol.tuwan.com':
            article['title'] = html.xpath('//div[@class="Content-info-box"]/h1/text()')[0]
            article['author'] = html.xpath('//div[@class="Text-style"]/a[1]/text()')[0]
            article['public_time'] = html.xpath('//div[@class="Text-style"]/text()').split('作者：')[0]
            contents = html.xpath('//div[@class="con f14"]/p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '兔玩网'

        elif domain == 'lolfun.cn':
            article['title'] = html.xpath('//h1[@class="detail_container_title"]//text()')[0]
            article['public_time'] = html.xpath('//a[@class="detail_time"]//text()')[0]
            article['author'] = html.xpath('//a[@class="detail_zuoe"]//text()')[0]
            contents = html.xpath('//div[@id="content_page"]//font/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '暴龙电竞'

        elif domain == 'piu4.cn':
            article['title'] = html.xpath('//div[@class="content_title"]/h1/text()')[0]
            article['public_time'] = html.xpath('//span[@class="info_right"]/em[1]/text()')[0]
            article['author'] = '木木不哭'
            contents = html.xpath('//div[@class="content_article"]/div/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '木木不哭'

        elif domain == 'wanplus.com':
            article['title'] = html.xpath('//div[@id="shareTitle"]/text()')[0]
            article['public_time'] = html.xpath('//span[@class="com-time"]/text()')[0]
            article['author'] = html.xpath('//a[@class="com-name"]/text()')[0].strip()
            contents = html.xpath('//div[@class="com-article-content"]//p/text()')
            article['contents'] = ''.join(contents)
            article['like_num'] = ''
            article['dislike_num'] = ''
            article['source'] = '玩加电竞'

        else:
            article = {}

        print(article)
        return article