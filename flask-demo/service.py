#coding:utf-8

import time
import datetime

import pymysql
import xlwt

from config import configs, sql


def _db():
    conf = configs['db']
    conf['charset'] = "utf8"
    conn = pymysql.connect(**conf)
    return conn.cursor()


def get_date():
    date = datetime.datetime.now()
    month = date.strftime('%Y-%m')
    day1 = month + '-01'
    day = date.strftime('%Y-%m-%d')
    return day1, day


def save_excel(data):
    name = str(int(time.time()))
    filename = '%s.xls' % name
    dir_name = './upload/' + filename

    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('result')
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            worksheet.write(i, j, data[i][j])
    workbook.save(dir_name)

    # f = open(filename, 'r')
    return filename

def get_hello(start_date, end_date):
    cur = _db()
    s = sql['hello'].format(start_date=start_date, end_date=end_date)
    cur.execute(s)
    return cur.fetchall()