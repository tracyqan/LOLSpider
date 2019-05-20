
import pymysql

class Storage:

    def __init__(self, host='localhost', port=3306, user='root', password='root', db='app', charset='utf8'):
        """
        数据存储类,使用Mysql存储
        :param host: ip,默认未本机ip
        :param port: 端口,默认未3306
        :param user: 用户名,默认为root
        :param password: 密码,默认为root
        :param db: 数据库,默认为lol_app
        :param charset: 编码
        """

        self.conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        self.cursor = self.conn.cursor()
        sql_create_table = """create table if not exists lol_article (
                    id int primary key auto_increment,
                    title varchar(128),
                    author varchar(20),
                    public_time varchar(20),
                    contents text,
                    like_num varchar(20),
                    dislike_num varchar(20),
                    url varchar(128),
                    source varchar(20))
                  """
        self.cursor.execute(sql_create_table)
        self.conn.commit()

    def save(self, data):
        if data:
            title = data['title']
            author = data['author']
            public_time = data['public_time']
            contents = data['contents']
            like_num = data['like_num']
            dislike_num = data['dislike_num']
            url = data['url']
            source = data['source']
            sql_insert = """insert into lol_article (title, author, public_time, contents, like_num, dislike_num, url, source) 
                        values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(title, author, public_time, contents, like_num, dislike_num, url, source)
            # print(sql_insert)
            self.cursor.execute(sql_insert)
            self.conn.commit()
            print('文章:{}已存入数据库'.format(title))
