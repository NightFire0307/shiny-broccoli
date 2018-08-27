# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate

import requests
import pymysql
from bs4 import BeautifulSoup

def db_table_create():
    sql = 'create table if not exists house (id int auto_increment, Title varchar (255) not null , Style varchar (255) not null , Info varchar (255) not null , Price varchar (255) not null , UnitPrice varchar (255), primary key (id))'
    cursor.execute(sql)

def main(number):
    sql = 'insert into house(Title, Style, Info, Price, UnitPrice) values (%s, %s, %s, %s, %s)'
    urls = 'https://sh.lianjia.com/ershoufang/pg' + str(number)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    reponse = requests.get(urls, headers=headers)
    html  = get_one_page(reponse)
    for detail in filter_page(html):
            # print(id, detail['Title'], detail['Style'], detail['Info'], detail['Price'], detail['unitPrice'])
            cursor.execute(sql, (detail['Title'], detail['Style'], detail['Info'], detail['Price'], detail['unitPrice']))
            db.commit()
            print('插入数据成功')

def get_one_page(response):
    if response.status_code == 200:
        return response.text

def filter_page(html):
    soup = BeautifulSoup(html, 'lxml')
    all_li = soup.find_all('li', {'class': 'clear'})
    for li in all_li:
        yield {
            'Title' : li.find('div', {'class': 'title'}).get_text(),
            'Style': li.find('div', {'class': 'positionInfo'}).get_text(),
            'Info': li.find('div', {'class': 'houseInfo'}).get_text(),
            'Price': li.find('div', {'class': 'totalPrice'}).get_text(),
            'unitPrice': li.find('div', {'class': 'unitPrice'}).get_text(),
        }

if __name__ == '__main__':
    db = pymysql.connect(host='192.168.26.116', user='root', password='wk123456', port=3306, db='lianjia', charset='utf8')
    print('Mysql已连接')
    cursor = db.cursor()
    db_table_create()

    for x in range(1, 11):
        main(x)

    db.close()


