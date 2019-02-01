# coding=utf-8
import pymysql, os, configparser
from common.my_logger import logger


class Mysql(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.dirname(__file__)) + '/config/config.ini')
        self.host = config.get("MYSQL", "host")
        self.port = eval(config.get("MYSQL", "port"))
        self.user = config.get("MYSQL", "user")
        self.password = config.get("MYSQL", "password")
        self.db = config.get("MYSQL", "db")
        self._conn = self.get_conn()
        self._cursor = self._conn.cursor()

    # 数据库连接
    def get_conn(self):
        try:
            conn = pymysql.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.db,
                                   port=self.port,
                                   charset='utf8')
        except pymysql.Error as e:
            logger.error("[{}]connect database failed.{}".format(os.path.basename(__file__), e))
            conn = False
        return conn

    # 获取查询结果集
    def select_all(self, sql):
        try:
            self._cursor.execute(sql)
            res = self._cursor.fetchall()
            self._conn.commit()
        except pymysql.Error as e:
            res = False
            logger.warn("[{}]select database exception:{}".format(os.path.basename(__file__), e))
        return res

    # 获取查询结果集
    def select_one(self, sql):
        try:
            self._cursor.execute(sql)
            res = self._cursor.fetchone()  # 获取第一行数据
            # res = self._cursor.fetchmany(3)  # 获取前n行数据
            self._conn.commit()
        except pymysql.Error as e:
            res = False
            logger.warn("[{}]select database exception.{}".format(os.path.basename(__file__), e))
        return res

    def update(self, sql):
        try:
            self._cursor.execute(sql)
            self._conn.commit()
        except pymysql.Error as e:
            logger.warn("[{}]update database exception.{}".format(os.path.basename(__file__), e))
            self._conn.rollback()
            return False
        return True

    # 关闭数据库连接
    def close(self):
        try:
            self._cursor.close()  # 关闭游标
            self._conn.close()  # 释放数据库资源
        except pymysql.Error as e:
            logger.warn("[{}]close database exception.{}".format(os.path.basename(__file__), e))


mysql = Mysql()
# if __name__ == "__main__":
#     mysql = Mysql()
#     sql = "select * from user_info;"
#     all = mysql.select_all(sql)
#     print(all)

