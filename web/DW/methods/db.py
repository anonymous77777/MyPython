#!/usr/bin/env Python
# coding=utf-8

#import MySQLdb
#conn = MySQLdb.connect(host="localhost", user="root", passwd="123123", db="qiwsirtest", port=3306, charset="utf8")

import sqlite3
conn = sqlite3.connect("methods/mytest.db")

cur = conn.cursor() #游标对象

#create_table = "create table users(id INTEGER not null primary key AUTOINCREMENT,username varchar(40),password text,email text)"
#cur.execute(create_table)
#c1 = 'insert into users(username,password,email) values("ly","123123","qiwsir@gmail.com")'
#cur.execute(c1)
#conn.commit()
#cur.close()
#conn.close()

def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_columns(table, column ):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines